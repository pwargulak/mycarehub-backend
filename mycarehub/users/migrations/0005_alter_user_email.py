# Generated by Django 3.2.5 on 2021-07-21 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='noemail@savannahghi.org', max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
