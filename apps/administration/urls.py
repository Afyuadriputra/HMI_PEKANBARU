from django.urls import path

from apps.administration import views

app_name = "administration"

urlpatterns = [
    path("arsip/", views.archive_list_view, name="archive_list"),
    path("arsip/create/", views.archive_create_view, name="archive_create"),
    path("arsip/<int:item_id>/edit/", views.archive_update_view, name="archive_update"),
    path("surat-masuk/", views.incoming_list_view, name="incoming_list"),
    path("surat-masuk/create/", views.incoming_create_view, name="incoming_create"),
    path("surat-masuk/<int:item_id>/edit/", views.incoming_update_view, name="incoming_update"),
    path("surat-keluar/", views.outgoing_list_view, name="outgoing_list"),
    path("surat-keluar/create/", views.outgoing_create_view, name="outgoing_create"),
    path("surat-keluar/<int:item_id>/edit/", views.outgoing_update_view, name="outgoing_update"),
    path("undangan/", views.invitation_list_view, name="invitation_list"),
    path("undangan/create/", views.invitation_create_view, name="invitation_create"),
    path("undangan/<int:item_id>/edit/", views.invitation_update_view, name="invitation_update"),
]
