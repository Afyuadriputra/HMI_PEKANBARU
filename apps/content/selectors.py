from django.utils import timezone

from apps.content.models import Event, GalleryCategory, GalleryImage, NewsCategory, NewsPost, Program


def published_programs():
    return Program.objects.filter(status=Program.STATUS_PUBLISHED).order_by("sort_order", "-created_at")


def featured_programs(limit=6):
    return published_programs().filter(is_featured=True)[:limit]


def program_get_by_slug(slug):
    return Program.objects.get(slug=slug, status=Program.STATUS_PUBLISHED)


def program_list_admin():
    return Program.objects.select_related("created_by").order_by("sort_order", "-created_at")


def program_get(program_id):
    return Program.objects.get(pk=program_id)


def published_events():
    return Event.objects.filter(status=Event.STATUS_PUBLISHED).order_by("-start_date", "-created_at")


def upcoming_events(limit=None):
    queryset = published_events().filter(start_date__gte=timezone.localdate()).order_by("start_date", "-created_at")
    return queryset[:limit] if limit else queryset


def event_get_by_slug(slug):
    return Event.objects.get(slug=slug, status=Event.STATUS_PUBLISHED)


def event_list_admin():
    return Event.objects.select_related("created_by").order_by("-start_date", "-created_at")


def event_get(event_id):
    return Event.objects.get(pk=event_id)


def news_categories():
    return NewsCategory.objects.order_by("name")


def news_category_get(category_id):
    return NewsCategory.objects.get(pk=category_id)


def published_news():
    return NewsPost.objects.select_related("category", "created_by").filter(status=NewsPost.STATUS_PUBLISHED).order_by("-published_at", "-created_at")


def latest_news(limit=6):
    return published_news()[:limit]


def news_get_by_slug(slug):
    return NewsPost.objects.select_related("category", "created_by").get(slug=slug, status=NewsPost.STATUS_PUBLISHED)


def news_list_admin():
    return NewsPost.objects.select_related("category", "created_by").order_by("-created_at")


def news_get(news_id):
    return NewsPost.objects.select_related("category", "created_by").get(pk=news_id)


def gallery_categories():
    return GalleryCategory.objects.order_by("name")


def gallery_category_get(category_id):
    return GalleryCategory.objects.get(pk=category_id)


def visible_gallery_images():
    return GalleryImage.objects.select_related("category").filter(status=GalleryImage.STATUS_SHOW).order_by("sort_order", "-created_at")


def gallery_list_admin():
    return GalleryImage.objects.select_related("category", "uploaded_by").order_by("sort_order", "-created_at")


def gallery_image_get(image_id):
    return GalleryImage.objects.select_related("category", "uploaded_by").get(pk=image_id)
