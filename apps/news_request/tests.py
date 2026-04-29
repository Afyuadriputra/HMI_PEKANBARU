from io import BytesIO

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from PIL import Image

from apps.core.test_factories import create_news_category, create_user
from apps.news_request.forms import NewsRequestPaymentForm, NewsUploadRequestForm
from apps.news_request.models import NewsRequestPayment, NewsUploadRequest
from apps.news_request.services import (
    approve_request,
    create_news_request,
    publish_news_request_as_post,
    upload_payment_proof,
    verify_payment,
)


def create_test_png(name="bukti.png"):
    buffer = BytesIO()
    Image.new("RGB", (1, 1), color="white").save(buffer, format="PNG")
    return SimpleUploadedFile(name, buffer.getvalue(), content_type="image/png")


class NewsRequestWorkflowTests(TestCase):
    def setUp(self):
        self.user = create_user()
        self.category = create_news_category()

    def _valid_request_form(self):
        return NewsUploadRequestForm(
            data={
                "requester_name": "Ahmad",
                "requester_email": "ahmad@example.com",
                "requester_phone": "08123456789",
                "title": "Kegiatan Komisariat",
                "category": self.category.id,
                "content": "Isi berita kegiatan komisariat.",
            }
        )

    def test_create_request_starts_pending_with_default_price_and_unpaid_payment(self):
        form = self._valid_request_form()
        self.assertTrue(form.is_valid(), form.errors)

        request = create_news_request(form)

        self.assertEqual(request.price, 50000)
        self.assertEqual(request.status, NewsUploadRequest.STATUS_PENDING)
        self.assertEqual(request.payment.amount, request.price)
        self.assertEqual(request.payment.payment_status, NewsRequestPayment.STATUS_UNPAID)

    def test_payment_upload_requires_real_proof_file(self):
        request = create_news_request(self._valid_request_form())
        form = NewsRequestPaymentForm(data={"payment_method": "Transfer Bank"}, instance=request.payment)

        self.assertFalse(form.is_valid())
        self.assertIn("payment_proof", form.errors)

    def test_upload_payment_marks_payment_paid_and_request_paid(self):
        request = create_news_request(self._valid_request_form())
        image = create_test_png()
        form = NewsRequestPaymentForm(
            data={"payment_method": "Transfer Bank"},
            files={"payment_proof": image},
            instance=request.payment,
        )

        self.assertTrue(form.is_valid(), form.errors)
        payment = upload_payment_proof(form)
        request.refresh_from_db()

        self.assertEqual(payment.payment_status, NewsRequestPayment.STATUS_PAID)
        self.assertEqual(request.status, NewsUploadRequest.STATUS_PAID)

    def test_admin_cannot_approve_request_before_payment_is_paid(self):
        request = create_news_request(self._valid_request_form())

        with self.assertRaises(ValidationError):
            approve_request(request, self.user)

    def test_verified_paid_request_can_be_approved_and_published_once(self):
        request = create_news_request(self._valid_request_form())
        request.status = NewsUploadRequest.STATUS_PAID
        request.save(update_fields=["status", "updated_at"])
        request.payment.payment_status = NewsRequestPayment.STATUS_PAID
        request.payment.save(update_fields=["payment_status", "updated_at"])

        verify_payment(request.payment, self.user)
        approved_request = approve_request(request, self.user, "Layak terbit")
        post = publish_news_request_as_post(approved_request, self.user)
        approved_request.refresh_from_db()

        self.assertEqual(approved_request.status, NewsUploadRequest.STATUS_PUBLISHED)
        self.assertEqual(post.request, approved_request)
        self.assertEqual(post.status, "published")
        self.assertEqual(post.slug, "kegiatan-komisariat")
