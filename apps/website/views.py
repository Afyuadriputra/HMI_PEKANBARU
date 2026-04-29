from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone

from apps.content import selectors as content_selectors
from apps.core.pagination import paginate_queryset
from apps.organization import selectors as organization_selectors
from apps.registration import selectors as registration_selectors
from apps.website import selectors, services
from apps.website.forms import NavigationMenuForm, SiteSettingForm


MONTHS = [
    "JAN",
    "FEB",
    "MAR",
    "APR",
    "MEI",
    "JUN",
    "JUL",
    "AGU",
    "SEP",
    "OKT",
    "NOV",
    "DES",
]


def _image_url(obj, field_name):
    if not obj:
        return ""

    image = getattr(obj, field_name, None)
    if not image:
        return ""

    try:
        return image.url
    except (ValueError, AttributeError):
        return ""


def _detail_url(namespace, obj, fallback="#"):
    """
    Return URL detail object berdasarkan slug.
    Kalau object/slug tidak ada, fallback ke anchor supaya template tidak error.
    """
    if not obj:
        return fallback

    slug = getattr(obj, "slug", "")
    if not slug:
        return fallback

    try:
        return reverse(f"{namespace}:detail", kwargs={"slug": slug})
    except Exception:
        return fallback


def _phone_href(phone):
    if not phone:
        return ""

    digits = "".join(char for char in str(phone) if char.isdigit())

    if digits.startswith("0"):
        digits = f"62{digits[1:]}"

    if not digits:
        return ""

    return f"+{digits}"


def _date_label(start_date, end_date=None, fallback=""):
    if not start_date:
        return fallback

    if end_date and end_date != start_date:
        return f"{start_date.strftime('%d %b')} - {end_date.strftime('%d %b %Y')}"

    return start_date.strftime("%d %b %Y")


def _month_label(value, fallback=""):
    if not value:
        return fallback

    return MONTHS[value.month - 1]


def _safe_text(value, fallback=""):
    return value or fallback


def _public_cards(
    profile,
    management_members,
    programs,
    news_posts,
    events,
    gallery_images,
    registration_forms,
):
    management_cards = []
    for member in management_members:
        management_cards.append(
            {
                "name": _safe_text(getattr(member, "name", "")),
                "position": _safe_text(getattr(member, "position", "")),
                "image_url": _image_url(member, "photo"),
            }
        )

    program_cards = []
    for program in programs:
        program_cards.append(
            {
                "title": _safe_text(getattr(program, "title", "")),
                "description": _safe_text(getattr(program, "description", "")),
                "icon": _safe_text(getattr(program, "icon", ""), "menu_book"),
                "image_url": _image_url(program, "image"),
                "url": _detail_url("programs", program, "#program"),
            }
        )

    news_cards = []
    for post in news_posts:
        category = getattr(getattr(post, "category", None), "name", "")

        news_cards.append(
            {
                "title": _safe_text(getattr(post, "title", "")),
                "excerpt": _safe_text(getattr(post, "excerpt", "")),
                "category": category.upper() if category else "BERITA",
                "date_label": _date_label(getattr(post, "published_at", None)),
                "image_url": _image_url(post, "image"),
                "url": _detail_url("news", post, "#berita"),
            }
        )

    event_cards = []
    for event in events:
        start_date = getattr(event, "start_date", None)
        end_date = getattr(event, "end_date", None)

        event_cards.append(
            {
                "title": _safe_text(getattr(event, "title", "")),
                "description": _safe_text(getattr(event, "description", "")),
                "location": _safe_text(getattr(event, "location", "")),
                "date_label": _date_label(start_date, end_date),
                "day": start_date.strftime("%d") if start_date else "",
                "month": _month_label(start_date),
                "image_url": _image_url(event, "image"),
                "url": _detail_url("events", event, "#agenda"),
            }
        )

    gallery_cards = []
    for image in gallery_images:
        gallery_cards.append(
            {
                "image_url": _image_url(image, "image"),
                "alt": _safe_text(
                    getattr(image, "alt_text", ""),
                    getattr(image, "title", "Galeri HMI Pekanbaru"),
                ),
            }
        )

    profile_image_url = _image_url(profile, "profile_image")
    logo_url = _image_url(profile, "logo")

    hero_image_url = profile_image_url
    if not hero_image_url and gallery_cards:
        hero_image_url = gallery_cards[0].get("image_url", "")

    primary_registration = None
    if registration_forms:
        primary = registration_forms[0]
        primary_registration = {
            "title": _safe_text(getattr(primary, "title", "")),
            "description": _safe_text(getattr(primary, "description", "")),
            "google_form_url": _safe_text(getattr(primary, "google_form_url", "")),
        }

    if profile:
        profile_name = _safe_text(getattr(profile, "name", ""), "SI-HMI Pekanbaru")
        site_name = _safe_text(getattr(profile, "short_name", ""), profile_name)
        founded_year = getattr(profile, "founded_year", None)
    else:
        profile_name = "SI-HMI Pekanbaru"
        site_name = "SI-HMI Pekanbaru"
        founded_year = None

    organization_age = ""
    if founded_year:
        organization_age = timezone.now().year - founded_year

    return {
        "site_name": site_name,
        "logo_url": logo_url,
        "contact_phone_href": _phone_href(getattr(profile, "phone", "") if profile else ""),
        "hero_image_url": hero_image_url,
        "profile_image_url": profile_image_url,
        "management_cards": management_cards,
        "program_cards": program_cards,
        "news_cards": news_cards,
        "event_main": event_cards[0] if event_cards else None,
        "event_timeline": event_cards[1:4],
        "gallery_cards": gallery_cards,
        "organization_age": organization_age,
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
        **_public_cards(
            profile=profile,
            management_members=management_members,
            programs=programs,
            news_posts=news_posts,
            events=events,
            gallery_images=gallery_images,
            registration_forms=registration_forms,
        ),
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