from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render

from apps.core.pagination import paginate_queryset
from apps.news_request import selectors, services
from apps.news_request.forms import NewsRequestPaymentForm, NewsRequestReviewForm, NewsUploadRequestForm


def request_create_view(request):
    form = NewsUploadRequestForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        news_request = services.create_news_request(form)
        messages.success(request, "Request berita berhasil dibuat. Silakan upload bukti pembayaran.")
        return redirect("news_request:payment_upload", item_id=news_request.id)
    return render(request, "public/news_request/form.html", {"form": form})


def payment_upload_view(request, item_id):
    news_request = selectors.request_get(item_id)
    payment = news_request.payment
    form = NewsRequestPaymentForm(request.POST or None, request.FILES or None, instance=payment)
    if request.method == "POST" and form.is_valid():
        services.upload_payment_proof(form)
        messages.success(request, "Bukti pembayaran berhasil diupload.")
        return redirect("website:home")
    return render(request, "public/news_request/payment_form.html", {"form": form, "news_request": news_request})


@login_required
def request_admin_list_view(request):
    return render(request, "admin/news_request/list.html", {"items": paginate_queryset(request, selectors.request_list())})


@login_required
def verify_payment_view(request, item_id):
    payment = selectors.payment_get_by_request(item_id)
    if request.method == "POST":
        services.verify_payment(payment, request.user)
        messages.success(request, "Pembayaran berhasil diverifikasi.")
        return redirect("news_request:admin_list")
    return render(request, "admin/confirm_action.html", {"title": "Verifikasi Pembayaran", "object": payment.request, "button_label": "Verifikasi"})


@login_required
def approve_view(request, item_id):
    news_request = selectors.request_get(item_id)
    form = NewsRequestReviewForm(request.POST or None, instance=news_request)
    if request.method == "POST" and form.is_valid():
        services.approve_request(news_request, request.user, form.cleaned_data.get("notes", ""))
        messages.success(request, "Request berhasil di-approve.")
        return redirect("news_request:admin_list")
    return render(request, "admin/form.html", {"form": form, "title": "Approve Request Berita"})


@login_required
def reject_view(request, item_id):
    news_request = selectors.request_get(item_id)
    form = NewsRequestReviewForm(request.POST or None, instance=news_request)
    if request.method == "POST" and form.is_valid():
        services.reject_request(news_request, request.user, form.cleaned_data.get("notes", ""))
        messages.success(request, "Request berhasil ditolak.")
        return redirect("news_request:admin_list")
    return render(request, "admin/form.html", {"form": form, "title": "Reject Request Berita"})


@login_required
def publish_view(request, item_id):
    news_request = selectors.request_get(item_id)
    if request.method == "POST":
        try:
            services.publish_news_request_as_post(news_request, request.user)
            messages.success(request, "Request berhasil dipublish menjadi berita.")
        except ValidationError as exc:
            messages.error(request, exc.message)
        return redirect("news_request:admin_list")
    return render(request, "admin/confirm_action.html", {"title": "Publish Request", "object": news_request, "button_label": "Publish"})
