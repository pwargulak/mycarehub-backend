# Generated by Django 3.2.9 on 2021-11-15 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0006_auto_20211110_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_value',
            field=models.TextField(unique=True),
        ),
    ]