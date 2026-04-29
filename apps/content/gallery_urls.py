from django.urls import path

from apps.content import views

app_name = "gallery"

urlpatterns = [
    path("", views.gallery_list_view, name="list"),
    path("admin/", views.gallery_admin_list_view, name="admin_list"),
    path("admin/create/", views.gallery_create_view, name="create"),
    path("admin/<int:image_id>/edit/", views.gallery_update_view, name="update"),
]
