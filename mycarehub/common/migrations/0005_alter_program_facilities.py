# Generated by Django 3.2.16 on 2023-01-30 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_program_facilities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='facilities',
            field=models.ManyToManyField(blank=True, related_name='programs', to='common.Facility'),
        ),
    ]
