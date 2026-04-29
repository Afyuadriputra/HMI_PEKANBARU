from django.contrib import admin

from apps.cadre.models import Alumni, Cadre, CadreLkHistory, Commissariat


@admin.register(Commissariat)
class CommissariatAdmin(admin.ModelAdmin):
    list_display = ("name", "university", "contact_person", "phone", "status")
    list_filter = ("status",)
    search_fields = ("name", "university", "contact_person", "phone")


@admin.register(Cadre)
class CadreAdmin(admin.ModelAdmin):
    list_display = ("full_name", "commissariat", "university", "entry_year", "lk1_year", "cadre_status")
    list_filter = ("cadre_status", "commissariat", "entry_year", "lk1_year")
    search_fields = ("full_name", "email", "phone", "university", "major")
    autocomplete_fields = ("commissariat",)


@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    list_display = ("full_name", "commissariat", "profession", "workplace", "graduation_year")
    list_filter = ("commissariat", "graduation_year", "lk1_year")
    search_fields = ("full_name", "email", "phone", "profession", "workplace")
    autocomplete_fields = ("cadre", "commissariat")


@admin.register(CadreLkHistory)
class CadreLkHistoryAdmin(admin.ModelAdmin):
    list_display = ("cadre", "lk_level", "batch", "year", "status", "certificate_number")
    list_filter = ("lk_level", "status", "year")
    search_fields = ("cadre__full_name", "certificate_number")
    autocomplete_fields = ("cadre", "batch")
