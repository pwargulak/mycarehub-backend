# Generated by Django 3.2.12 on 2022-06-30 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0022_alter_facility_county'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='sub_county',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]