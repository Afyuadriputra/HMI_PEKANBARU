from apps.accounts.models import Role


def user_has_role(user, role_name):
    if not getattr(user, "is_authenticated", False):
        return False

    if getattr(user, "is_superuser", False):
        return True

    role = getattr(user, "role", None)
    return bool(role and role.name == role_name)


def is_super_admin(user):
    return user_has_role(user, Role.SUPER_ADMIN)


def is_admin_website(user):
    return user_has_role(user, Role.ADMIN_WEBSITE)


def is_admin_administrasi(user):
    return user_has_role(user, Role.ADMIN_ADMINISTRATION)
