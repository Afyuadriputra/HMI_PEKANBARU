from apps.administration.models import DocumentArchive, IncomingLetter, Invitation, OutgoingLetter


def archive_list():
    return DocumentArchive.objects.select_related("uploaded_by").order_by("-archive_date", "-created_at")


def archive_get(item_id):
    return DocumentArchive.objects.select_related("uploaded_by").get(pk=item_id)


def incoming_letter_list():
    return IncomingLetter.objects.select_related("created_by").order_by("-received_date", "-created_at")


def incoming_letter_get(item_id):
    return IncomingLetter.objects.select_related("created_by").get(pk=item_id)


def outgoing_letter_list():
    return OutgoingLetter.objects.select_related("created_by").order_by("-letter_date", "-created_at")


def outgoing_letter_get(item_id):
    return OutgoingLetter.objects.select_related("created_by").get(pk=item_id)


def invitation_list():
    return Invitation.objects.select_related("event", "created_by").order_by("-invitation_date", "-created_at")


def invitation_get(item_id):
    return Invitation.objects.select_related("event", "created_by").get(pk=item_id)
