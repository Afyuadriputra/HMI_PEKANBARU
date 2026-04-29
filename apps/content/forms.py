from django import forms

from apps.content.models import Event, GalleryCategory, GalleryImage, NewsCategory, NewsPost, Program

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


def allow_auto_slug(form):
    if "slug" in form.fields:
        form.fields["slug"].required = False
    return form


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        exclude = ("created_by",)
        widgets = {"description": forms.Textarea(attrs={"rows": 3}), "content": forms.Textarea(attrs={"rows": 6})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        allow_auto_slug(self)
        apply_tailwind(self)

    def clean_image(self):
        file_obj = self.cleaned_data.get("image")
        validate_image_extension(file_obj)
        return file_obj


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ("created_by",)
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
            "content": forms.Textarea(attrs={"rows": 6}),
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
            "start_time": forms.TimeInput(attrs={"type": "time"}),
            "end_time": forms.TimeInput(attrs={"type": "time"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        allow_auto_slug(self)
        apply_tailwind(self)

    def clean_image(self):
        file_obj = self.cleaned_data.get("image")
        validate_image_extension(file_obj)
        return file_obj


class NewsCategoryForm(forms.ModelForm):
    class Meta:
        model = NewsCategory
        fields = "__all__"
        widgets = {"description": forms.Textarea(attrs={"rows": 3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        allow_auto_slug(self)
        apply_tailwind(self)


class NewsPostForm(forms.ModelForm):
    class Meta:
        model = NewsPost
        exclude = ("request", "created_by")
        widgets = {
            "excerpt": forms.Textarea(attrs={"rows": 3}),
            "content": forms.Textarea(attrs={"rows": 8}),
            "published_at": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        allow_auto_slug(self)
        apply_tailwind(self)

    def clean_image(self):
        file_obj = self.cleaned_data.get("image")
        validate_image_extension(file_obj)
        return file_obj


class GalleryCategoryForm(forms.ModelForm):
    class Meta:
        model = GalleryCategory
        fields = "__all__"
        widgets = {"description": forms.Textarea(attrs={"rows": 3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        allow_auto_slug(self)
        apply_tailwind(self)


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        exclude = ("uploaded_by",)
        widgets = {"description": forms.Textarea(attrs={"rows": 3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)

    def clean_image(self):
        file_obj = self.cleaned_data.get("image")
        validate_image_extension(file_obj)
        return file_obj
