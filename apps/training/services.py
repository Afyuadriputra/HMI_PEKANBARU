from django.db import transaction
from django.utils import timezone

from apps.training.models import LkAssessment, LkAssessmentDetail, LkCertificate, LkParticipant


@transaction.atomic
def save_model_form(form, user=None):
    instance = form.save(commit=False)
    if hasattr(instance, "created_by_id") and user and not instance.created_by_id:
        instance.created_by = user
    instance.save()
    form.save_m2m()
    return instance


@transaction.atomic
def create_lk_assessment(assessment_form, detail_forms, assessor=None):
    assessment = assessment_form.save(commit=False)
    if assessor and not assessment.assessor_id:
        assessment.assessor = assessor
    if not assessment.assessed_at:
        assessment.assessed_at = timezone.now()
    assessment.save()

    total = 0
    count = 0
    for detail_form in detail_forms:
        if not detail_form.cleaned_data:
            continue
        detail = detail_form.save(commit=False)
        detail.assessment = assessment
        detail.save()
        if detail.score is not None:
            total += detail.score
            count += 1

    if assessment.total_score is None and count:
        assessment.total_score = total / count
        assessment.save(update_fields=["total_score", "updated_at"])

    participant = assessment.participant
    if assessment.result_status == LkAssessment.RESULT_PASSED:
        participant.graduation_status = LkParticipant.GRADUATION_PASSED
    elif assessment.result_status == LkAssessment.RESULT_FAILED:
        participant.graduation_status = LkParticipant.GRADUATION_FAILED
    participant.save(update_fields=["graduation_status", "updated_at"])
    return assessment


@transaction.atomic
def upload_lk_certificate(form):
    certificate = form.save(commit=False)
    certificate.save()
    return certificate


@transaction.atomic
def delete_instance(instance):
    instance.delete()
