# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emergencies', '0005_emergency_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergencyimage',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
