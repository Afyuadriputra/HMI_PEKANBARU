import uuid

from django.db import migrations, models


def populate_tracking_codes(apps, schema_editor):
    NewsUploadRequest = apps.get_model("news_request", "NewsUploadRequest")
    for news_request in NewsUploadRequest.objects.filter(tracking_code__isnull=True):
        news_request.tracking_code = uuid.uuid4()
        news_request.save(update_fields=["tracking_code"])


class Migration(migrations.Migration):
    dependencies = [
        ("news_request", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="newsuploadrequest",
            name="tracking_code",
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
        migrations.RunPython(populate_tracking_codes, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="newsuploadrequest",
            name="tracking_code",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
