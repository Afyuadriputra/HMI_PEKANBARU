from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from apps.core.pagination import paginate_queryset
from apps.registration import selectors, services
from apps.registration.forms import RegistrationFormForm


def registration_list_view(request):
    return render(request, "public/registration/list.html", {"forms": selectors.active_registration_forms()})


@login_required
def registration_admin_list_view(request):
    page = paginate_queryset(request, selectors.registration_form_list())
    return render(request, "admin/registration/form_list.html", {"forms": page})


@login_required
def registration_create_view(request):
    form = RegistrationFormForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        services.save_registration_form(form, request.user)
        messages.success(request, "Link pendaftaran berhasil disimpan.")
        return redirect("registration:admin_list")
    return render(request, "admin/form.html", {"form": form, "title": "Tambah Link Pendaftaran"})


@login_required
def registration_update_view(request, form_id):
    registration_form = selectors.registration_form_get(form_id)
    form = RegistrationFormForm(request.POST or None, instance=registration_form)
    if request.method == "POST" and form.is_valid():
        services.save_registration_form(form, request.user)
        messages.success(request, "Link pendaftaran berhasil diperbarui.")
        return redirect("registration:admin_list")
    return render(request, "admin/form.html", {"form": form, "title": "Edit Link Pendaftaran"})
