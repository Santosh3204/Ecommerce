# Generated by Django 3.0.5 on 2020-08-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.IntegerField()),
                ('product_order_date', models.DateField(auto_now=True)),
                ('product_quantity', models.PositiveIntegerField()),
            ],
        ),
    ]