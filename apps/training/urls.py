from django.urls import path

from apps.training import views

app_name = "training"

urlpatterns = [
    path("level/", views.level_list_view, name="level_list"),
    path("level/create/", views.level_create_view, name="level_create"),
    path("level/<int:item_id>/edit/", views.level_update_view, name="level_update"),
    path("batch/", views.batch_list_view, name="batch_list"),
    path("batch/create/", views.batch_create_view, name="batch_create"),
    path("batch/<int:item_id>/edit/", views.batch_update_view, name="batch_update"),
    path("peserta/", views.participant_list_view, name="participant_list"),
    path("peserta/create/", views.participant_create_view, name="participant_create"),
    path("peserta/<int:item_id>/edit/", views.participant_update_view, name="participant_update"),
    path("materi/", views.material_list_view, name="material_list"),
    path("materi/create/", views.material_create_view, name="material_create"),
    path("materi/<int:item_id>/edit/", views.material_update_view, name="material_update"),
    path("sertifikat/", views.certificate_list_view, name="certificate_list"),
    path("sertifikat/create/", views.certificate_create_view, name="certificate_create"),
    path("sertifikat/<int:item_id>/edit/", views.certificate_update_view, name="certificate_update"),
]
