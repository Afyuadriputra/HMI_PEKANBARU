import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactMessage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("sender_name", models.CharField(max_length=150)),
                ("sender_email", models.EmailField(max_length=150)),
                ("sender_phone", models.CharField(blank=True, max_length=50)),
                ("subject", models.CharField(max_length=200)),
                ("message", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[("unread", "Unread"), ("read", "Read"), ("replied", "Replied")],
                        default="unread",
                        max_length=20,
                    ),
                ),
                (
                    "handled_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="handled_contact_messages",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "contact_messages",
                "ordering": ["-created_at"],
            },
        ),
    ]
