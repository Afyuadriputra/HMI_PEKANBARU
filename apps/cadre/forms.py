from django import forms

from apps.cadre.models import Alumni, Cadre, CadreLkHistory, Commissariat

IMAGE_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}
TAILWIND_INPUT = "w-full rounded border border-slate-300 px-3 py-2 text-sm"


def validate_image_extension(file_obj):
    if not file_obj:
        return
    extension = file_obj.name.rsplit(".", 1)[-1].lower()
    if extension not in IMAGE_EXTENSIONS:
        raise forms.ValidationError("File gambar harus jpg, jpeg, png, atau webp.")


def apply_tailwind(form):
    for field in form.fields.values():
        field.widget.attrs["class"] = f"{field.widget.attrs.get('class', '')} {TAILWIND_INPUT}".strip()
    return form


class CommissariatForm(forms.ModelForm):
    class Meta:
        model = Commissariat
        fields = "__all__"
        widgets = {"address": forms.Textarea(attrs={"rows": 3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)


class CadreForm(forms.ModelForm):
    class Meta:
        model = Cadre
        fields = "__all__"
        widgets = {"birth_date": forms.DateInput(attrs={"type": "date"}), "address": forms.Textarea(attrs={"rows": 3}), "notes": forms.Textarea(attrs={"rows": 3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)

    def clean_photo(self):
        file_obj = self.cleaned_data.get("photo")
        validate_image_extension(file_obj)
        return file_obj


class AlumniForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = "__all__"
        widgets = {"address": forms.Textarea(attrs={"rows": 3}), "notes": forms.Textarea(attrs={"rows": 3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)

    def clean_photo(self):
        file_obj = self.cleaned_data.get("photo")
        validate_image_extension(file_obj)
        return file_obj


class CadreLkHistoryForm(forms.ModelForm):
    class Meta:
        model = CadreLkHistory
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)
