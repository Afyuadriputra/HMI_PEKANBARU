from django import forms

from apps.news_request.models import NewsRequestPayment, NewsUploadRequest

DOCUMENT_EXTENSIONS = {"pdf", "doc", "docx", "xls", "xlsx"}
IMAGE_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}
TAILWIND_INPUT = "w-full rounded border border-slate-300 px-3 py-2 text-sm"


def validate_extension(file_obj, allowed, message):
    if not file_obj:
        return
    extension = file_obj.name.rsplit(".", 1)[-1].lower()
    if extension not in allowed:
        raise forms.ValidationError(message)


def apply_tailwind(form):
    for field in form.fields.values():
        field.widget.attrs["class"] = f"{field.widget.attrs.get('class', '')} {TAILWIND_INPUT}".strip()
    return form


class NewsUploadRequestForm(forms.ModelForm):
    class Meta:
        model = NewsUploadRequest
        fields = ("requester_name", "requester_email", "requester_phone", "title", "category", "content", "image", "attachment")
        widgets = {"content": forms.Textarea(attrs={"rows": 8})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)

    def clean_image(self):
        file_obj = self.cleaned_data.get("image")
        validate_extension(file_obj, IMAGE_EXTENSIONS, "File gambar harus jpg, jpeg, png, atau webp.")
        return file_obj

    def clean_attachment(self):
        file_obj = self.cleaned_data.get("attachment")
        validate_extension(file_obj, DOCUMENT_EXTENSIONS, "Lampiran harus pdf, doc, docx, xls, atau xlsx.")
        return file_obj


class NewsRequestPaymentForm(forms.ModelForm):
    class Meta:
        model = NewsRequestPayment
        fields = ("payment_method", "payment_proof")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)

    def clean_payment_proof(self):
        file_obj = self.cleaned_data.get("payment_proof")
        if not file_obj and not getattr(self.instance, "payment_proof", None):
            raise forms.ValidationError("Bukti pembayaran wajib diupload.")
        validate_extension(file_obj, IMAGE_EXTENSIONS, "Bukti pembayaran harus jpg, jpeg, png, atau webp.")
        return file_obj


class NewsRequestReviewForm(forms.ModelForm):
    class Meta:
        model = NewsUploadRequest
        fields = ("notes",)
        widgets = {"notes": forms.Textarea(attrs={"rows": 4})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)
