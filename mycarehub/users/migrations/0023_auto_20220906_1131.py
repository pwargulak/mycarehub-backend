# Generated by Django 3.2.14 on 2022-09-06 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_user_has_set_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userotp',
            name='user',
        ),
        migrations.AlterIndexTogether(
            name='userpin',
            index_together=None,
        ),
        migrations.RemoveField(
            model_name='userpin',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='accepted_terms_of_service',
        ),
        migrations.DeleteModel(
            name='TermsOfService',
        ),
        migrations.DeleteModel(
            name='UserOTP',
        ),
        migrations.DeleteModel(
            name='UserPIN',
        ),
    ]