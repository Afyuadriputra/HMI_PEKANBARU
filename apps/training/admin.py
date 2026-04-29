from django.contrib import admin

from apps.training.models import (
    LkAssessment,
    LkAssessmentDetail,
    LkBatch,
    LkCertificate,
    LkLevel,
    LkMaterial,
    LkParticipant,
    Signature,
)


class LkAssessmentDetailInline(admin.TabularInline):
    model = LkAssessmentDetail
    extra = 0


@admin.register(LkLevel)
class LkLevelAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")


@admin.register(LkBatch)
class LkBatchAdmin(admin.ModelAdmin):
    list_display = ("title", "lk_level", "location", "start_date", "end_date", "status")
    list_filter = ("lk_level", "status", "start_date")
    search_fields = ("title", "theme", "location")


@admin.register(LkParticipant)
class LkParticipantAdmin(admin.ModelAdmin):
    list_display = ("full_name", "batch", "commissariat", "registration_status", "graduation_status")
    list_filter = ("batch", "commissariat", "registration_status", "graduation_status")
    search_fields = ("full_name", "email", "phone", "university")
    autocomplete_fields = ("batch", "cadre", "commissariat")


@admin.register(LkMaterial)
class LkMaterialAdmin(admin.ModelAdmin):
    list_display = ("title", "lk_level", "batch", "sort_order", "status")
    list_filter = ("lk_level", "batch", "status")
    search_fields = ("title", "description")


@admin.register(LkAssessment)
class LkAssessmentAdmin(admin.ModelAdmin):
    list_display = ("participant", "batch", "total_score", "final_grade", "result_status", "assessed_at")
    list_filter = ("batch", "result_status", "assessed_at")
    search_fields = ("participant__full_name", "final_grade", "notes")
    autocomplete_fields = ("participant", "batch", "assessor")
    inlines = (LkAssessmentDetailInline,)


@admin.register(Signature)
class SignatureAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "status")
    list_filter = ("status",)
    search_fields = ("name", "position")


@admin.register(LkCertificate)
class LkCertificateAdmin(admin.ModelAdmin):
    list_display = ("certificate_number", "participant", "assessment", "issued_date", "print_count")
    list_filter = ("issued_date", "signature")
    search_fields = ("certificate_number", "title", "participant__full_name")
    autocomplete_fields = ("participant", "assessment", "signature")
