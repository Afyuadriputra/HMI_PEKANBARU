from django.db import models

from apps.core.models import TimeStampedModel


class Commissariat(TimeStampedModel):
    STATUS_ACTIVE = "active"
    STATUS_INACTIVE = "inactive"

    STATUS_CHOICES = [
        (STATUS_ACTIVE, "Active"),
        (STATUS_INACTIVE, "Inactive"),
    ]

    name = models.CharField(max_length=150)
    university = models.CharField(max_length=150, blank=True)
    address = models.TextField(blank=True)
    contact_person = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_ACTIVE,
    )

    class Meta:
        db_table = "commissariats"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Cadre(TimeStampedModel):
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"

    GENDER_CHOICES = [
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    ]

    STATUS_ACTIVE = "active"
    STATUS_ALUMNI = "alumni"
    STATUS_INACTIVE = "inactive"

    STATUS_CHOICES = [
        (STATUS_ACTIVE, "Active"),
        (STATUS_ALUMNI, "Alumni"),
        (STATUS_INACTIVE, "Inactive"),
    ]

    commissariat = models.ForeignKey(
        Commissariat,
        on_delete=models.SET_NULL,
        related_name="cadres",
        blank=True,
        null=True,
    )
    full_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True)
    birth_place = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    university = models.CharField(max_length=150, blank=True)
    faculty = models.CharField(max_length=150, blank=True)
    major = models.CharField(max_length=150, blank=True)
    entry_year = models.IntegerField(blank=True, null=True)
    lk1_year = models.IntegerField(blank=True, null=True)
    cadre_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_ACTIVE,
    )
    photo = models.ImageField(upload_to="cadres/photos/", blank=True, null=True)
    notes = models.TextField(blank=True)

    class Meta:
        db_table = "cadres"
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name


class Alumni(TimeStampedModel):
    cadre = models.ForeignKey(
        Cadre,
        on_delete=models.SET_NULL,
        related_name="alumni_records",
        blank=True,
        null=True,
    )
    commissariat = models.ForeignKey(
        Commissariat,
        on_delete=models.SET_NULL,
        related_name="alumni",
        blank=True,
        null=True,
    )
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    profession = models.CharField(max_length=150, blank=True)
    workplace = models.CharField(max_length=150, blank=True)
    position = models.CharField(max_length=150, blank=True)
    graduation_year = models.IntegerField(blank=True, null=True)
    lk1_year = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True)
    photo = models.ImageField(upload_to="alumni/photos/", blank=True, null=True)
    notes = models.TextField(blank=True)

    class Meta:
        db_table = "alumni"
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name


class CadreLkHistory(TimeStampedModel):
    STATUS_REGISTERED = "registered"
    STATUS_PASSED = "passed"
    STATUS_FAILED = "failed"

    STATUS_CHOICES = [
        (STATUS_REGISTERED, "Registered"),
        (STATUS_PASSED, "Passed"),
        (STATUS_FAILED, "Failed"),
    ]

    cadre = models.ForeignKey(
        Cadre,
        on_delete=models.CASCADE,
        related_name="lk_histories",
    )
    lk_level = models.ForeignKey(
        "training.LkLevel",
        on_delete=models.PROTECT,
        related_name="cadre_histories",
    )
    batch = models.ForeignKey(
        "training.LkBatch",
        on_delete=models.SET_NULL,
        related_name="cadre_histories",
        blank=True,
        null=True,
    )
    year = models.IntegerField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_REGISTERED,
    )
    certificate_number = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = "cadre_lk_histories"
        ordering = ["-year", "-created_at"]

    def __str__(self):
        return f"{self.cadre} - {self.lk_level}"