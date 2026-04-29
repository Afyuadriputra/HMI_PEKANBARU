from django.contrib import admin

from apps.organization.models import ChairmanHistory, ManagementMember, OrganizationProfile


@admin.register(OrganizationProfile)
class OrganizationProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "short_name", "email", "phone", "updated_at")
    search_fields = ("name", "short_name", "email", "phone")


@admin.register(ManagementMember)
class ManagementMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "period", "sort_order", "status")
    list_filter = ("status", "period")
    search_fields = ("name", "position", "period")
    ordering = ("sort_order", "name")


@admin.register(ChairmanHistory)
class ChairmanHistoryAdmin(admin.ModelAdmin):
    list_display = ("name", "period_start", "period_end", "sort_order", "status")
    list_filter = ("status",)
    search_fields = ("name", "description")
    ordering = ("sort_order", "period_start")
