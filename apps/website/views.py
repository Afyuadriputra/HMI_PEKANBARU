from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect, render

from apps.content import selectors as content_selectors
from apps.core.pagination import paginate_queryset
from apps.organization import selectors as organization_selectors
from apps.registration import selectors as registration_selectors
from apps.website import selectors, services
from apps.website.forms import NavigationMenuForm, SiteSettingForm


STATIC_IMAGES = {
    "logo": "https://hmipemkabriau.com/img/logohmi.png",
    "hero": "https://www.indonesia-tourism.com/french/riau/images/gallery/pekanbaru-city-riau-2.jpg",
    "profile": "https://lh3.googleusercontent.com/aida-public/AB6AXuAmljfKHK-fB65Qz-aJnm27NxlM_HYlqKVlIv6dnM6AwS30aPW1CwzQZ0WJwxwNXfllefcVOMmDXy0MlkmKnmtYVGV2_FdSEI-Ci_P56ibgYeOFErA8Z-OJTkjoqi9mitJHkLCcD56E3rDeqGao2ftRF-g7UzTszoW7ThvegFJU1Ne4AijvtDC3LDyfuEU-6r1z_JCd-FwqJBn-IdwL5U_mm3ieZvKcG-dMzjaqJFjE37vLfekybkaAIgsfBnkX2JJsXmveTH0m6Grh",
    "management": [
        "https://lh3.googleusercontent.com/aida-public/AB6AXuBhZKsW-ZsJAhjOyU_k1unm8yYLMTT2HlMpdzopRxfg8TUMZnCzOclc0fGrb3eCxpCNbBDw-QQ1eTq6n57HF34_pze1l6RG-10_VJjlTmcifgbtMwVO-RFs_BCtP1F7C4bmx_BcywawdQd-eFQS2vYallyekO5_TwQOQGYlH036cw6ztOEkxrGDXYtty_IqISiQqfMjnhjZt-DKjqAoYJ9yDkgzgX5RKXG2jfOkJNZeV7-zyGATv0X-U4G9y6_9md24bLfkpIfWB0R-",
        "https://lh3.googleusercontent.com/aida-public/AB6AXuDLoLP83TgdKnanj8XM-M2zpsEBjDpK3BNZ0etxN3wo6F_-FLaizkDk3tEijBvuW5X4fyL4IuhWJ7kHnnD2bKPV0-AWx2KCnKqjRh64g2I0nSyTDrTmvWhsyR6TF9EoZefJjaehpc7MiduRZSRD1vQhRcCtiGOaZnpyUGjHgDYVW0YWQIZwjj0lWY8lGjxrW7lGmHJeKOcgQVv6vEHdfAgYliPb3oKXLHUJN1dkYPsNA4_d2aM8lccvfMi_3oOd4nUFYN7psj0KUPvl",
        "https://lh3.googleusercontent.com/aida-public/AB6AXuB7du5ZZF0p5NlYHtBxoX8GsjlT_XwPx9UimKMq5W8l6DHC1DbhslPqrpkUz-4Yq1qMk6XNcxCpTX1R8WZAaHM3UocUvah0h8XDBJX0FC2f1oug_vIi6800nV8FAZa9bUCpNoi8RQ7D_npuDxx8ugFkMSIpGkGQcaG9ZN05KgOpcm2JBxmIYXeK-HfmMDWNt9Wt4-kN_Di9po_dF7iJ7BeY4W8Iu2DCB9jkjBAEBn6PIyDnMenEkvkSBNuCdv1lA-oZ04tpM7NKcmT0",
    ],
    "program": "https://lh3.googleusercontent.com/aida-public/AB6AXuBMLIR6zglLqXdEfuPbdqUFWl4ORkyOmf95rMhMPUxUrUUTt-LhmD3Lisk9l7pkVNKZk-5PBnvh4FB0go1RHZ154XjucqtiSg0zor21Aqh2DuroprWh-d8DuLd5VhMDTu_xb4MrRc2T4lE9lec6yIZbEAG_yYgse5wUmCgeItcCYteMZ_ueYnGEsmVV6nrFzyvKHdu4NiiTN302VqtjeZHBdunVhGdUAIg9x467EAaVVpUJ2Rt6p1hA1vod9Q9rcVVzMIpVOzR1AUFH",
    "news": [
        "https://lh3.googleusercontent.com/aida-public/AB6AXuBfXDWUepq-HDpzCsWqOXgREaiIElQo4Dcyz479ZoD42emvO3MPQ6H3Cu1bVFhFZVptu58UmGNsmxsqtJmiFLsOFkfUyXwMnQ84bT3CHhs_s8fKYdVYVELNoB_qPx17dSu-N5bNpzFhUTRaDcPiPTAwdzNpy8FS12Z_hl0bVjmb3G5pqXwp1MHl1lC6asXqrAXfTVCvtgQUJY9idAnccO3absNUIUr2X3Akd7hMklvVODyWXn8abBs5t-MoowyxMKy5iUp8L1kYMvFw",
        "https://lh3.googleusercontent.com/aida-public/AB6AXuA_3Q2_wk6RQxgfbqVk7DrzRS64NScwQ3vd69ZHxCNZYFy_67a7LM5h5B7Mbyd86Y1QVVxjpjWAKDGNwTIz0PC2SmV6J_16d4u2kDX_c6geVcDVO5SSGJvJEPkZDvEdDVHIxWTd1aT7F2Zl9ZtrpDP7D4p5Yzn02et9VpiS3LK7Lf_oCkyHBCXO_ezkcPs6OZsC6EDIF2aRSCNrwtb99nyz83Q7xQ9QK_9ZwWTdmtQ8sPx4pFT46e9DM3rt348RcCYUsRSRxpnFslPx",
        "https://lh3.googleusercontent.com/aida-public/AB6AXuAIo5vgE2yZsZYWHk7xEbXyzdrKhb27wPGbFg_dY85T8iar49kcvLHdd1nu1L-XVG_Nv8OrPWwQDk2m-dm5SkbyRsJgCw-4ZGAuwGX4EFbdslRqroNeHJJmx7aQwV-EQiYLU7BSpfzUJmxxhWsPJD0RNhRkcTW4LZq3m_cQV01HlQHVFidGaDP7HlPFp0E6WD5o56QkmCMGMR45dZwlmXWsCXtKXn47xtsVCU3RKpXVvSUYYkUh_txcNc4Jv-616UO9eQaAaMTHKWp6",
    ],
    "event": "https://lh3.googleusercontent.com/aida-public/AB6AXuDvKUDGMUEXPR_FJNk_oylibzyw_fzEaeDO6P-SmSzvjbxNTDQ1QqwAYMJPXdhBCY3fHNnzkAAlga_wv5d1_KQwTgFdd1e7eiptvRsPUAtQ72vZihgRNugrycsTZWy-F9KXKX_LT7xION94U9Oz7ol6ihEVHP6WWM4KNm_AJ9FzDNHtu6V2QOWXDFvbYxJHtV6MNWKfnh8_WeegKyzCxYlNhBeAW6B2kvfhP51J5FzN1nlV0YmBYuaPqkqBACpCOymGicqTxETwFgyV",
    "gallery": [
        "https://lh3.googleusercontent.com/aida-public/AB6AXuDwXK1kMnT1GzzJr016cwDYPTG96Y4VPcma7LtHqhEjmfdU7dOShTzrv_T1qCQfIys8kZJEMgG8eUctCLg1aRLGhpvHB_BdTHwNZ3e9wY17QlylpXhPoYRVUj7_3dVVwpOiuweFph5hpZ7_f9rs3FBkJfi5dJSFCntUH4Yitky_64-E06GwAXX__lFkcD4lDS7Io30LNvEd2frx2QO0kcyo5NehoO4ODLcFXMxOa5PdC2SH6vFwRK4gGYfWgPMWU_-h_Pv5agtW5pw2",
        "https://lh3.googleusercontent.com/aida-public/AB6AXuBhQg4RgIQ8kIFUMMGsOSFhZCL7D0dTtioOPtooMe-Qhe7jDqBOZD_JgJrreBF7fZ7vySY02v5RlkvWd1kbOcxnYVe5T4Q29vcXMPmOb9cj0u8NIA498hF6VofVxwm5u3dyLc_jnO-NJpIE1b2SiUSpsPDFU8ZBI7Wu1E--4PC3s8aGhM0pS9ibSBFbn0oC5UQx9T2vqdufolPNd44CI17yYE-_4OsGwZe5R410HKZcfjzmg_8Xk_wczJS06EKCDABzBP0sAnUIn8Eb",
        "https://lh3.googleusercontent.com/aida-public/AB6AXuDEzqPcUE5o01Ga70KFi8P1qDAYshvnPjsaTelOlA_Q2OiJGLYPAXwriPXR8a2wNa_Uhqlj_v8eDl2AoOa6Ne9R-iwE54Mj7ablfVyx_G-C8dZv3k-cZYjPHMuojZcB-IfYdbm0r0oPDVZ6DHojvGkJnYtiyGrst_rk8rhqOG1NFjXPdQNDqa1gOFaFlDxm05gkaU6ZLnUvwQPLj7X2y_GraxY36XFGTlgOGGovNxcEBnHhcOy2V5IDX-eEGgtfHZDbL01Mh3-pFO4_",
        "https://lh3.googleusercontent.com/aida-public/AB6AXuAz9B6Zfu1fKGEJzQnYNdJICC_9z4ZIJYptWfFcUjzp3lM1nWnjc2IY_E0UwCboVZWXE-4eLw6zgCobp8HIe4aL1822uZ0NbEafsBTi5LHJ86rxvAe3WeiTVy2YX4lUUvPtk795h_uUF6VIRldkW9g1n_qRx0-IKDqw7O8Xaj6C-6uwiJUG9IatiSaUMpr17KqbVw8YDt_uNlhxKcIrA4TbDZ-WvOtc073VOcZqTO4BGx2IRGNctYBPzdfguzFbiwskoZFaTwUURVWm",
    ],
}


