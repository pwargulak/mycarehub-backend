# Generated by Django 3.2.11 on 2022-03-24 06:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mycarehub.common.models.base_models
import mycarehub.utils.general_utils
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0016_auto_20220215_1721'),
        ('staff', '0003_auto_20220215_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.UUIDField(blank=True, null=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.UUIDField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('request_type', models.CharField(choices=[('STAFF_PIN_RESET', 'STAFF_PIN_RESET')], max_length=36)),
                ('request', models.TextField()),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('RESOLVED', 'RESOLVED')], default='PENDING', max_length=36)),
                ('resolved_at', models.DateTimeField(blank=True, null=True)),
                ('meta', models.JSONField(blank=True, null=True)),
                ('organisation', models.ForeignKey(default=mycarehub.utils.general_utils.default_organisation, on_delete=django.db.models.deletion.PROTECT, related_name='staff_servicerequest_related', to='common.organisation')),
                ('resolved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='service_request_resolved_by_admin_staff', to='staff.staff')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='staff.staff')),
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