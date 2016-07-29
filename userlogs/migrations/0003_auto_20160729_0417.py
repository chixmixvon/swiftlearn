# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 04:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userlogs', '0002_auto_20160728_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recentactivity',
            name='app_label',
        ),
        migrations.RemoveField(
            model_name='recentactivity',
            name='model_name',
        ),
        migrations.RemoveField(
            model_name='recentactivity',
            name='text',
        ),
        migrations.AddField(
            model_name='recentactivity',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 7, 29, 4, 17, 42, 43070, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
