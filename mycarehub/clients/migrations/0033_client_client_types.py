# Generated by Django 3.2.11 on 2022-04-25 09:13

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0032_remove_client_client_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_types',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('PMTCT', 'PMTCT'), ('OTZ', 'OTZ'), ('OTZ_PLUS', 'OTZ Plus'), ('HVL', 'HVL'), ('OVC', 'OVC'), ('DREAMS', 'DREAMS'), ('HIGH_RISK', 'High Risk Clients'), ('SPOUSES', 'SPOUSES'), ('YOUTH', 'Youth'), ('KenyaEMR', 'Kenya EMR')], max_length=64), blank=True, default=list, size=None),
        ),
    ]