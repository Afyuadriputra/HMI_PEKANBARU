from django.contrib import admin

from apps.website.models import NavigationMenu, SiteSetting


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ("setting_key", "setting_value", "updated_at")
    search_fields = ("setting_key", "setting_value")


@admin.register(NavigationMenu)
class NavigationMenuAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "location", "sort_order", "status")
    list_filter = ("location", "status")
    search_fields = ("title", "url")
    ordering = ("location", "sort_order", "title")
