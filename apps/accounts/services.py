from django.db import transaction


@transaction.atomic
def save_user_form(form):
    old_password = None
    if form.instance.pk:
        old_password = type(form.instance).objects.only("password").get(pk=form.instance.pk).password

    user = form.save(commit=False)
    password = form.cleaned_data.get("password1") or form.cleaned_data.get("password")
    if password:
        user.set_password(password)
    elif old_password is not None:
        user.password = old_password
    user.save()
    form.save_m2m()
    return user


@transaction.atomic
def delete_user(user):
    user.delete()
