from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import redirect, render

from apps.content import selectors as content_selectors
from apps.core.pagination import paginate_queryset
from apps.organization import selectors as organization_selectors
from apps.registration import selectors as registration_selectors
from apps.website import selectors, services
from apps.website.forms import NavigationMenuForm, SiteSettingForm


MONTHS = ["JAN", "FEB", "MAR", "APR", "MEI", "JUN", "JUL", "AGU", "SEP", "OKT", "NOV", "DES"]


def _image_url(obj, field_name):
    if not obj:
        return ""
    image = getattr(obj, field_name, None)
    if not image:
        return ""
    try:
        return image.url
    except ValueError:
        return ""


def _detail_url(namespace, obj, fallback="#"):
    if not obj:
        return fallback
    slug = getattr(obj, "slug", "")
    if not slug:
        return fallback
    return reverse(f"{namespace}:detail", kwargs={"slug": slug})


def _phone_href(phone):
    if not phone:
        return ""
    digits = "".join(char for char in phone if char.isdigit())
    if digits.startswith("0"):
        digits = f"62{digits[1:]}"
    return f"+{digits}" if digits else ""


def _date_label(start_date, end_date=None, fallback=""):
    if not start_date:
        return fallback
    label = start_date.strftime("%d %b %Y")
    if end_date:
        label = f"{start_date.strftime('%d %b')}-{end_date.strftime('%d %b %Y')}"
    return label


def _month_label(value, fallback="NOV"):
    if not value:
        return fallback
    return MONTHS[value.month - 1]


def _public_cards(profile, management_members, programs, news_posts, events, gallery_images, registration_forms):
    management_cards = []
    for member in management_members:
        management_cards.append({
            "name": member.name,
            "position": member.position,
            "image_url": _image_url(member, "photo"),
        })

    program_cards = []
    for program in programs:
        program_cards.append({
            "title": program.title,
            "description": program.description,
            "icon": program.icon,
            "image_url": _image_url(program, "image"),
            "url": _detail_url("programs", program, "#program"),
        })

    news_cards = []
    for post in news_posts:
        category = getattr(post.category, "name", "")
        news_cards.append({
            "title": post.title,
            "excerpt": post.excerpt,
            "category": category.upper(),
            "date_label": _date_label(post.published_at),
            "image_url": _image_url(post, "image"),
            "url": _detail_url("news", post, "#berita"),
        })

    event_cards = []
    for event in events:
        start_date = event.start_date
        event_cards.append({
            "title": event.title,
            "description": event.description,
            "location": event.location,
            "date_label": _date_label(start_date, event.end_date),
            "day": start_date.strftime("%d") if start_date else "",
            "month": _month_label(start_date, ""),
            "image_url": _image_url(event, "image"),
            "url": _detail_url("events", event, "#agenda"),
        })

    gallery_cards = []
    for image in gallery_images:
        gallery_cards.append({
            "image_url": _image_url(image, "image"),
            "alt": image.alt_text or image.title,
        })

    profile_image_url = _image_url(profile, "profile_image")
    hero_image_url = profile_image_url or (gallery_cards[0]["image_url"] if gallery_cards else "")

    primary_registration = registration_forms[0] if registration_forms else None

    return {
        "site_name": profile.short_name or profile.name if profile else "",
        "logo_url": _image_url(profile, "logo"),
        "contact_phone_href": _phone_href(profile.phone if profile else ""),
        "hero_image_url": hero_image_url,
        "profile_image_url": profile_image_url,
        "management_cards": management_cards,
        "program_cards": program_cards,
        "news_cards": news_cards,
        "event_main": event_cards[0] if event_cards else {},
        "event_timeline": event_cards[1:],
        "gallery_cards": gallery_cards,
        "organization_age": timezone.now().year - profile.founded_year if profile and profile.founded_year else "",
        "primary_registration": primary_registration,
    }


def _public_context():
    profile = organization_selectors.organization_profile()
    management_members = list(organization_selectors.active_management_members()[:6])
    programs = list(content_selectors.featured_programs(limit=6))
    news_posts = list(content_selectors.latest_news(limit=6))
    events = list(content_selectors.upcoming_events(limit=6))
    gallery_images = list(content_selectors.visible_gallery_images()[:8])
    registration_forms = list(registration_selectors.active_registration_forms()[:5])

    return {
        "settings": selectors.site_settings_map(),
        "profile": profile,
        "management_members": management_members,
        "chairmen": organization_selectors.visible_chairmen()[:6],
        "programs": programs,
        "news_posts": news_posts,
        "events": events,
        "gallery_images": gallery_images,
        "registration_forms": registration_forms,
        **_public_cards(profile, management_members, programs, news_posts, events, gallery_images, registration_forms),
    }


def home_view(request):
    return render(request, "public/index.html")


def desktop_view(request):
    return render(request, "public/desktop.html", _public_context())


def mobile_view(request):
    return render(request, "public/mobile.html", _public_context())


@login_required
def setting_list_view(request):
    page = paginate_queryset(request, selectors.site_setting_list())
    return render(request, "admin/website/setting_list.html", {"settings": page})


@login_required
def setting_create_view(request):
    form = SiteSettingForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form)
        messages.success(request, "Setting berhasil disimpan.")
        return redirect("website:setting_list")
    return render(request, "admin/form.html", {"form": form, "title": "Tambah Setting"})


@login_required
def setting_update_view(request, setting_id):
    setting = selectors.site_setting_get(setting_id)
    form = SiteSettingForm(request.POST or None, instance=setting)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form)
        messages.success(request, "Setting berhasil diperbarui.")
        return redirect("website:setting_list")
    return render(request, "admin/form.html", {"form": form, "title": "Edit Setting"})


@login_required
def menu_list_view(request):
    page = paginate_queryset(request, selectors.navigation_list())
    return render(request, "admin/website/menu_list.html", {"menus": page})


@login_required
def menu_create_view(request):
    form = NavigationMenuForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form)
        messages.success(request, "Menu berhasil disimpan.")
        return redirect("website:menu_list")
    return render(request, "admin/form.html", {"form": form, "title": "Tambah Menu"})


@login_required
def menu_update_view(request, menu_id):
    menu = selectors.navigation_get(menu_id)
    form = NavigationMenuForm(request.POST or None, instance=menu)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form)
        messages.success(request, "Menu berhasil diperbarui.")
        return redirect("website:menu_list")
    return render(request, "admin/form.html", {"form": form, "title": "Edit Menu"})
