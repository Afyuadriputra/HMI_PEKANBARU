from django.db import models

from apps.core.models import TimeStampedModel


class OrganizationProfile(TimeStampedModel):
    name = models.CharField(max_length=150)
    short_name = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    history = models.TextField(blank=True)
    vision = models.TextField(blank=True)
    mission = models.TextField(blank=True)
    logo = models.ImageField(upload_to="organization/logo/", blank=True, null=True)
    profile_image = models.ImageField(
        upload_to="organization/profile/",
        blank=True,
        null=True,
    )
    founded_year = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True)
    email = models.EmailField(max_length=150, blank=True)
    phone = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = "organization_profile"
        verbose_name = "Organization Profile"
        verbose_name_plural = "Organization Profile"

    def __str__(self):
        return self.name


class ManagementMember(TimeStampedModel):
    STATUS_ACTIVE = "active"
    STATUS_INACTIVE = "inactive"

    STATUS_CHOICES = [
        (STATUS_ACTIVE, "Active"),
        (STATUS_INACTIVE, "Inactive"),
    ]

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="management/photos/", blank=True, null=True)
    period = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    sort_order = models.IntegerField(default=0)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_ACTIVE,
    )

    class Meta:
        db_table = "management_members"
        ordering = ["sort_order", "name"]

    def __str__(self):
        return f"{self.name} - {self.position}"


class ChairmanHistory(TimeStampedModel):
    STATUS_SHOW = "show"
    STATUS_HIDE = "hide"

    STATUS_CHOICES = [
        (STATUS_SHOW, "Show"),
        (STATUS_HIDE, "Hide"),
    ]

    name = models.CharField(max_length=100)
    period_start = models.IntegerField(blank=True, null=True)
    period_end = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to="chairman/photos/", blank=True, null=True)
    description = models.TextField(blank=True)
    sort_order = models.IntegerField(default=0)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_SHOW,
    )

    class Meta:
        db_table = "chairman_histories"
        ordering = ["sort_order", "period_start"]

    def __str__(self):
        return self.name