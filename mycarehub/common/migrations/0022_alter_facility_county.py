# Generated by Django 3.2.12 on 2022-06-30 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0021_auto_20220513_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='county',
            field=models.CharField(blank=True, choices=[('Nairobi', 'Nairobi'), ('Kajiado', 'Kajiado')], max_length=64, null=True),
        ),
    ]