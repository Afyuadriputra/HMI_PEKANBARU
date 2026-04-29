from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from apps.accounts import selectors, services
from apps.accounts.forms import LoginForm, UserAdminCreationForm, UserUpdateForm
from apps.core.pagination import paginate_queryset


def login_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:dashboard")

    form = LoginForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("accounts:dashboard")

    return render(request, "admin/login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return redirect("accounts:login")


@login_required
def dashboard_view(request):
    return render(request, "admin/dashboard.html", {"counts": selectors.dashboard_counts()})


@login_required
def user_list_view(request):
    users = paginate_queryset(request, selectors.user_list(), per_page=10)
    return render(request, "admin/accounts/user_list.html", {"users": users})


@login_required
def user_create_view(request):
    form = UserAdminCreationForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        services.save_user_form(form)
        messages.success(request, "User berhasil dibuat.")
        return redirect("accounts:user_list")
    return render(request, "admin/form.html", {"form": form, "title": "Tambah User"})


@login_required
def user_update_view(request, user_id):
    user = selectors.user_get(user_id)
    form = UserUpdateForm(request.POST or None, request.FILES or None, instance=user)
    if request.method == "POST" and form.is_valid():
        services.save_user_form(form)
        messages.success(request, "User berhasil diperbarui.")
        return redirect("accounts:user_list")
    return render(request, "admin/form.html", {"form": form, "title": "Edit User"})


@login_required
def user_delete_view(request, user_id):
    user = selectors.user_get(user_id)
    if request.method == "POST":
        services.delete_user(user)
        messages.success(request, "User berhasil dihapus.")
        return redirect("accounts:user_list")
    return render(request, "admin/confirm_delete.html", {"object": user, "cancel_url": "accounts:user_list"})
