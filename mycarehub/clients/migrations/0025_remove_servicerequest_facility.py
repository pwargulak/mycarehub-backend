# Generated by Django 3.2.9 on 2022-02-08 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0024_alter_servicerequest_facility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicerequest',
            name='facility',
        ),
    ]