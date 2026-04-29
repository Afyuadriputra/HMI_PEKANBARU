from django.contrib import admin

from apps.content.models import (
    Event,
    GalleryCategory,
    GalleryImage,
    NewsCategory,
    NewsPost,
    Program,
)


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_featured", "sort_order", "status", "created_at")
    list_filter = ("status", "is_featured", "category")
    search_fields = ("title", "description", "content")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "start_date", "end_date", "is_featured", "status")
    list_filter = ("status", "is_featured", "start_date")
    search_fields = ("title", "location", "description", "content")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "author_name", "published_at", "status")
    list_filter = ("status", "category", "published_at")
    search_fields = ("title", "excerpt", "content", "author_name")
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ("category",)


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "sort_order", "status", "uploaded_by")
    list_filter = ("status", "category")
    search_fields = ("title", "alt_text", "description")
    autocomplete_fields = ("category",)
