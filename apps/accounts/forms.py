from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, ReadOnlyPasswordHashField

User = get_user_model()

TAILWIND_INPUT = "w-full rounded border border-slate-300 px-3 py-2 text-sm"


def apply_tailwind(form):
    for field in form.fields.values():
        css = field.widget.attrs.get("class", "")
        field.widget.attrs["class"] = f"{css} {TAILWIND_INPUT}".strip()
    return form


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)


class UserAdminForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label="Password")

    class Meta:
        model = User
        fields = ("email", "name", "phone", "photo", "role", "status", "is_staff", "is_superuser", "password")


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Konfirmasi Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email", "name", "phone", "photo", "role", "status", "is_staff", "is_superuser")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password tidak sama.")
        return password2


class UserUpdateForm(forms.ModelForm):
    password = forms.CharField(label="Password baru", widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ("email", "name", "phone", "photo", "role", "status", "is_staff", "is_superuser", "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_tailwind(self)
