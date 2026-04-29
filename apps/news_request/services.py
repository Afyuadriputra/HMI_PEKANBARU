from django.db import transaction
from django.core.exceptions import ValidationError
from django.utils import timezone

from apps.content.models import NewsPost
from apps.core.utils import generate_unique_slug
from apps.news_request.models import NewsRequestPayment, NewsUploadRequest


@transaction.atomic
def create_news_request(form):
    if hasattr(form, "validated_data") and not hasattr(form, "cleaned_data"):
        news_request = form.save(price=50000, status=NewsUploadRequest.STATUS_PENDING)
    else:
        news_request = form.save(commit=False)
        news_request.price = news_request.price or 50000
        news_request.status = NewsUploadRequest.STATUS_PENDING
        news_request.save()

    NewsRequestPayment.objects.create(request=news_request, amount=news_request.price)
    return news_request


@transaction.atomic
def upload_payment_proof(form):
    if hasattr(form, "validated_data") and not hasattr(form, "cleaned_data"):
        payment = form.save(payment_status=NewsRequestPayment.STATUS_PAID)
    else:
        payment = form.save(commit=False)
        payment.payment_status = NewsRequestPayment.STATUS_PAID
        payment.save()

    payment.payment_status = NewsRequestPayment.STATUS_PAID
    payment.request.status = NewsUploadRequest.STATUS_PAID
    payment.request.save(update_fields=["status", "updated_at"])
    payment.save(update_fields=["payment_status", "payment_method", "payment_proof", "updated_at"])
    return payment


@transaction.atomic
def verify_payment(payment, user):
    if payment.payment_status != NewsRequestPayment.STATUS_PAID:
        raise ValidationError("Pembayaran harus berstatus paid sebelum diverifikasi.")

    payment.payment_status = NewsRequestPayment.STATUS_VERIFIED
    payment.verified_by = user
    payment.verified_at = timezone.now()
    payment.request.status = NewsUploadRequest.STATUS_PAID
    payment.request.save(update_fields=["status", "updated_at"])
    payment.save(update_fields=["payment_status", "verified_by", "verified_at", "updated_at"])
    return payment


@transaction.atomic
def approve_request(news_request, user, notes=""):
    if news_request.status != NewsUploadRequest.STATUS_PAID:
        raise ValidationError("Request berita harus paid sebelum approve.")

    news_request.status = NewsUploadRequest.STATUS_APPROVED
    news_request.reviewed_by = user
    news_request.reviewed_at = timezone.now()
    news_request.notes = notes or news_request.notes
    news_request.save(update_fields=["status", "reviewed_by", "reviewed_at", "notes", "updated_at"])
    return news_request


@transaction.atomic
def reject_request(news_request, user, notes=""):
    news_request.status = NewsUploadRequest.STATUS_REJECTED
    news_request.reviewed_by = user
    news_request.reviewed_at = timezone.now()
    news_request.notes = notes or news_request.notes
    news_request.save(update_fields=["status", "reviewed_by", "reviewed_at", "notes", "updated_at"])
    return news_request


@transaction.atomic
def publish_news_request_as_post(news_request, user):
    if news_request.status != NewsUploadRequest.STATUS_APPROVED:
        raise ValidationError("Request berita harus approved sebelum publish.")

    post = NewsPost.objects.create(
        request=news_request,
        category=news_request.category,
        title=news_request.title,
        slug=generate_unique_slug(NewsPost, news_request.title),
        excerpt=news_request.content[:240],
        content=news_request.content,
        image=news_request.image,
        author_name=news_request.requester_name,
        published_at=timezone.now(),
        status=NewsPost.STATUS_PUBLISHED,
        created_by=user,
    )
    news_request.status = NewsUploadRequest.STATUS_PUBLISHED
    news_request.reviewed_by = user
    news_request.reviewed_at = timezone.now()
    news_request.save(update_fields=["status", "reviewed_by", "reviewed_at", "updated_at"])
    return post
