# Generated by Django 3.2.5 on 2021-07-05 02:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20210705_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 5, 7, 52, 10, 796545)),
        ),
    ]