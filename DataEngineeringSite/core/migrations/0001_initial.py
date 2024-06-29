# Generated by Django 5.0.6 on 2024-06-25 19:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('sku', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField(default=0)),
                ('location', models.TextField()),
                ('DateAdded', models.DateField(default=datetime.datetime.now)),
                ('DateUpdated', models.DateField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'store_product',
            },
        ),
    ]