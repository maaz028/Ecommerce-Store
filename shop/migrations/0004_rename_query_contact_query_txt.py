# Generated by Django 3.2.5 on 2021-08-05 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='query',
            new_name='query_txt',
        ),
    ]
