from django.contrib import admin

from apps.registration.models import RegistrationForm


@admin.register(RegistrationForm)
class RegistrationFormAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "status", "created_by", "updated_at")
    list_filter = ("type", "status")
    search_fields = ("title", "description", "google_form_url")
