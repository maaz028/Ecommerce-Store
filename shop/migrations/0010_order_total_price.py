# Generated by Django 3.2.5 on 2021-08-09 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_update_order_timestamps'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.CharField(default='', max_length=100),
        ),
    ]
