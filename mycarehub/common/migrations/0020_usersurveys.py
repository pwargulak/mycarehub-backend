# Generated by Django 3.2.11 on 2022-05-09 13:37

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
        ('common', '0019_alter_notification_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSurveys',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.UUIDField(blank=True, null=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.UUIDField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('survey_link', models.TextField()),
                ('survey_title', models.TextField()),
                ('survey_description', models.TextField(blank=True, null=True)),
                ('has_submitted', models.BooleanField(default=False)),
                ('organisation', models.ForeignKey(default=mycarehub.utils.general_utils.default_organisation, on_delete=django.db.models.deletion.PROTECT, related_name='common_usersurveys_related', to='common.organisation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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