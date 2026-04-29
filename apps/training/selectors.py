from apps.training.models import LkAssessment, LkBatch, LkCertificate, LkLevel, LkMaterial, LkParticipant, Signature


def lk_level_list():
    return LkLevel.objects.order_by("id")


def lk_level_get(item_id):
    return LkLevel.objects.get(pk=item_id)


def lk_batch_list():
    return LkBatch.objects.select_related("lk_level", "created_by").order_by("-start_date", "-created_at")


def lk_batch_get(item_id):
    return LkBatch.objects.select_related("lk_level").get(pk=item_id)


def participant_list():
    return LkParticipant.objects.select_related("batch", "cadre", "commissariat").order_by("full_name")


def participant_get(item_id):
    return LkParticipant.objects.select_related("batch", "cadre", "commissariat").get(pk=item_id)


def material_list():
    return LkMaterial.objects.select_related("lk_level", "batch").order_by("sort_order", "title")


def material_get(item_id):
    return LkMaterial.objects.select_related("lk_level", "batch").get(pk=item_id)


def assessment_list():
    return LkAssessment.objects.select_related("participant", "batch", "assessor").prefetch_related("details").order_by("-assessed_at", "-created_at")


def assessment_get(item_id):
    return LkAssessment.objects.select_related("participant", "batch", "assessor").prefetch_related("details").get(pk=item_id)


def signature_list():
    return Signature.objects.order_by("name")


def certificate_list():
    return LkCertificate.objects.select_related("participant", "assessment", "signature").order_by("-issued_date", "-created_at")


def certificate_get(item_id):
    return LkCertificate.objects.select_related("participant", "assessment", "signature").get(pk=item_id)
