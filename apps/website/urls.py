from django.urls import path

from apps.website import views

app_name = "website"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("desktop.html", views.desktop_view, name="desktop"),
    path("mobile.html", views.mobile_view, name="mobile"),

    # sementara kalau URL lama masih sering dibuka
    path("dekstop.html", views.desktop_view, name="desktop_old"),

    path("admin/settings/", views.setting_list_view, name="setting_list"),
    path("admin/settings/create/", views.setting_create_view, name="setting_create"),
    path("admin/settings/<int:setting_id>/edit/", views.setting_update_view, name="setting_update"),
    path("admin/menus/", views.menu_list_view, name="menu_list"),
    path("admin/menus/create/", views.menu_create_view, name="menu_create"),
    path("admin/menus/<int:menu_id>/edit/", views.menu_update_view, name="menu_update"),
]
