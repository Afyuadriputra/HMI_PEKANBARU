from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from apps.core.pagination import paginate_queryset
from apps.training import selectors, services
from apps.training.forms import LkBatchForm, LkCertificateForm, LkLevelForm, LkMaterialForm, LkParticipantForm


@login_required
def level_list_view(request):
    return render(request, "admin/training/generic_list.html", {"items": paginate_queryset(request, selectors.lk_level_list()), "title": "Level LK", "create_url": "training:level_create", "update_url": "training:level_update"})


@login_required
def level_create_view(request):
    form = LkLevelForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form)
        messages.success(request, "Level LK berhasil disimpan.")
        return redirect("training:level_list")
    return render(request, "admin/form.html", {"form": form, "title": "Tambah Level LK"})


@login_required
def level_update_view(request, item_id):
    form = LkLevelForm(request.POST or None, instance=selectors.lk_level_get(item_id))
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form)
        messages.success(request, "Level LK berhasil diperbarui.")
        return redirect("training:level_list")
    return render(request, "admin/form.html", {"form": form, "title": "Edit Level LK"})


@login_required
def batch_list_view(request):
    return render(request, "admin/training/generic_list.html", {"items": paginate_queryset(request, selectors.lk_batch_list()), "title": "Batch LK", "create_url": "training:batch_create", "update_url": "training:batch_update"})


@login_required
def batch_create_view(request):
    form = LkBatchForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form, request.user)
        messages.success(request, "Batch LK berhasil disimpan.")
        return redirect("training:batch_list")
    return render(request, "admin/form.html", {"form": form, "title": "Tambah Batch LK"})


@login_required
def batch_update_view(request, item_id):
    form = LkBatchForm(request.POST or None, instance=selectors.lk_batch_get(item_id))
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form, request.user)
        messages.success(request, "Batch LK berhasil diperbarui.")
        return redirect("training:batch_list")
    return render(request, "admin/form.html", {"form": form, "title": "Edit Batch LK"})


@login_required
def participant_list_view(request):
    return render(request, "admin/training/generic_list.html", {"items": paginate_queryset(request, selectors.participant_list()), "title": "Peserta LK", "create_url": "training:participant_create", "update_url": "training:participant_update"})


@login_required
def participant_create_view(request):
    form = LkParticipantForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form)
        messages.success(request, "Peserta LK berhasil disimpan.")
        return redirect("training:participant_list")
    return render(request, "admin/form.html", {"form": form, "title": "Tambah Peserta LK"})


@login_required
def participant_update_view(request, item_id):
    form = LkParticipantForm(request.POST or None, request.FILES or None, instance=selectors.participant_get(item_id))
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form)
        messages.success(request, "Peserta LK berhasil diperbarui.")
        return redirect("training:participant_list")
    return render(request, "admin/form.html", {"form": form, "title": "Edit Peserta LK"})


@login_required
def material_list_view(request):
    return render(request, "admin/training/generic_list.html", {"items": paginate_queryset(request, selectors.material_list()), "title": "Materi LK", "create_url": "training:material_create", "update_url": "training:material_update"})


@login_required
def material_create_view(request):
    form = LkMaterialForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form)
        messages.success(request, "Materi LK berhasil disimpan.")
        return redirect("training:material_list")
    return render(request, "admin/form.html", {"form": form, "title": "Tambah Materi LK"})


@login_required
def material_update_view(request, item_id):
    form = LkMaterialForm(request.POST or None, instance=selectors.material_get(item_id))
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form)
        messages.success(request, "Materi LK berhasil diperbarui.")
        return redirect("training:material_list")
    return render(request, "admin/form.html", {"form": form, "title": "Edit Materi LK"})


@login_required
def certificate_list_view(request):
    return render(request, "admin/training/generic_list.html", {"items": paginate_queryset(request, selectors.certificate_list()), "title": "Sertifikat LK", "create_url": "training:certificate_create", "update_url": "training:certificate_update"})


@login_required
def certificate_create_view(request):
    form = LkCertificateForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        services.upload_lk_certificate(form)
        messages.success(request, "Sertifikat berhasil di-upload.")
        return redirect("training:certificate_list")
    return render(request, "admin/form.html", {"form": form, "title": "Upload Sertifikat LK"})


@login_required
def certificate_update_view(request, item_id):
    form = LkCertificateForm(request.POST or None, request.FILES or None, instance=selectors.certificate_get(item_id))
    if request.method == "POST" and form.is_valid():
        services.upload_lk_certificate(form)
        messages.success(request, "Sertifikat berhasil diperbarui.")
        return redirect("training:certificate_list")
    return render(request, "admin/form.html", {"form": form, "title": "Edit Sertifikat LK"})
