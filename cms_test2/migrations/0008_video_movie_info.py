# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-12 09:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms_test2', '0007_auto_20180412_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='movie_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_test2.MovieInfo'),
        ),
    ]
