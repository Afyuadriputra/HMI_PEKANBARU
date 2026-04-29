from django.conf import settings
from django.db import models

from apps.core.models import TimeStampedModel


class SiteSetting(TimeStampedModel):
    setting_key = models.CharField(max_length=100, unique=True)
    setting_value = models.TextField(blank=True)

    class Meta:
        db_table = "site_settings"
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.setting_key


class NavigationMenu(TimeStampedModel):
    LOCATION_NAVBAR = "navbar"
    LOCATION_FOOTER = "footer"

    LOCATION_CHOICES = [
        (LOCATION_NAVBAR, "Navbar"),
        (LOCATION_FOOTER, "Footer"),
    ]

    STATUS_ACTIVE = "active"
    STATUS_INACTIVE = "inactive"

    STATUS_CHOICES = [
        (STATUS_ACTIVE, "Active"),
        (STATUS_INACTIVE, "Inactive"),
    ]

    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    location = models.CharField(
        max_length=20,
        choices=LOCATION_CHOICES,
        default=LOCATION_NAVBAR,
    )
    sort_order = models.IntegerField(default=0)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_ACTIVE,
    )

    class Meta:
        db_table = "navigation_menus"
        ordering = ["sort_order", "title"]

    def __str__(self):
        return self.title


class ContactMessage(TimeStampedModel):
    STATUS_UNREAD = "unread"
    STATUS_READ = "read"
    STATUS_REPLIED = "replied"

    STATUS_CHOICES = [
        (STATUS_UNREAD, "Unread"),
        (STATUS_READ, "Read"),
        (STATUS_REPLIED, "Replied"),
    ]

    sender_name = models.CharField(max_length=150)
    sender_email = models.EmailField(max_length=150)
    sender_phone = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_UNREAD,
    )
    handled_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="handled_contact_messages",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "contact_messages"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.sender_name} - {self.subject}"
