# Generated by Django 3.0.8 on 2020-08-20 19:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_order_order_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 21, 0, 33, 39, 782313)),
        ),
    ]