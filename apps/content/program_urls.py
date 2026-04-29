from django.urls import path

from apps.content import views

app_name = "programs"

urlpatterns = [
    path("", views.program_list_view, name="list"),
    path("admin/", views.program_admin_list_view, name="admin_list"),
    path("admin/create/", views.program_create_view, name="create"),
    path("admin/<int:program_id>/edit/", views.program_update_view, name="update"),
    path("<slug:slug>/", views.program_detail_view, name="detail"),
]
