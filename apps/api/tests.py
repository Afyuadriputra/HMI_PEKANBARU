from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from apps.content.models import GalleryCategory, GalleryImage, NewsPost, Program
from apps.core.test_factories import create_news_category, create_user
from apps.news_request.models import NewsRequestPayment, NewsUploadRequest
from apps.organization.models import OrganizationProfile
from apps.website.models import ContactMessage, NavigationMenu, SiteSetting


class PublicApiContractTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = create_user()
        self.category = create_news_category()
        self.gallery_category = GalleryCategory.objects.create(name="LK 1", slug="lk-1")
        SiteSetting.objects.create(setting_key="site_name", setting_value="SI-HMI Pekanbaru")
        NavigationMenu.objects.create(title="Beranda", url="/", location=NavigationMenu.LOCATION_NAVBAR)
        OrganizationProfile.objects.create(name="HMI Cabang Pekanbaru", short_name="HMI Pekanbaru")
        Program.objects.create(
            title="Basic Training",
            slug="basic-training",
            description="Program kaderisasi",
            status=Program.STATUS_PUBLISHED,
            is_featured=True,
        )
        NewsPost.objects.create(
            category=self.category,
            title="Berita Publik",
            slug="berita-publik",
            excerpt="Ringkasan",
            content="Isi berita",
            status=NewsPost.STATUS_PUBLISHED,
            created_by=self.user,
        )
        GalleryImage.objects.create(
            category=self.gallery_category,
            title="Foto LK 1",
            image="gallery/images/lk1.jpg",
            status=GalleryImage.STATUS_SHOW,
        )

    def test_home_contract_returns_frontend_ready_sections(self):
        response = self.client.get(reverse("api:home"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["settings"]["site_name"], "SI-HMI Pekanbaru")
        self.assertEqual(response.data["navigation"][0]["title"], "Beranda")
        self.assertEqual(response.data["profile"]["name"], "HMI Cabang Pekanbaru")
        self.assertEqual(response.data["featured_programs"][0]["slug"], "basic-training")
        self.assertEqual(response.data["latest_news"][0]["slug"], "berita-publik")

    def test_contact_message_create_stores_unread_message(self):
        response = self.client.post(
            reverse("api:contact_message_create"),
            {
                "sender_name": "Siti",
                "sender_email": "siti@example.com",
                "sender_phone": "08123456788",
                "subject": "Kerja sama",
                "message": "Saya ingin bertanya soal program HMI.",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["status"], ContactMessage.STATUS_UNREAD)
        self.assertTrue(ContactMessage.objects.filter(sender_email="siti@example.com").exists())

    def test_news_categories_contract_available_for_filter_ui(self):
        response = self.client.get(reverse("api:news_category_list"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["slug"], self.category.slug)

    def test_gallery_categories_and_gallery_filter_contract(self):
        category_response = self.client.get(reverse("api:gallery_category_list"))
        gallery_response = self.client.get(reverse("api:gallery_list"), {"category": "lk-1"})

        self.assertEqual(category_response.status_code, 200)
        self.assertEqual(category_response.data[0]["slug"], "lk-1")
        self.assertEqual(gallery_response.status_code, 200)
        self.assertEqual(gallery_response.data["count"], 1)
        self.assertEqual(gallery_response.data["results"][0]["title"], "Foto LK 1")

    def test_program_list_only_returns_published_programs(self):
        Program.objects.create(title="Draft Program", slug="draft-program", status=Program.STATUS_DRAFT)

        response = self.client.get(reverse("api:program_list"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["slug"], "basic-training")

    def test_news_request_create_returns_contract_status_and_payment_row(self):
        response = self.client.post(
            reverse("api:news_request_create"),
            {
                "requester_name": "Ahmad",
                "requester_email": "ahmad@example.com",
                "requester_phone": "08123456789",
                "title": "Kegiatan Komisariat",
                "category": self.category.id,
                "content": "Isi berita dari pengunjung.",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["status"], NewsUploadRequest.STATUS_PENDING)
        self.assertIn("tracking_code", response.data)
        news_request = NewsUploadRequest.objects.get(pk=response.data["id"])
        self.assertEqual(news_request.payment.payment_status, NewsRequestPayment.STATUS_UNPAID)

        tracking_response = self.client.get(
            reverse("api:news_request_tracking", kwargs={"tracking_code": news_request.tracking_code})
        )

        self.assertEqual(tracking_response.status_code, 200)
        self.assertEqual(tracking_response.data["tracking_code"], str(news_request.tracking_code))
        self.assertEqual(tracking_response.data["payment_status"], NewsRequestPayment.STATUS_UNPAID)

    def test_openapi_schema_is_available_for_react_contract(self):
        response = self.client.get(reverse("api_schema"))

        self.assertEqual(response.status_code, 200)
        self.assertIn("openapi", response.data)
