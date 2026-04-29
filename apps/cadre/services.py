from django.db import transaction


@transaction.atomic
def save_model_form(form):
    return form.save()


@transaction.atomic
def delete_instance(instance):
    instance.delete()
