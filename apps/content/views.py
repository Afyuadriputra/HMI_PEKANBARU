from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from apps.content import selectors, services
from apps.content.forms import EventForm, GalleryImageForm, NewsPostForm, ProgramForm
from apps.core.pagination import paginate_queryset


def news_list_view(request):
    page = paginate_queryset(request, selectors.published_news(), per_page=9)
    return render(request, "public/content/news_list.html", {"news_posts": page})


def news_detail_view(request, slug):
    return render(request, "public/content/news_detail.html", {"post": selectors.news_get_by_slug(slug)})


def program_list_view(request):
    return render(request, "public/content/program_list.html", {"programs": selectors.published_programs()})


def program_detail_view(request, slug):
    return render(request, "public/content/program_detail.html", {"program": selectors.program_get_by_slug(slug)})


def event_list_view(request):
    page = paginate_queryset(request, selectors.published_events(), per_page=9)
    return render(request, "public/content/event_list.html", {"events": page})


def event_detail_view(request, slug):
    return render(request, "public/content/event_detail.html", {"event": selectors.event_get_by_slug(slug)})


def gallery_list_view(request):
    page = paginate_queryset(request, selectors.visible_gallery_images(), per_page=12)
    return render(request, "public/content/gallery_list.html", {"images": page})


@login_required
def program_admin_list_view(request):
    page = paginate_queryset(request, selectors.program_list_admin())
    return render(request, "admin/content/program_list.html", {"programs": page})


@login_required
def program_create_view(request):
    form = ProgramForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        services.save_program_form(form, request.user)
        messages.success(request, "Program berhasil disimpan.")
        return redirect("programs:admin_list")
    return render(request, "admin/form.html", {"form": form, "title": "Tambah Program"})


@login_required
def program_update_view(request, program_id):
    program = selectors.program_get(program_id)
    form = ProgramForm(request.POST or None, request.FILES or None, instance=program)
    if request.method == "POST" and form.is_valid():
        services.save_program_form(form, request.user)
        messages.success(request, "Program berhasil diperbarui.")
        return redirect("programs:admin_list")
    return render(request, "admin/form.html", {"form": form, "title": "Edit Program"})


@login_required
def event_admin_list_view(request):
    page = paginate_queryset(request, selectors.event_list_admin())
    return render(request, "admin/content/event_list.html", {"events": page})


@login_required
def event_create_view(request):
    form = EventForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        services.save_event_form(form, request.user)
        messages.success(request, "Agenda berhasil disimpan.")
        return redirect("events:admin_list")
    return render(request, "admin/form.html", {"form": form, "title": "Tambah Agenda"})


@login_required
def event_update_view(request, event_id):
    event = selectors.event_get(event_id)
    form = EventForm(request.POST or None, request.FILES or None, instance=event)
    if request.method == "POST" and form.is_valid():
        services.save_event_form(form, request.user)
        messages.success(request, "Agenda berhasil diperbarui.")
        return redirect("events:admin_list")
    return render(request, "admin/form.html", {"form": form, "title": "Edit Agenda"})


@login_required
def news_admin_list_view(request):
    page = paginate_queryset(request, selectors.news_list_admin())
    return render(request, "admin/content/news_list.html", {"news_posts": page})


@login_required
def news_create_view(request):
    form = NewsPostForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        services.save_news_form(form, request.user)
        messages.success(request, "Berita berhasil disimpan.")
        return redirect("news:admin_list")
    return render(request, "admin/form.html", {"form": form, "title": "Tambah Berita"})


@login_required
def news_update_view(request, news_id):
    post = selectors.news_get(news_id)
    form = NewsPostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == "POST" and form.is_valid():
        services.save_news_form(form, request.user)
        messages.success(request, "Berita berhasil diperbarui.")
        return redirect("news:admin_list")
    return render(request, "admin/form.html", {"form": form, "title": "Edit Berita"})


@login_required
def gallery_admin_list_view(request):
    page = paginate_queryset(request, selectors.gallery_list_admin())
    return render(request, "admin/content/gallery_list.html", {"images": page})


@login_required
def gallery_create_view(request):
    form = GalleryImageForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        services.save_gallery_image_form(form, request.user)
        messages.success(request, "Gambar galeri berhasil disimpan.")
        return redirect("gallery:admin_list")
    return render(request, "admin/form.html", {"form": form, "title": "Tambah Galeri"})


@login_required
def gallery_update_view(request, image_id):
    image = selectors.gallery_image_get(image_id)
    form = GalleryImageForm(request.POST or None, request.FILES or None, instance=image)
    if request.method == "POST" and form.is_valid():
        services.save_gallery_image_form(form, request.user)
        messages.success(request, "Gambar galeri berhasil diperbarui.")
        return redirect("gallery:admin_list")
    return render(request, "admin/form.html", {"form": form, "title": "Edit Galeri"})
