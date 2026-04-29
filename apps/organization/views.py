from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from apps.core.pagination import paginate_queryset
from apps.organization import selectors, services
from apps.organization.forms import ChairmanHistoryForm, ManagementMemberForm, OrganizationProfileForm


def profile_view(request):
    return render(request, "public/organization/profile.html", {"profile": selectors.organization_profile()})


def management_view(request):
    return render(request, "public/organization/management.html", {"members": selectors.active_management_members()})


def chairmen_view(request):
    return render(request, "public/organization/chairmen.html", {"chairmen": selectors.visible_chairmen()})


@login_required
def profile_list_view(request):
    page = paginate_queryset(request, selectors.organization_profile_list())
    return render(request, "admin/organization/profile_list.html", {"profiles": page})


@login_required
def profile_create_view(request):
    form = OrganizationProfileForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form)
        messages.success(request, "Profil berhasil disimpan.")
        return redirect("organization:profile_list")
    return render(request, "admin/form.html", {"form": form, "title": "Tambah Profil"})


@login_required
def profile_update_view(request, profile_id):
    profile = selectors.organization_profile_get(profile_id)
    form = OrganizationProfileForm(request.POST or None, request.FILES or None, instance=profile)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form)
        messages.success(request, "Profil berhasil diperbarui.")
        return redirect("organization:profile_list")
    return render(request, "admin/form.html", {"form": form, "title": "Edit Profil"})


@login_required
def management_list_view(request):
    page = paginate_queryset(request, selectors.management_member_list())
    return render(request, "admin/organization/management_list.html", {"members": page})


@login_required
def management_create_view(request):
    form = ManagementMemberForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form)
        messages.success(request, "Pengurus berhasil disimpan.")
        return redirect("organization:management_list")
    return render(request, "admin/form.html", {"form": form, "title": "Tambah Pengurus"})


@login_required
def management_update_view(request, member_id):
    member = selectors.management_member_get(member_id)
    form = ManagementMemberForm(request.POST or None, request.FILES or None, instance=member)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form)
        messages.success(request, "Pengurus berhasil diperbarui.")
        return redirect("organization:management_list")
    return render(request, "admin/form.html", {"form": form, "title": "Edit Pengurus"})


@login_required
def chairman_list_view(request):
    page = paginate_queryset(request, selectors.chairman_list())
    return render(request, "admin/organization/chairman_list.html", {"chairmen": page})


@login_required
def chairman_create_view(request):
    form = ChairmanHistoryForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form)
        messages.success(request, "Ketua umum berhasil disimpan.")
        return redirect("organization:chairman_list")
    return render(request, "admin/form.html", {"form": form, "title": "Tambah Ketua Umum"})


@login_required
def chairman_update_view(request, chairman_id):
    chairman = selectors.chairman_get(chairman_id)
    form = ChairmanHistoryForm(request.POST or None, request.FILES or None, instance=chairman)
    if request.method == "POST" and form.is_valid():
        services.save_model_form(form)
        messages.success(request, "Ketua umum berhasil diperbarui.")
        return redirect("organization:chairman_list")
    return render(request, "admin/form.html", {"form": form, "title": "Edit Ketua Umum"})
