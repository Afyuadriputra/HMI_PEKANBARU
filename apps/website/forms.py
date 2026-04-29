from django import forms

from apps.website.models import NavigationMenu, SiteSetting

TAILWIND_INPUT = "w-full rounded border border-slate-300 px-3 py-2 text-sm"


def apply_tailwind(form):
    for field in form.fields.values():
        field.widget.attrs["class"] = f"{field.widget.attrs.get('class', '')} {TAILWIND_INPUT}".strip()
    return form


class SiteSettingForm(forms.ModelForm):
    class Meta:
        model = SiteSetting
        fields = ("setting_key", "setting_value")
        widgets = {"setting_value": forms.Textarea(attrs={"rows": 4})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)


class NavigationMenuForm(forms.ModelForm):
    class Meta:
        model = NavigationMenu
        fields = ("title", "url", "location", "sort_order", "status")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)
