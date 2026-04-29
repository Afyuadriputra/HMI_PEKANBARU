from django.db import transaction


@transaction.atomic
def save_registration_form(form, user=None):
    registration_form = form.save(commit=False)
    if user and not registration_form.created_by_id:
        registration_form.created_by = user
    registration_form.save()
    return registration_form


@transaction.atomic
def delete_instance(instance):
    instance.delete()
