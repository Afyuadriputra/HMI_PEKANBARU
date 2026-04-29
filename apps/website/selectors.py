from apps.website.models import NavigationMenu, SiteSetting


def site_settings_map():
    return {item.setting_key: item.setting_value for item in SiteSetting.objects.all()}


def site_setting_list():
    return SiteSetting.objects.order_by("setting_key")


def site_setting_get(setting_id):
    return SiteSetting.objects.get(pk=setting_id)


def active_navigation(location=None):
    queryset = NavigationMenu.objects.filter(status=NavigationMenu.STATUS_ACTIVE)
    if location:
        queryset = queryset.filter(location=location)
    return queryset.order_by("sort_order", "title")


def navigation_list():
    return NavigationMenu.objects.order_by("location", "sort_order", "title")


def navigation_get(menu_id):
    return NavigationMenu.objects.get(pk=menu_id)
