# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 15:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emergencies', '0004_auto_20170626_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergency',
            name='status',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='emergencies.Status'),
        ),
    ]
