# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-06 19:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_activities', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='activity_periods',
            new_name='activity_period',
        ),
    ]
