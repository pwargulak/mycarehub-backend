# Generated by Django 3.2.12 on 2022-06-30 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0024_alter_facility_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='name',
            field=models.TextField(unique=True),
        ),
    ]