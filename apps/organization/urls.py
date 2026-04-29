from django.urls import path

from apps.organization import views

app_name = "organization"

urlpatterns = [
    path("profil/", views.profile_view, name="profile"),
    path("pengurus/", views.management_view, name="management"),
    path("ketua-umum/", views.chairmen_view, name="chairmen"),
    path("admin/profil/", views.profile_list_view, name="profile_list"),
    path("admin/profil/create/", views.profile_create_view, name="profile_create"),
    path("admin/profil/<int:profile_id>/edit/", views.profile_update_view, name="profile_update"),
    path("admin/pengurus/", views.management_list_view, name="management_list"),
    path("admin/pengurus/create/", views.management_create_view, name="management_create"),
    path("admin/pengurus/<int:member_id>/edit/", views.management_update_view, name="management_update"),
    path("admin/ketua-umum/", views.chairman_list_view, name="chairman_list"),
    path("admin/ketua-umum/create/", views.chairman_create_view, name="chairman_create"),
    path("admin/ketua-umum/<int:chairman_id>/edit/", views.chairman_update_view, name="chairman_update"),
]
