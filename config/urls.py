"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.website.urls")),
    path("accounts/", include("apps.accounts.urls")),
    path("organisasi/", include("apps.organization.urls")),
    path("berita/", include("apps.content.news_urls")),
    path("program/", include("apps.content.program_urls")),
    path("agenda/", include("apps.content.event_urls")),
    path("galeri/", include("apps.content.gallery_urls")),
    path("pendaftaran/", include("apps.registration.urls")),
    path("cadre/", include("apps.cadre.urls")),
    path("training/", include("apps.training.urls")),
    path("administrasi/", include("apps.administration.urls")),
    path("request-berita/", include("apps.news_request.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    if "debug_toolbar" in settings.INSTALLED_APPS:
        urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
