from apps.registration.models import RegistrationForm


def active_registration_forms():
    return RegistrationForm.objects.select_related("created_by").filter(status=RegistrationForm.STATUS_ACTIVE).order_by("title")


def registration_form_list():
    return RegistrationForm.objects.select_related("created_by").order_by("title")


def registration_form_get(form_id):
    return RegistrationForm.objects.select_related("created_by").get(pk=form_id)
