from django import forms

from apps.administration.models import DocumentArchive, IncomingLetter, Invitation, OutgoingLetter

DOCUMENT_EXTENSIONS = {"pdf", "doc", "docx", "xls", "xlsx"}
TAILWIND_INPUT = "w-full rounded border border-slate-300 px-3 py-2 text-sm"


def validate_document_extension(file_obj):
    if not file_obj:
        return
    extension = file_obj.name.rsplit(".", 1)[-1].lower()
    if extension not in DOCUMENT_EXTENSIONS:
        raise forms.ValidationError("File dokumen harus pdf, doc, docx, xls, atau xlsx.")


def apply_tailwind(form):
    for field in form.fields.values():
        field.widget.attrs["class"] = f"{field.widget.attrs.get('class', '')} {TAILWIND_INPUT}".strip()
    return form


class DocumentArchiveForm(forms.ModelForm):
    class Meta:
        model = DocumentArchive
        exclude = ("uploaded_by",)
        widgets = {"archive_date": forms.DateInput(attrs={"type": "date"}), "description": forms.Textarea(attrs={"rows": 3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)

    def clean_file_path(self):
        file_obj = self.cleaned_data.get("file_path")
        validate_document_extension(file_obj)
        return file_obj


class IncomingLetterForm(forms.ModelForm):
    class Meta:
        model = IncomingLetter
        exclude = ("created_by",)
        widgets = {"received_date": forms.DateInput(attrs={"type": "date"}), "letter_date": forms.DateInput(attrs={"type": "date"}), "description": forms.Textarea(attrs={"rows": 3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)

    def clean_file_path(self):
        file_obj = self.cleaned_data.get("file_path")
        validate_document_extension(file_obj)
        return file_obj


class OutgoingLetterForm(forms.ModelForm):
    class Meta:
        model = OutgoingLetter
        exclude = ("created_by", "sent_at")
        widgets = {"letter_date": forms.DateInput(attrs={"type": "date"}), "content": forms.Textarea(attrs={"rows": 5})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)

    def clean_file_path(self):
        file_obj = self.cleaned_data.get("file_path")
        validate_document_extension(file_obj)
        return file_obj


class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitation
        exclude = ("created_by", "sent_at")
        widgets = {"invitation_date": forms.DateInput(attrs={"type": "date"}), "event_date": forms.DateInput(attrs={"type": "date"}), "content": forms.Textarea(attrs={"rows": 5})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)

    def clean_file_path(self):
        file_obj = self.cleaned_data.get("file_path")
        validate_document_extension(file_obj)
        return file_obj
