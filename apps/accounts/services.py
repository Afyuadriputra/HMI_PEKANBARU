from django.db import transaction


@transaction.atomic
def save_user_form(form):
    user = form.save(commit=False)
    password = form.cleaned_data.get("password1") or form.cleaned_data.get("password")
    if password:
        user.set_password(password)
    user.save()
    form.save_m2m()
    return user


@transaction.atomic
def delete_user(user):
    user.delete()
