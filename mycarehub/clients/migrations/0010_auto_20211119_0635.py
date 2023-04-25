# Generated by Django 3.2.9 on 2021-11-19 03:35

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import mycarehub.users.models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_auto_20211119_0628'),
        ('clients', '0009_remove_securityquestionresponse_flavour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='addresses',
            field=models.ManyToManyField(blank=True, related_name='client_addresses', to='common.Address'),
        ),
        migrations.AlterField(
            model_name='client',
            name='contacts',
            field=models.ManyToManyField(blank=True, related_name='client_contacts', to='common.Contact'),
        ),
        migrations.AlterField(
            model_name='client',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('en', 'English'), ('sw', 'Swahili')], max_length=150), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='client',
            name='organisation',
            field=models.ForeignKey(default=mycarehub.users.models.default_organisation, on_delete=django.db.models.deletion.PROTECT, related_name='clients_client_related', to='common.organisation'),
        ),
        migrations.AlterField(
            model_name='client',
            name='related_persons',
            field=models.ManyToManyField(blank=True, related_name='client_related_persons', to='clients.RelatedPerson'),
        ),
        migrations.AlterField(
            model_name='clientfacility',
            name='organisation',
            field=models.ForeignKey(default=mycarehub.users.models.default_organisation, on_delete=django.db.models.deletion.PROTECT, related_name='clients_clientfacility_related', to='common.organisation'),
        ),
        migrations.AlterField(
            model_name='identifier',
            name='organisation',
            field=models.ForeignKey(default=mycarehub.users.models.default_organisation, on_delete=django.db.models.deletion.PROTECT, related_name='clients_identifier_related', to='common.organisation'),
        ),
        migrations.AlterField(
            model_name='relatedperson',
            name='addresses',
            field=models.ManyToManyField(related_name='related_person_addresses', to='common.Address'),
        ),
        migrations.AlterField(
            model_name='relatedperson',
            name='contacts',
            field=models.ManyToManyField(related_name='related_person_contacts', to='common.Contact'),
        ),
        migrations.AlterField(
            model_name='relatedperson',
            name='organisation',
            field=models.ForeignKey(default=mycarehub.users.models.default_organisation, on_delete=django.db.models.deletion.PROTECT, related_name='clients_relatedperson_related', to='common.organisation'),
        ),
        migrations.AlterField(
            model_name='securityquestion',
            name='organisation',
            field=models.ForeignKey(default=mycarehub.users.models.default_organisation, on_delete=django.db.models.deletion.PROTECT, related_name='clients_securityquestion_related', to='common.organisation'),
        ),
        migrations.AlterField(
            model_name='securityquestionresponse',
            name='organisation',
            field=models.ForeignKey(default=mycarehub.users.models.default_organisation, on_delete=django.db.models.deletion.PROTECT, related_name='clients_securityquestionresponse_related', to='common.organisation'),
        ),
    ]