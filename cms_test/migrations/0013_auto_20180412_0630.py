# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-12 06:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_test', '0012_auto_20180412_0626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shortvideoinfo',
            old_name='relation_id',
            new_name='relation_video',
        ),
    ]
