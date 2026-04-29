from django.urls import path

from apps.registration import views

app_name = "registration"

urlpatterns = [
    path("", views.registration_list_view, name="list"),
    path("admin/", views.registration_admin_list_view, name="admin_list"),
    path("admin/create/", views.registration_create_view, name="create"),
    path("admin/<int:form_id>/edit/", views.registration_update_view, name="update"),
]
