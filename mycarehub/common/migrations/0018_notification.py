# Generated by Django 3.2.12 on 2022-04-08 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mycarehub.common.models.base_models
import mycarehub.utils.general_utils
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0017_facility_fhir_organization_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.UUIDField(blank=True, null=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.UUIDField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=32)),
                ('body', models.TextField()),
                ('notification_type', models.CharField(max_length=32)),
                ('flavour', models.CharField(choices=[('PRO', 'PRO'), ('CONSUMER', 'CONSUMER')], max_length=32)),
                ('is_read', models.BooleanField(default=False)),
                ('facility', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.facility')),
                ('organisation', models.ForeignKey(default=mycarehub.utils.general_utils.default_organisation, on_delete=django.db.models.deletion.PROTECT, related_name='common_notification_related', to='common.organisation')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
            },
            managers=[
                ('objects', mycarehub.common.models.base_models.AbstractBaseManager()),
            ],
        ),
    ]
