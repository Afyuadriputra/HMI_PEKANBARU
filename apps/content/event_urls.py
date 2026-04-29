from django.urls import path

from apps.content import views

app_name = "events"

urlpatterns = [
    path("", views.event_list_view, name="list"),
    path("admin/", views.event_admin_list_view, name="admin_list"),
    path("admin/create/", views.event_create_view, name="create"),
    path("admin/<int:event_id>/edit/", views.event_update_view, name="update"),
    path("<slug:slug>/", views.event_detail_view, name="detail"),
]
