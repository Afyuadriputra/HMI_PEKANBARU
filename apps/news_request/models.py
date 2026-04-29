import uuid

from django.conf import settings
from django.db import models

from apps.core.models import TimeStampedModel


class NewsUploadRequest(TimeStampedModel):
    STATUS_PENDING = "pending"
    STATUS_WAITING_PAYMENT = "waiting_payment"
    STATUS_PAID = "paid"
    STATUS_APPROVED = "approved"
    STATUS_REJECTED = "rejected"
    STATUS_PUBLISHED = "published"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_WAITING_PAYMENT, "Waiting Payment"),
        (STATUS_PAID, "Paid"),
        (STATUS_APPROVED, "Approved"),
        (STATUS_REJECTED, "Rejected"),
        (STATUS_PUBLISHED, "Published"),
    ]

    requester_name = models.CharField(max_length=150)
    requester_email = models.EmailField(max_length=150, blank=True)
    requester_phone = models.CharField(max_length=50, blank=True)
    tracking_code = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(
        "content.NewsCategory",
        on_delete=models.SET_NULL,
        related_name="upload_requests",
        blank=True,
        null=True,
    )
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="news_requests/images/", blank=True, null=True)
    attachment = models.FileField(
        upload_to="news_requests/attachments/",
        blank=True,
        null=True,
    )
    price = models.DecimalField(max_digits=12, decimal_places=2, default=50000)
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="reviewed_news_requests",
        blank=True,
        null=True,
    )
    reviewed_at = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True)

    class Meta:
        db_table = "news_upload_requests"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class NewsRequestPayment(TimeStampedModel):
    STATUS_UNPAID = "unpaid"
    STATUS_PAID = "paid"
    STATUS_VERIFIED = "verified"
    STATUS_REJECTED = "rejected"

    STATUS_CHOICES = [
        (STATUS_UNPAID, "Unpaid"),
        (STATUS_PAID, "Paid"),
        (STATUS_VERIFIED, "Verified"),
        (STATUS_REJECTED, "Rejected"),
    ]

    request = models.OneToOneField(
        NewsUploadRequest,
        on_delete=models.CASCADE,
        related_name="payment",
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=50000)
    payment_method = models.CharField(max_length=100, blank=True)
    payment_proof = models.ImageField(
        upload_to="news_requests/payment_proofs/",
        blank=True,
        null=True,
    )
    payment_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_UNPAID,
    )
    verified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="verified_news_request_payments",
        blank=True,
        null=True,
    )
    verified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "news_request_payments"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.request.title} - {self.payment_status}"
