from django import forms

from apps.organization.models import ChairmanHistory, ManagementMember, OrganizationProfile

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


class OrganizationProfileForm(forms.ModelForm):
    class Meta:
        model = OrganizationProfile
        fields = "__all__"
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "history": forms.Textarea(attrs={"rows": 5}),
            "vision": forms.Textarea(attrs={"rows": 3}),
            "mission": forms.Textarea(attrs={"rows": 4}),
            "address": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)

    def clean_logo(self):
        file_obj = self.cleaned_data.get("logo")
        validate_image_extension(file_obj)
        return file_obj

    def clean_profile_image(self):
        file_obj = self.cleaned_data.get("profile_image")
        validate_image_extension(file_obj)
        return file_obj


class ManagementMemberForm(forms.ModelForm):
    class Meta:
        model = ManagementMember
        fields = "__all__"
        widgets = {"description": forms.Textarea(attrs={"rows": 3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)

    def clean_photo(self):
        file_obj = self.cleaned_data.get("photo")
        validate_image_extension(file_obj)
        return file_obj


class ChairmanHistoryForm(forms.ModelForm):
    class Meta:
        model = ChairmanHistory
        fields = "__all__"
        widgets = {"description": forms.Textarea(attrs={"rows": 3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)

    def clean_photo(self):
        file_obj = self.cleaned_data.get("photo")
        validate_image_extension(file_obj)
        return file_obj
