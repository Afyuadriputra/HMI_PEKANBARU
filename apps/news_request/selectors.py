from apps.news_request.models import NewsRequestPayment, NewsUploadRequest


def request_list():
    return NewsUploadRequest.objects.select_related("category", "reviewed_by").order_by("-created_at")


def request_get(item_id):
    return NewsUploadRequest.objects.select_related("category", "reviewed_by").get(pk=item_id)


def payment_get_by_request(request_id):
    return NewsRequestPayment.objects.select_related("request", "verified_by").get(request_id=request_id)
