from decimal import Decimal

from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from apps.core.test_factories import create_lk_participant, create_user
from apps.training.forms import LkCertificateForm
from apps.training.models import LkAssessment, LkAssessmentDetail, LkMaterial, LkParticipant
from apps.training.services import create_lk_assessment


class LkAssessmentForm(forms.ModelForm):
    class Meta:
        model = LkAssessment
        fields = ("participant", "batch", "result_status", "notes")


class LkAssessmentDetailForm(forms.ModelForm):
    class Meta:
        model = LkAssessmentDetail
        fields = ("material", "score", "grade", "notes")


class TrainingWorkflowTests(TestCase):
    def setUp(self):
        self.assessor = create_user()
        self.participant = create_lk_participant()
        self.material_a = LkMaterial.objects.create(
            lk_level=self.participant.batch.lk_level,
            batch=self.participant.batch,
            title="Sejarah HMI",
        )
        self.material_b = LkMaterial.objects.create(
            lk_level=self.participant.batch.lk_level,
            batch=self.participant.batch,
            title="Nilai Dasar Perjuangan",
        )

    def test_passed_assessment_calculates_average_score_and_marks_participant_passed(self):
        assessment_form = LkAssessmentForm(
            data={
                "participant": self.participant.id,
                "batch": self.participant.batch.id,
                "result_status": LkAssessment.RESULT_PASSED,
                "notes": "Peserta aktif",
            }
        )
        detail_forms = [
            LkAssessmentDetailForm(data={"material": self.material_a.id, "score": "80.00", "grade": "B"}),
            LkAssessmentDetailForm(data={"material": self.material_b.id, "score": "90.00", "grade": "A"}),
        ]

        self.assertTrue(assessment_form.is_valid(), assessment_form.errors)
        for detail_form in detail_forms:
            self.assertTrue(detail_form.is_valid(), detail_form.errors)

        assessment = create_lk_assessment(assessment_form, detail_forms, self.assessor)
        self.participant.refresh_from_db()

        self.assertEqual(assessment.assessor, self.assessor)
        self.assertEqual(assessment.total_score, Decimal("85.00"))
        self.assertEqual(assessment.details.count(), 2)
        self.assertEqual(self.participant.graduation_status, LkParticipant.GRADUATION_PASSED)

    def test_failed_assessment_marks_participant_failed(self):
        assessment_form = LkAssessmentForm(
            data={
                "participant": self.participant.id,
                "batch": self.participant.batch.id,
                "result_status": LkAssessment.RESULT_FAILED,
            }
        )
        detail_form = LkAssessmentDetailForm(data={"material": self.material_a.id, "score": "55.00", "grade": "D"})

        self.assertTrue(assessment_form.is_valid(), assessment_form.errors)
        self.assertTrue(detail_form.is_valid(), detail_form.errors)
        create_lk_assessment(assessment_form, [detail_form], self.assessor)
        self.participant.refresh_from_db()

        self.assertEqual(self.participant.graduation_status, LkParticipant.GRADUATION_FAILED)

    def test_certificate_upload_rejects_unsupported_file_extension(self):
        bad_file = SimpleUploadedFile("sertifikat.exe", b"not-valid", content_type="application/octet-stream")
        form = LkCertificateForm(
            data={
                "participant": self.participant.id,
                "certificate_number": "LK1-001",
                "title": "Sertifikat LK 1",
            },
            files={"file_path": bad_file},
        )

        self.assertFalse(form.is_valid())
        self.assertIn("file_path", form.errors)
