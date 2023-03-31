# Generated by Django 3.2.17 on 2023-02-14 11:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_alter_program_facilities'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='content_sequence',
            field=models.CharField(choices=[('GRADUAL', 'Gradual'), ('INSTANT', 'Instant')], default='INSTANT', help_text='How content is served in the program', max_length=16),
        ),
        migrations.AddField(
            model_name='program',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]