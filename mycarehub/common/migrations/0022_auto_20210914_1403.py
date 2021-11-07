# Generated by Django 3.2.6 on 2021-09-14 11:03

from django.db import migrations
import mycarehub.common.models.base_models
import mycarehub.common.models.common_models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0021_auto_20210911_1724'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='facility',
            managers=[
                ('objects', mycarehub.common.models.common_models.FacilityManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='facilityattachment',
            managers=[
                ('objects', mycarehub.common.models.base_models.AbstractBaseManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='facilityuser',
            managers=[
                ('objects', mycarehub.common.models.base_models.AbstractBaseManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='system',
            managers=[
                ('objects', mycarehub.common.models.base_models.AbstractBaseManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='userfacilityallotment',
            managers=[
                ('objects', mycarehub.common.models.base_models.AbstractBaseManager()),
            ],
        ),
    ]
