# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-27 17:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_auto_20171127_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='my_date_field',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
