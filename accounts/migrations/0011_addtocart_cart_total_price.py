# Generated by Django 3.0.5 on 2020-08-12 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200812_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtocart',
            name='cart_total_price',
            field=models.IntegerField(default=None),
        ),
    ]
