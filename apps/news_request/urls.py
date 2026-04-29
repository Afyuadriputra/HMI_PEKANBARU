from django.urls import path

from apps.news_request import views

app_name = "news_request"

urlpatterns = [
    path("create/", views.request_create_view, name="create"),
    path("<int:item_id>/payment/", views.payment_upload_view, name="payment_upload"),
    path("admin/", views.request_admin_list_view, name="admin_list"),
    path("admin/<int:item_id>/verify-payment/", views.verify_payment_view, name="verify_payment"),
    path("admin/<int:item_id>/approve/", views.approve_view, name="approve"),
    path("admin/<int:item_id>/reject/", views.reject_view, name="reject"),
    path("admin/<int:item_id>/publish/", views.publish_view, name="publish"),
]
