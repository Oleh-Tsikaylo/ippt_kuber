# Generated by Django 3.2.2 on 2021-06-15 12:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 15, 15, 11, 4, 492964)),
        ),
    ]
