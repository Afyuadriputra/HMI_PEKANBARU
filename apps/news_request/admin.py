from django.contrib import admin

from apps.news_request.models import NewsRequestPayment, NewsUploadRequest


class NewsRequestPaymentInline(admin.StackedInline):
    model = NewsRequestPayment
    extra = 0
    max_num = 1


@admin.register(NewsUploadRequest)
class NewsUploadRequestAdmin(admin.ModelAdmin):
    list_display = ("title", "requester_name", "requester_email", "price", "status", "reviewed_by", "created_at")
    list_filter = ("status", "category", "created_at")
    search_fields = ("title", "requester_name", "requester_email", "requester_phone", "content")
    autocomplete_fields = ("category", "reviewed_by")
    inlines = (NewsRequestPaymentInline,)


@admin.register(NewsRequestPayment)
class NewsRequestPaymentAdmin(admin.ModelAdmin):
    list_display = ("request", "amount", "payment_method", "payment_status", "verified_by", "verified_at")
    list_filter = ("payment_status", "payment_method", "verified_at")
    search_fields = ("request__title", "payment_method")
    autocomplete_fields = ("request", "verified_by")
