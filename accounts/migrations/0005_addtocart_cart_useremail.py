# Generated by Django 3.0.8 on 2020-08-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_addtocart'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtocart',
            name='cart_useremail',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]