from django.conf import settings
from django.db import models

from apps.core.models import TimeStampedModel


class DocumentArchive(TimeStampedModel):
    title = models.CharField(max_length=150)
    archive_number = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    file_path = models.FileField(upload_to="archives/documents/", blank=True, null=True)
    archive_date = models.DateField(blank=True, null=True)
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="uploaded_document_archives",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "document_archives"
        ordering = ["-archive_date", "-created_at"]

    def __str__(self):
        return self.title


class IncomingLetter(TimeStampedModel):
    STATUS_NEW = "new"
    STATUS_PROCESSED = "processed"
    STATUS_ARCHIVED = "archived"

    STATUS_CHOICES = [
        (STATUS_NEW, "New"),
        (STATUS_PROCESSED, "Processed"),
        (STATUS_ARCHIVED, "Archived"),
    ]

    letter_number = models.CharField(max_length=100, blank=True)
    sender = models.CharField(max_length=150, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    received_date = models.DateField(blank=True, null=True)
    letter_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    file_path = models.FileField(
        upload_to="letters/incoming/",
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_NEW,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="created_incoming_letters",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "incoming_letters"
        ordering = ["-received_date", "-created_at"]

    def __str__(self):
        return self.subject or self.letter_number


class OutgoingLetter(TimeStampedModel):
    STATUS_DRAFT = "draft"
    STATUS_SENT = "sent"
    STATUS_ARCHIVED = "archived"

    STATUS_CHOICES = [
        (STATUS_DRAFT, "Draft"),
        (STATUS_SENT, "Sent"),
        (STATUS_ARCHIVED, "Archived"),
    ]

    letter_number = models.CharField(max_length=100, blank=True)
    recipient = models.CharField(max_length=150, blank=True)
    recipient_email = models.EmailField(max_length=150, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    letter_date = models.DateField(blank=True, null=True)
    content = models.TextField(blank=True)
    file_path = models.FileField(
        upload_to="letters/outgoing/",
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_DRAFT,
    )
    sent_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="created_outgoing_letters",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "outgoing_letters"
        ordering = ["-letter_date", "-created_at"]

    def __str__(self):
        return self.subject or self.letter_number


class Invitation(TimeStampedModel):
    STATUS_DRAFT = "draft"
    STATUS_SENT = "sent"
    STATUS_ARCHIVED = "archived"

    STATUS_CHOICES = [
        (STATUS_DRAFT, "Draft"),
        (STATUS_SENT, "Sent"),
        (STATUS_ARCHIVED, "Archived"),
    ]

    invitation_number = models.CharField(max_length=100, blank=True)
    event = models.ForeignKey(
        "content.Event",
        on_delete=models.SET_NULL,
        related_name="invitations",
        blank=True,
        null=True,
    )
    recipient = models.CharField(max_length=150, blank=True)
    recipient_email = models.EmailField(max_length=150, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    invitation_date = models.DateField(blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=150, blank=True)
    file_path = models.FileField(
        upload_to="letters/invitations/",
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_DRAFT,
    )
    sent_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="created_invitations",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "invitations"
        ordering = ["-invitation_date", "-created_at"]

    def __str__(self):
        return self.subject or self.invitation_number


class GmailIntegration(TimeStampedModel):
    STATUS_CONNECTED = "connected"
    STATUS_DISCONNECTED = "disconnected"

    STATUS_CHOICES = [
        (STATUS_CONNECTED, "Connected"),
        (STATUS_DISCONNECTED, "Disconnected"),
    ]

    email = models.EmailField(max_length=150)
    access_token = models.TextField(blank=True)
    refresh_token = models.TextField(blank=True)
    token_expired_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_DISCONNECTED,
    )
    connected_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="gmail_integrations",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "gmail_integrations"

    def __str__(self):
        return self.email


class EmailLog(TimeStampedModel):
    STATUS_PENDING = "pending"
    STATUS_SENT = "sent"
    STATUS_FAILED = "failed"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_SENT, "Sent"),
        (STATUS_FAILED, "Failed"),
    ]

    gmail_integration = models.ForeignKey(
        GmailIntegration,
        on_delete=models.SET_NULL,
        related_name="email_logs",
        blank=True,
        null=True,
    )
    related_type = models.CharField(max_length=100, blank=True)
    related_id = models.BigIntegerField(blank=True, null=True)
    recipient_email = models.EmailField(max_length=150, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )
    sent_at = models.DateTimeField(blank=True, null=True)
    error_message = models.TextField(blank=True)

    class Meta:
        db_table = "email_logs"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.recipient_email} - {self.status}"