from django import forms

from apps.training.models import LkAssessment, LkAssessmentDetail, LkBatch, LkCertificate, LkLevel, LkMaterial, LkParticipant, Signature

DOCUMENT_EXTENSIONS = {"pdf", "doc", "docx", "xls", "xlsx"}
IMAGE_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}
TAILWIND_INPUT = "w-full rounded border border-slate-300 px-3 py-2 text-sm"


def validate_file_extension(file_obj, allowed, message):
    if not file_obj:
        return
    extension = file_obj.name.rsplit(".", 1)[-1].lower()
    if extension not in allowed:
        raise forms.ValidationError(message)


def apply_tailwind(form):
    for field in form.fields.values():
        field.widget.attrs["class"] = f"{field.widget.attrs.get('class', '')} {TAILWIND_INPUT}".strip()
    return form


class LkLevelForm(forms.ModelForm):
    class Meta:
        model = LkLevel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)


class LkBatchForm(forms.ModelForm):
    class Meta:
        model = LkBatch
        exclude = ("created_by",)
        widgets = {"start_date": forms.DateInput(attrs={"type": "date"}), "end_date": forms.DateInput(attrs={"type": "date"}), "registration_open": forms.DateInput(attrs={"type": "date"}), "registration_close": forms.DateInput(attrs={"type": "date"})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)


class LkParticipantForm(forms.ModelForm):
    class Meta:
        model = LkParticipant
        fields = "__all__"
        widgets = {"address": forms.Textarea(attrs={"rows": 3}), "motivation": forms.Textarea(attrs={"rows": 3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)

    def clean_photo(self):
        file_obj = self.cleaned_data.get("photo")
        validate_file_extension(file_obj, IMAGE_EXTENSIONS, "File gambar harus jpg, jpeg, png, atau webp.")
        return file_obj


class LkMaterialForm(forms.ModelForm):
    class Meta:
        model = LkMaterial
        fields = "__all__"
        widgets = {"description": forms.Textarea(attrs={"rows": 3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)


class LkAssessmentForm(forms.ModelForm):
    class Meta:
        model = LkAssessment
        exclude = ("assessor",)
        widgets = {"assessed_at": forms.DateTimeInput(attrs={"type": "datetime-local"}), "notes": forms.Textarea(attrs={"rows": 3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)


class LkAssessmentDetailForm(forms.ModelForm):
    class Meta:
        model = LkAssessmentDetail
        exclude = ("assessment",)
        widgets = {"notes": forms.Textarea(attrs={"rows": 2})}


class LkCertificateForm(forms.ModelForm):
    class Meta:
        model = LkCertificate
        fields = "__all__"
        widgets = {"issued_date": forms.DateInput(attrs={"type": "date"})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)

    def clean_file_path(self):
        file_obj = self.cleaned_data.get("file_path")
        validate_file_extension(file_obj, DOCUMENT_EXTENSIONS | IMAGE_EXTENSIONS, "File sertifikat harus pdf, doc, docx, xls, xlsx, jpg, jpeg, png, atau webp.")
        return file_obj


class SignatureForm(forms.ModelForm):
    class Meta:
        model = Signature
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)
