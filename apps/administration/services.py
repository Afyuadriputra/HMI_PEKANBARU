from django.db import transaction


@transaction.atomic
def save_model_form(form, user=None):
    instance = form.save(commit=False)
    if hasattr(instance, "created_by_id") and user and not instance.created_by_id:
        instance.created_by = user
    if hasattr(instance, "uploaded_by_id") and user and not instance.uploaded_by_id:
        instance.uploaded_by = user
    instance.save()
    form.save_m2m()
    return instance


@transaction.atomic
def delete_instance(instance):
    instance.delete()
