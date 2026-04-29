from django.conf import settings
from django.db import models

from apps.core.models import TimeStampedModel


class LkLevel(TimeStampedModel):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        db_table = "lk_levels"
        ordering = ["id"]

    def __str__(self):
        return self.name


class LkBatch(TimeStampedModel):
    STATUS_DRAFT = "draft"
    STATUS_OPEN = "open"
    STATUS_CLOSED = "closed"
    STATUS_FINISHED = "finished"

    STATUS_CHOICES = [
        (STATUS_DRAFT, "Draft"),
        (STATUS_OPEN, "Open"),
        (STATUS_CLOSED, "Closed"),
        (STATUS_FINISHED, "Finished"),
    ]

    lk_level = models.ForeignKey(
        LkLevel,
        on_delete=models.PROTECT,
        related_name="batches",
    )
    title = models.CharField(max_length=150)
    theme = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=150, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    registration_open = models.DateField(blank=True, null=True)
    registration_close = models.DateField(blank=True, null=True)
    registration_form_url = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_DRAFT,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="created_lk_batches",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "lk_batches"
        ordering = ["-start_date", "-created_at"]

    def __str__(self):
        return self.title


class LkParticipant(TimeStampedModel):
    REGISTRATION_REGISTERED = "registered"
    REGISTRATION_VERIFIED = "verified"
    REGISTRATION_REJECTED = "rejected"

    REGISTRATION_STATUS_CHOICES = [
        (REGISTRATION_REGISTERED, "Registered"),
        (REGISTRATION_VERIFIED, "Verified"),
        (REGISTRATION_REJECTED, "Rejected"),
    ]

    GRADUATION_NOT_ASSESSED = "not_assessed"
    GRADUATION_PASSED = "passed"
    GRADUATION_FAILED = "failed"

    GRADUATION_STATUS_CHOICES = [
        (GRADUATION_NOT_ASSESSED, "Not Assessed"),
        (GRADUATION_PASSED, "Passed"),
        (GRADUATION_FAILED, "Failed"),
    ]

    batch = models.ForeignKey(
        LkBatch,
        on_delete=models.CASCADE,
        related_name="participants",
    )
    cadre = models.ForeignKey(
        "cadre.Cadre",
        on_delete=models.SET_NULL,
        related_name="lk_participants",
        blank=True,
        null=True,
    )
    commissariat = models.ForeignKey(
        "cadre.Commissariat",
        on_delete=models.SET_NULL,
        related_name="lk_participants",
        blank=True,
        null=True,
    )
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    university = models.CharField(max_length=150, blank=True)
    faculty = models.CharField(max_length=150, blank=True)
    major = models.CharField(max_length=150, blank=True)
    semester = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    motivation = models.TextField(blank=True)
    photo = models.ImageField(upload_to="lk/participants/", blank=True, null=True)
    registration_status = models.CharField(
        max_length=20,
        choices=REGISTRATION_STATUS_CHOICES,
        default=REGISTRATION_REGISTERED,
    )
    graduation_status = models.CharField(
        max_length=20,
        choices=GRADUATION_STATUS_CHOICES,
        default=GRADUATION_NOT_ASSESSED,
    )

    class Meta:
        db_table = "lk_participants"
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name


class LkMaterial(TimeStampedModel):
    STATUS_ACTIVE = "active"
    STATUS_INACTIVE = "inactive"

    STATUS_CHOICES = [
        (STATUS_ACTIVE, "Active"),
        (STATUS_INACTIVE, "Inactive"),
    ]

    lk_level = models.ForeignKey(
        LkLevel,
        on_delete=models.PROTECT,
        related_name="materials",
    )
    batch = models.ForeignKey(
        LkBatch,
        on_delete=models.CASCADE,
        related_name="materials",
        blank=True,
        null=True,
    )
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    sort_order = models.IntegerField(default=0)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_ACTIVE,
    )

    class Meta:
        db_table = "lk_materials"
        ordering = ["sort_order", "title"]

    def __str__(self):
        return self.title


class LkAssessment(TimeStampedModel):
    RESULT_PASSED = "passed"
    RESULT_FAILED = "failed"
    RESULT_PENDING = "pending"

    RESULT_STATUS_CHOICES = [
        (RESULT_PASSED, "Passed"),
        (RESULT_FAILED, "Failed"),
        (RESULT_PENDING, "Pending"),
    ]

    participant = models.ForeignKey(
        LkParticipant,
        on_delete=models.CASCADE,
        related_name="assessments",
    )
    batch = models.ForeignKey(
        LkBatch,
        on_delete=models.CASCADE,
        related_name="assessments",
    )
    assessor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="lk_assessments",
        blank=True,
        null=True,
    )
    total_score = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
    )
    final_grade = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)
    result_status = models.CharField(
        max_length=20,
        choices=RESULT_STATUS_CHOICES,
        default=RESULT_PENDING,
    )
    assessed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "lk_assessments"
        ordering = ["-assessed_at", "-created_at"]

    def __str__(self):
        return f"{self.participant} - {self.batch}"


class LkAssessmentDetail(TimeStampedModel):
    assessment = models.ForeignKey(
        LkAssessment,
        on_delete=models.CASCADE,
        related_name="details",
    )
    material = models.ForeignKey(
        LkMaterial,
        on_delete=models.CASCADE,
        related_name="assessment_details",
    )
    score = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
    )
    grade = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        db_table = "lk_assessment_details"

    def __str__(self):
        return f"{self.assessment} - {self.material}"


class Signature(TimeStampedModel):
    STATUS_ACTIVE = "active"
    STATUS_INACTIVE = "inactive"

    STATUS_CHOICES = [
        (STATUS_ACTIVE, "Active"),
        (STATUS_INACTIVE, "Inactive"),
    ]

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    signature_image = models.ImageField(
        upload_to="signatures/images/",
        blank=True,
        null=True,
    )
    stamp_image = models.ImageField(
        upload_to="signatures/stamps/",
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_ACTIVE,
    )

    class Meta:
        db_table = "signatures"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} - {self.position}"


class LkCertificate(TimeStampedModel):
    participant = models.ForeignKey(
        LkParticipant,
        on_delete=models.CASCADE,
        related_name="certificates",
    )
    assessment = models.ForeignKey(
        LkAssessment,
        on_delete=models.SET_NULL,
        related_name="certificates",
        blank=True,
        null=True,
    )
    certificate_number = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=150, blank=True)
    issued_date = models.DateField(blank=True, null=True)
    signature = models.ForeignKey(
        Signature,
        on_delete=models.SET_NULL,
        related_name="certificates",
        blank=True,
        null=True,
    )
    file_path = models.FileField(
        upload_to="lk/certificates/",
        blank=True,
        null=True,
    )
    print_count = models.IntegerField(default=0)

    class Meta:
        db_table = "lk_certificates"
        ordering = ["-issued_date", "-created_at"]

    def __str__(self):
        return self.certificate_number