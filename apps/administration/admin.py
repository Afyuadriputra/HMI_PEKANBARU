from django.contrib import admin

from apps.administration.models import (
    DocumentArchive,
    EmailLog,
    GmailIntegration,
    IncomingLetter,
    Invitation,
    OutgoingLetter,
)


@admin.register(DocumentArchive)
class DocumentArchiveAdmin(admin.ModelAdmin):
    list_display = ("title", "archive_number", "category", "archive_date", "uploaded_by")
    list_filter = ("category", "archive_date")
    search_fields = ("title", "archive_number", "description")


@admin.register(IncomingLetter)
class IncomingLetterAdmin(admin.ModelAdmin):
    list_display = ("letter_number", "sender", "subject", "received_date", "status")
    list_filter = ("status", "received_date")
    search_fields = ("letter_number", "sender", "subject", "description")


@admin.register(OutgoingLetter)
class OutgoingLetterAdmin(admin.ModelAdmin):
    list_display = ("letter_number", "recipient", "subject", "letter_date", "status", "sent_at")
    list_filter = ("status", "letter_date", "sent_at")
    search_fields = ("letter_number", "recipient", "recipient_email", "subject")


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ("invitation_number", "recipient", "subject", "invitation_date", "event_date", "status")
    list_filter = ("status", "invitation_date", "event_date")
    search_fields = ("invitation_number", "recipient", "recipient_email", "subject")
    autocomplete_fields = ("event",)


@admin.register(GmailIntegration)
class GmailIntegrationAdmin(admin.ModelAdmin):
    list_display = ("email", "status", "token_expired_at", "connected_by")
    list_filter = ("status",)
    search_fields = ("email",)


@admin.register(EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    list_display = ("recipient_email", "subject", "status", "related_type", "related_id", "sent_at")
    list_filter = ("status", "related_type", "sent_at")
    search_fields = ("recipient_email", "subject", "error_message")
