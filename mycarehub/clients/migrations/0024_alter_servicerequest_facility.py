# Generated by Django 3.2.9 on 2022-02-08 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0015_faq'),
        ('clients', '0023_alter_servicerequest_facility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='facility',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='common.facility'),
        ),
    ]