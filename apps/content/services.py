from django.db import transaction
from django.utils import timezone

from apps.content.models import Event, GalleryCategory, GalleryImage, NewsCategory, NewsPost, Program
from apps.core.utils import generate_unique_slug


def _set_slug(instance, model_class):
    if not instance.slug:
        instance.slug = generate_unique_slug(model_class, instance.name if hasattr(instance, "name") else instance.title)


@transaction.atomic
def save_program_form(form, user=None):
    program = form.save(commit=False)
    _set_slug(program, Program)
    if user and not program.created_by_id:
        program.created_by = user
    program.save()
    form.save_m2m()
    return program


@transaction.atomic
def save_event_form(form, user=None):
    event = form.save(commit=False)
    _set_slug(event, Event)
    if user and not event.created_by_id:
        event.created_by = user
    event.save()
    form.save_m2m()
    return event


@transaction.atomic
def save_news_category_form(form):
    category = form.save(commit=False)
    _set_slug(category, NewsCategory)
    category.save()
    return category


@transaction.atomic
def save_news_form(form, user=None):
    post = form.save(commit=False)
    _set_slug(post, NewsPost)
    if post.status == NewsPost.STATUS_PUBLISHED and not post.published_at:
        post.published_at = timezone.now()
    if user and not post.created_by_id:
        post.created_by = user
    post.save()
    form.save_m2m()
    return post


@transaction.atomic
def save_gallery_category_form(form):
    category = form.save(commit=False)
    _set_slug(category, GalleryCategory)
    category.save()
    return category


@transaction.atomic
def save_gallery_image_form(form, user=None):
    image = form.save(commit=False)
    if user and not image.uploaded_by_id:
        image.uploaded_by = user
    image.save()
    form.save_m2m()
    return image


@transaction.atomic
def delete_instance(instance):
    instance.delete()
