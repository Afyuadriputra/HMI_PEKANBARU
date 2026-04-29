from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from apps.cadre import selectors, services
from apps.cadre.forms import AlumniForm, CadreForm, CadreLkHistoryForm, CommissariatForm
from apps.core.pagination import paginate_queryset


def _admin_list(request, queryset, template_name, context_name):
    page = paginate_queryset(request, queryset)
    return render(request, template_name, {context_name: page})


@login_required
def commissariat_list_view(request):
    return _admin_list(request, selectors.commissariat_list(), "admin/cadre/commissariat_list.html", "items")


@login_required
def commissariat_create_view(request):
    form = CommissariatForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form)
        messages.success(request, "Komisariat berhasil disimpan.")
        return redirect("cadre:commissariat_list")
    return render(request, "admin/form.html", {"form": form, "title": "Tambah Komisariat"})


@login_required
def commissariat_update_view(request, item_id):
    item = selectors.commissariat_get(item_id)
    form = CommissariatForm(request.POST or None, instance=item)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form)
        messages.success(request, "Komisariat berhasil diperbarui.")
        return redirect("cadre:commissariat_list")
    return render(request, "admin/form.html", {"form": form, "title": "Edit Komisariat"})


@login_required
def cadre_list_view(request):
    return _admin_list(request, selectors.cadre_list(), "admin/cadre/cadre_list.html", "items")


@login_required
def cadre_create_view(request):
    form = CadreForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form)
        messages.success(request, "Kader berhasil disimpan.")
        return redirect("cadre:cadre_list")
    return render(request, "admin/form.html", {"form": form, "title": "Tambah Kader"})


@login_required
def cadre_update_view(request, item_id):
    item = selectors.cadre_get(item_id)
    form = CadreForm(request.POST or None, request.FILES or None, instance=item)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form)
        messages.success(request, "Kader berhasil diperbarui.")
        return redirect("cadre:cadre_list")
    return render(request, "admin/form.html", {"form": form, "title": "Edit Kader"})


@login_required
def alumni_list_view(request):
    return _admin_list(request, selectors.alumni_list(), "admin/cadre/alumni_list.html", "items")


@login_required
def alumni_create_view(request):
    form = AlumniForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form)
        messages.success(request, "Alumni berhasil disimpan.")
        return redirect("cadre:alumni_list")
    return render(request, "admin/form.html", {"form": form, "title": "Tambah Alumni"})


@login_required
def alumni_update_view(request, item_id):
    item = selectors.alumni_get(item_id)
    form = AlumniForm(request.POST or None, request.FILES or None, instance=item)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form)
        messages.success(request, "Alumni berhasil diperbarui.")
        return redirect("cadre:alumni_list")
    return render(request, "admin/form.html", {"form": form, "title": "Edit Alumni"})


@login_required
def lk_history_list_view(request):
    return _admin_list(request, selectors.lk_history_list(), "admin/cadre/lk_history_list.html", "items")


@login_required
def lk_history_create_view(request):
    form = CadreLkHistoryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form)
        messages.success(request, "Riwayat LK berhasil disimpan.")
        return redirect("cadre:lk_history_list")
    return render(request, "admin/form.html", {"form": form, "title": "Tambah Riwayat LK"})
