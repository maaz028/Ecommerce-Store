# Generated by Django 3.2.5 on 2021-08-05 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_rename_query_contact_query_txt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=11),
        ),
    ]
