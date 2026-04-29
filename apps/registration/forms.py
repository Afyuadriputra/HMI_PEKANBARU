from django import forms

from apps.registration.models import RegistrationForm

TAILWIND_INPUT = "w-full rounded border border-slate-300 px-3 py-2 text-sm"


class RegistrationFormForm(forms.ModelForm):
    class Meta:
        model = RegistrationForm
        exclude = ("created_by",)
        widgets = {"description": forms.Textarea(attrs={"rows": 3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = f"{field.widget.attrs.get('class', '')} {TAILWIND_INPUT}".strip()
