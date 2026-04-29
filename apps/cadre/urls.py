from django.urls import path

from apps.cadre import views

app_name = "cadre"

urlpatterns = [
    path("komisariat/", views.commissariat_list_view, name="commissariat_list"),
    path("komisariat/create/", views.commissariat_create_view, name="commissariat_create"),
    path("komisariat/<int:item_id>/edit/", views.commissariat_update_view, name="commissariat_update"),
    path("kader/", views.cadre_list_view, name="cadre_list"),
    path("kader/create/", views.cadre_create_view, name="cadre_create"),
    path("kader/<int:item_id>/edit/", views.cadre_update_view, name="cadre_update"),
    path("alumni/", views.alumni_list_view, name="alumni_list"),
    path("alumni/create/", views.alumni_create_view, name="alumni_create"),
    path("alumni/<int:item_id>/edit/", views.alumni_update_view, name="alumni_update"),
    path("riwayat-lk/", views.lk_history_list_view, name="lk_history_list"),
    path("riwayat-lk/create/", views.lk_history_create_view, name="lk_history_create"),
]