MONTHS = ["JAN", "FEB", "MAR", "APR", "MEI", "JUN", "JUL", "AGU", "SEP", "OKT", "NOV", "DES"]


def _image_url(obj, field_name, fallback):
    if not obj:
        return fallback
    image = getattr(obj, field_name, None)
    if not image:
        return fallback
    try:
        return image.url
    except ValueError:
        return fallback


def _detail_url(namespace, obj, fallback="#"):
    if not obj:
        return fallback
    slug = getattr(obj, "slug", "")
    if not slug:
        return fallback
    return reverse(f"{namespace}:detail", kwargs={"slug": slug})


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


def _first_or_none(items, index):
    return items[index] if len(items) > index else None


def _public_cards(profile, management_members, programs, news_posts, events, gallery_images):
    management_defaults = [
        ("Ahmad Fauzi", "Ketua Umum"),
        ("Rizky Ramadhan", "Sekretaris Umum"),
        ("Dedi Kurniawan", "Bendahara Umum"),
    ]
    program_defaults = [
        ("Perkaderan Latihan Kader I", "Gerbang utama pembinaan karakter dan ideologi mahasiswa Islam untuk menjadi kader berkualitas.", "menu_book"),
        ("Kajian Intelektual", "Diskusi rutin mingguan membedah isu kontemporer.", "menu_book"),
        ("HMI Mengabdi", "Program aksi sosial dan pemberdayaan masyarakat.", "volunteer_activism"),
        ("Advokasi Kampus", "Pendampingan aspirasi mahasiswa di lingkungan kampus.", "public"),
        ("Penerbitan Jurnal", "Publikasi karya ilmiah dan opini kader HMI.", "edit_note"),
    ]
    news_defaults = [
        ("Pelantikan Pengurus Baru HMI Pekanbaru", "Himpunan Mahasiswa Islam Cabang Pekanbaru resmi melantik jajaran pengurus baru untuk masa khidmat satu tahun ke depan.", "BERITA", "24 Okt 2023"),
        ("Digitalisasi Dakwah: Tantangan Kader di Era Modern", "Menghadapi pesatnya arus informasi, kader HMI dituntut untuk cakap dalam memanfaatkan teknologi sebagai medium perjuangan.", "OPINI", "12 Okt 2023"),
        ("Seminar Nasional: Peran Pemuda dalam Pemilu", "Seminar yang menghadirkan tokoh nasional ini bertujuan membekali mahasiswa dengan pemahaman politik yang sehat dan inklusif.", "KEGIATAN", "05 Okt 2023"),
    ]
    event_defaults = [
        ("Intermediate Training (LK II) Nasional", "Pekanbaru akan menjadi tuan rumah pelatihan kepemimpinan tingkat menengah yang diikuti utusan cabang se-Indonesia.", "Hotel Grand Elite", "15-22 Des 2023", "15", "DES"),
        ("Diskusi Pahlawan", "", "Sekretariat HMI Pekanbaru", "", "10", "NOV"),
        ("Latihan Kader 1 (LK1)", "", "Wisma Haji Riau", "", "18", "NOV"),
        ("Malam Keakraban", "", "Ballroom Pangeran Hotel", "", "02", "DES"),
    ]

    management_cards = []
    for index, defaults in enumerate(management_defaults):
        member = _first_or_none(management_members, index)
        management_cards.append({
            "name": getattr(member, "name", "") or defaults[0],
            "position": getattr(member, "position", "") or defaults[1],
            "image_url": _image_url(member, "photo", STATIC_IMAGES["management"][index]),
        })

    program_cards = []
    for index, defaults in enumerate(program_defaults):
        program = _first_or_none(programs, index)
        program_cards.append({
            "title": getattr(program, "title", "") or defaults[0],
            "description": getattr(program, "description", "") or defaults[1],
            "icon": getattr(program, "icon", "") or defaults[2],
            "image_url": _image_url(program, "image", STATIC_IMAGES["program"]),
            "url": _detail_url("programs", program, "#program"),
        })

    news_cards = []
    for index, defaults in enumerate(news_defaults):
        post = _first_or_none(news_posts, index)
        category = getattr(getattr(post, "category", None), "name", "") or defaults[2]
        news_cards.append({
            "title": getattr(post, "title", "") or defaults[0],
            "excerpt": getattr(post, "excerpt", "") or defaults[1],
            "category": category.upper(),
            "date_label": _date_label(getattr(post, "published_at", None), fallback=defaults[3]),
            "image_url": _image_url(post, "image", STATIC_IMAGES["news"][index]),
            "url": _detail_url("news", post, "#berita"),
        })

    event_cards = []
    for index, defaults in enumerate(event_defaults):
        event = _first_or_none(events, index)
        start_date = getattr(event, "start_date", None)
        event_cards.append({
            "title": getattr(event, "title", "") or defaults[0],
            "description": getattr(event, "description", "") or defaults[1],
            "location": getattr(event, "location", "") or defaults[2],
            "date_label": _date_label(start_date, getattr(event, "end_date", None), defaults[3]),
            "day": start_date.strftime("%d") if start_date else defaults[4],
            "month": _month_label(start_date, defaults[5]),
            "image_url": _image_url(event, "image", STATIC_IMAGES["event"]),
            "url": _detail_url("events", event, "#agenda"),
        })

    gallery_cards = []
    for index, fallback in enumerate(STATIC_IMAGES["gallery"]):
        image = _first_or_none(gallery_images, index)
        gallery_cards.append({
            "image_url": _image_url(image, "image", fallback),
            "alt": getattr(image, "alt_text", "") or getattr(image, "title", "") or f"Galeri {index + 1}",
        })

    return {
        "logo_url": _image_url(profile, "logo", STATIC_IMAGES["logo"]),
        "hero_image_url": STATIC_IMAGES["hero"],
        "profile_image_url": _image_url(profile, "profile_image", STATIC_IMAGES["profile"]),
        "management_cards": management_cards,
        "program_cards": program_cards,
        "news_cards": news_cards,
        "event_main": event_cards[0],
        "event_timeline": event_cards[1:],
        "gallery_cards": gallery_cards,
    }


def _public_context():
    profile = organization_selectors.organization_profile()
    management_members = list(organization_selectors.active_management_members()[:6])
    programs = list(content_selectors.featured_programs(limit=6))
    news_posts = list(content_selectors.latest_news(limit=6))
    events = list(content_selectors.upcoming_events(limit=6))
    gallery_images = list(content_selectors.visible_gallery_images()[:8])

    return {
        "settings": selectors.site_settings_map(),
        "profile": profile,
        "management_members": management_members,
        "chairmen": organization_selectors.visible_chairmen()[:6],
        "programs": programs,
        "news_posts": news_posts,
        "events": events,
        "gallery_images": gallery_images,
        "registration_forms": registration_selectors.active_registration_forms()[:5],
        **_public_cards(profile, management_members, programs, news_posts, events, gallery_images),
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
