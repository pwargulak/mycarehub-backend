# Generated by Django 3.2.11 on 2022-03-15 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0027_alter_servicerequest_request_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='ccc_number',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
    ]
