from apps.organization.models import ChairmanHistory, ManagementMember, OrganizationProfile


def organization_profile():
    return OrganizationProfile.objects.order_by("-updated_at").first()


def organization_profile_list():
    return OrganizationProfile.objects.order_by("-updated_at")


def organization_profile_get(profile_id):
    return OrganizationProfile.objects.get(pk=profile_id)


def active_management_members():
    return ManagementMember.objects.filter(status=ManagementMember.STATUS_ACTIVE).order_by("sort_order", "name")


def management_member_list():
    return ManagementMember.objects.order_by("sort_order", "name")


def management_member_get(member_id):
    return ManagementMember.objects.get(pk=member_id)


def visible_chairmen():
    return ChairmanHistory.objects.filter(status=ChairmanHistory.STATUS_SHOW).order_by("sort_order", "period_start")


def chairman_list():
    return ChairmanHistory.objects.order_by("sort_order", "period_start")


def chairman_get(chairman_id):
    return ChairmanHistory.objects.get(pk=chairman_id)
