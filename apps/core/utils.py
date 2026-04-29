from django.utils.text import slugify


def generate_unique_slug(model_class, value, slug_field="slug"):
    base_slug = slugify(value) or "item"
    slug = base_slug
    counter = 1

    while model_class.objects.filter(**{slug_field: slug}).exists():
        counter += 1
        slug = f"{base_slug}-{counter}"

    return slug
