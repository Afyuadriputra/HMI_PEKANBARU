from apps.cadre.models import Alumni, Cadre, CadreLkHistory, Commissariat


def commissariat_list():
    return Commissariat.objects.order_by("name")


def commissariat_get(item_id):
    return Commissariat.objects.get(pk=item_id)


def cadre_list():
    return Cadre.objects.select_related("commissariat").order_by("full_name")


def cadre_get(item_id):
    return Cadre.objects.select_related("commissariat").get(pk=item_id)


def alumni_list():
    return Alumni.objects.select_related("cadre", "commissariat").order_by("full_name")


def alumni_get(item_id):
    return Alumni.objects.select_related("cadre", "commissariat").get(pk=item_id)


def lk_history_list():
    return CadreLkHistory.objects.select_related("cadre", "lk_level", "batch").order_by("-year", "-created_at")


def lk_history_get(item_id):
    return CadreLkHistory.objects.select_related("cadre", "lk_level", "batch").get(pk=item_id)
