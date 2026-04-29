from django.urls import path

from apps.content import views

app_name = "news"

urlpatterns = [
    path("", views.news_list_view, name="list"),
    path("admin/", views.news_admin_list_view, name="admin_list"),
    path("admin/create/", views.news_create_view, name="create"),
    path("admin/<int:news_id>/edit/", views.news_update_view, name="update"),
    path("<slug:slug>/", views.news_detail_view, name="detail"),
]
