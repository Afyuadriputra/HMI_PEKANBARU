from datetime import date

from django.contrib.auth import get_user_model

from apps.accounts.models import Role
from apps.content.models import NewsCategory
from apps.training.models import LkBatch, LkLevel, LkParticipant


def create_role(name=Role.SUPER_ADMIN):
    return Role.objects.create(name=name, description=f"{name} role")


def create_user(email="admin@example.com", password="StrongPass123", role=None, **extra_fields):
    role = role or create_role()
    defaults = {
        "name": "Admin Test",
        "status": get_user_model().STATUS_ACTIVE,
        "is_staff": True,
    }
    defaults.update(extra_fields)
    return get_user_model().objects.create_user(
        email=email,
        password=password,
        role=role,
        **defaults,
    )


def create_news_category(name="Kegiatan"):
    return NewsCategory.objects.create(name=name, slug=name.lower().replace(" ", "-"))


def create_lk_batch(title="Basic Training HMI"):
    level = LkLevel.objects.create(name="LK 1", description="Latihan Kader 1")
    return LkBatch.objects.create(
        lk_level=level,
        title=title,
        theme="Mission HMI",
        location="Pekanbaru",
        start_date=date(2026, 5, 10),
        status=LkBatch.STATUS_OPEN,
    )


def create_lk_participant(batch=None, full_name="Peserta Test"):
    batch = batch or create_lk_batch()
    return LkParticipant.objects.create(
        batch=batch,
        full_name=full_name,
        email="peserta@example.com",
        phone="08123456789",
        university="UIN Suska Riau",
        registration_status=LkParticipant.REGISTRATION_VERIFIED,
    )
