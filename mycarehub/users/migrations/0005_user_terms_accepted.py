# Generated by Django 3.2.9 on 2021-11-15 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20211112_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='terms_accepted',
            field=models.BooleanField(default=False),
        ),
    ]