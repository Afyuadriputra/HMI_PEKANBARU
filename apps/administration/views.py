from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from apps.administration import selectors, services
from apps.administration.forms import DocumentArchiveForm, IncomingLetterForm, InvitationForm, OutgoingLetterForm
from apps.core.pagination import paginate_queryset


def _list_response(request, queryset, title, create_url, update_url):
    return render(request, "admin/administration/generic_list.html", {"items": paginate_queryset(request, queryset), "title": title, "create_url": create_url, "update_url": update_url})


@login_required
def archive_list_view(request):
    return _list_response(request, selectors.archive_list(), "Arsip Dokumen", "administration:archive_create", "administration:archive_update")


@login_required
def archive_create_view(request):
    form = DocumentArchiveForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form, request.user)
        messages.success(request, "Arsip berhasil disimpan.")
        return redirect("administration:archive_list")
    return render(request, "admin/form.html", {"form": form, "title": "Tambah Arsip"})


@login_required
def archive_update_view(request, item_id):
    form = DocumentArchiveForm(request.POST or None, request.FILES or None, instance=selectors.archive_get(item_id))
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form, request.user)
        messages.success(request, "Arsip berhasil diperbarui.")
        return redirect("administration:archive_list")
    return render(request, "admin/form.html", {"form": form, "title": "Edit Arsip"})


@login_required
def incoming_list_view(request):
    return _list_response(request, selectors.incoming_letter_list(), "Surat Masuk", "administration:incoming_create", "administration:incoming_update")


@login_required
def incoming_create_view(request):
    form = IncomingLetterForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form, request.user)
        messages.success(request, "Surat masuk berhasil disimpan.")
        return redirect("administration:incoming_list")
    return render(request, "admin/form.html", {"form": form, "title": "Tambah Surat Masuk"})


@login_required
def incoming_update_view(request, item_id):
    form = IncomingLetterForm(request.POST or None, request.FILES or None, instance=selectors.incoming_letter_get(item_id))
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form, request.user)
        messages.success(request, "Surat masuk berhasil diperbarui.")
        return redirect("administration:incoming_list")
    return render(request, "admin/form.html", {"form": form, "title": "Edit Surat Masuk"})


@login_required
def outgoing_list_view(request):
    return _list_response(request, selectors.outgoing_letter_list(), "Surat Keluar", "administration:outgoing_create", "administration:outgoing_update")


@login_required
def outgoing_create_view(request):
    form = OutgoingLetterForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form, request.user)
        messages.success(request, "Surat keluar berhasil disimpan.")
        return redirect("administration:outgoing_list")
    return render(request, "admin/form.html", {"form": form, "title": "Tambah Surat Keluar"})


@login_required
def outgoing_update_view(request, item_id):
    form = OutgoingLetterForm(request.POST or None, request.FILES or None, instance=selectors.outgoing_letter_get(item_id))
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form, request.user)
        messages.success(request, "Surat keluar berhasil diperbarui.")
        return redirect("administration:outgoing_list")
    return render(request, "admin/form.html", {"form": form, "title": "Edit Surat Keluar"})


@login_required
def invitation_list_view(request):
    return _list_response(request, selectors.invitation_list(), "Undangan", "administration:invitation_create", "administration:invitation_update")


@login_required
def invitation_create_view(request):
    form = InvitationForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form, request.user)
        messages.success(request, "Undangan berhasil disimpan.")
        return redirect("administration:invitation_list")
    return render(request, "admin/form.html", {"form": form, "title": "Tambah Undangan"})


@login_required
def invitation_update_view(request, item_id):
    form = InvitationForm(request.POST or None, request.FILES or None, instance=selectors.invitation_get(item_id))
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form, request.user)
        messages.success(request, "Undangan berhasil diperbarui.")
        return redirect("administration:invitation_list")
    return render(request, "admin/form.html", {"form": form, "title": "Edit Undangan"})
