# Generated by Django 3.2.9 on 2021-12-07 11:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mycarehub.common.models.base_models
import mycarehub.users.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0014_facility_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.UUIDField(blank=True, null=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.UUIDField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('title', models.TextField(unique=True)),
                ('description', models.TextField(blank=True, null=True, unique=True)),
                ('body', models.TextField(unique=True)),
                ('flavour', models.CharField(blank=True, choices=[('PRO', 'PRO'), ('CONSUMER', 'CONSUMER')], max_length=32, null=True)),
                ('organisation', models.ForeignKey(default=mycarehub.users.models.default_organisation, on_delete=django.db.models.deletion.PROTECT, related_name='common_faq_related', to='common.organisation')),
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