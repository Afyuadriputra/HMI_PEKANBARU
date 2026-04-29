from django.conf import settings
from django.db import models

from apps.core.models import TimeStampedModel


class RegistrationForm(TimeStampedModel):
    TYPE_KADER = "kader"
    TYPE_LK1 = "lk1"
    TYPE_LK2 = "lk2"
    TYPE_LK3 = "lk3"
    TYPE_PROGRAM = "program"
    TYPE_AGENDA = "agenda"
    TYPE_OTHER = "other"

    TYPE_CHOICES = [
        (TYPE_KADER, "Kader"),
        (TYPE_LK1, "LK 1"),
        (TYPE_LK2, "LK 2"),
        (TYPE_LK3, "LK 3"),
        (TYPE_PROGRAM, "Program"),
        (TYPE_AGENDA, "Agenda"),
        (TYPE_OTHER, "Other"),
    ]

    STATUS_ACTIVE = "active"
    STATUS_INACTIVE = "inactive"

    STATUS_CHOICES = [
        (STATUS_ACTIVE, "Active"),
        (STATUS_INACTIVE, "Inactive"),
    ]

    title = models.CharField(max_length=150)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES, default=TYPE_KADER)
    google_form_url = models.TextField()
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_ACTIVE,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="created_registration_forms",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "registration_forms"
        ordering = ["title"]

    def __str__(self):
        return self.title