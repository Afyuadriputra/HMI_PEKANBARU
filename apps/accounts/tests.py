from django.contrib.auth import authenticate
from django.test import TestCase

from apps.accounts.forms import UserAdminCreationForm, UserUpdateForm
from apps.accounts.models import Role
from apps.accounts.services import save_user_form


class AccountServiceTests(TestCase):
    def setUp(self):
        self.role = Role.objects.create(name=Role.ADMIN_WEBSITE)

    def test_create_user_hashes_password_and_can_authenticate(self):
        form = UserAdminCreationForm(
            data={
                "email": "website.admin@example.com",
                "name": "Admin Website",
                "phone": "08123456789",
                "role": self.role.id,
                "status": "active",
                "is_staff": "on",
                "password1": "StrongPass123",
                "password2": "StrongPass123",
            }
        )

        self.assertTrue(form.is_valid(), form.errors)
        user = save_user_form(form)

        self.assertNotEqual(user.password, "StrongPass123")
        self.assertTrue(user.check_password("StrongPass123"))
        self.assertEqual(authenticate(email="website.admin@example.com", password="StrongPass123"), user)

    def test_create_user_rejects_mismatched_password_confirmation(self):
        form = UserAdminCreationForm(
            data={
                "email": "website.admin@example.com",
                "name": "Admin Website",
                "role": self.role.id,
                "status": "active",
                "password1": "StrongPass123",
                "password2": "WrongPass123",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)

    def test_update_user_without_new_password_keeps_existing_password(self):
        form = UserAdminCreationForm(
            data={
                "email": "admin@example.com",
                "name": "Admin",
                "role": self.role.id,
                "status": "active",
                "password1": "StrongPass123",
                "password2": "StrongPass123",
            }
        )
        self.assertTrue(form.is_valid(), form.errors)
        user = save_user_form(form)
        old_password_hash = user.password

        update_form = UserUpdateForm(
            data={
                "email": user.email,
                "name": "Admin Updated",
                "phone": "",
                "role": self.role.id,
                "status": "active",
                "password": "",
            },
            instance=user,
        )
        self.assertTrue(update_form.is_valid(), update_form.errors)
        updated_user = save_user_form(update_form)

        self.assertEqual(updated_user.password, old_password_hash)
        self.assertEqual(updated_user.name, "Admin Updated")
