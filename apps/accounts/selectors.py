from django.contrib.auth import get_user_model

from apps.accounts.models import Role

User = get_user_model()


def role_list():
    return Role.objects.all().order_by("name")


def user_list():
    return User.objects.select_related("role").order_by("name")


def user_get(user_id):
    return User.objects.select_related("role").get(pk=user_id)


def dashboard_counts():
    from apps.cadre.models import Alumni, Cadre, Commissariat
    from apps.content.models import Event, GalleryImage, NewsPost, Program
    from apps.news_request.models import NewsUploadRequest

    return {
        "users": User.objects.count(),
        "programs": Program.objects.count(),
        "news": NewsPost.objects.count(),
        "events": Event.objects.count(),
        "gallery": GalleryImage.objects.count(),
        "commissariats": Commissariat.objects.count(),
        "cadres": Cadre.objects.count(),
        "alumni": Alumni.objects.count(),
        "news_requests": NewsUploadRequest.objects.count(),
    }
