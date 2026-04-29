from django.conf import settings
from django.db import models

from apps.core.models import TimeStampedModel


class Program(TimeStampedModel):
    STATUS_DRAFT = "draft"
    STATUS_PUBLISHED = "published"

    STATUS_CHOICES = [
        (STATUS_DRAFT, "Draft"),
        (STATUS_PUBLISHED, "Published"),
    ]

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=180, unique=True)
    category = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="programs/images/", blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True)
    is_featured = models.BooleanField(default=False)
    button_text = models.CharField(max_length=100, blank=True)
    button_link = models.CharField(max_length=255, blank=True)
    registration_form_url = models.TextField(blank=True)
    sort_order = models.IntegerField(default=0)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PUBLISHED,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="created_programs",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "programs"
        ordering = ["sort_order", "-created_at"]

    def __str__(self):
        return self.title


class Event(TimeStampedModel):
    STATUS_DRAFT = "draft"
    STATUS_PUBLISHED = "published"
    STATUS_FINISHED = "finished"

    STATUS_CHOICES = [
        (STATUS_DRAFT, "Draft"),
        (STATUS_PUBLISHED, "Published"),
        (STATUS_FINISHED, "Finished"),
    ]

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=180, unique=True)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="events/images/", blank=True, null=True)
    location = models.CharField(max_length=150, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    registration_form_url = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PUBLISHED,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="created_events",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "events"
        ordering = ["-start_date", "-created_at"]

    def __str__(self):
        return self.title


class NewsCategory(TimeStampedModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        db_table = "news_categories"
        verbose_name = "News Category"
        verbose_name_plural = "News Categories"

    def __str__(self):
        return self.name


class NewsPost(TimeStampedModel):
    STATUS_DRAFT = "draft"
    STATUS_PUBLISHED = "published"

    STATUS_CHOICES = [
        (STATUS_DRAFT, "Draft"),
        (STATUS_PUBLISHED, "Published"),
    ]

    category = models.ForeignKey(
        NewsCategory,
        on_delete=models.SET_NULL,
        related_name="posts",
        blank=True,
        null=True,
    )
    request = models.ForeignKey(
        "news_request.NewsUploadRequest",
        on_delete=models.SET_NULL,
        related_name="published_posts",
        blank=True,
        null=True,
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="news/images/", blank=True, null=True)
    author_name = models.CharField(max_length=100, blank=True)
    published_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_DRAFT,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="created_news_posts",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "news_posts"
        ordering = ["-published_at", "-created_at"]

    def __str__(self):
        return self.title


class GalleryCategory(TimeStampedModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        db_table = "gallery_categories"
        verbose_name = "Gallery Category"
        verbose_name_plural = "Gallery Categories"

    def __str__(self):
        return self.name


class GalleryImage(TimeStampedModel):
    STATUS_SHOW = "show"
    STATUS_HIDE = "hide"

    STATUS_CHOICES = [
        (STATUS_SHOW, "Show"),
        (STATUS_HIDE, "Hide"),
    ]

    category = models.ForeignKey(
        GalleryCategory,
        on_delete=models.SET_NULL,
        related_name="images",
        blank=True,
        null=True,
    )
    title = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to="gallery/images/")
    alt_text = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    sort_order = models.IntegerField(default=0)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_SHOW,
    )
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="uploaded_gallery_images",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "gallery_images"
        ordering = ["sort_order", "-created_at"]

    def __str__(self):
        return self.title or self.image.name