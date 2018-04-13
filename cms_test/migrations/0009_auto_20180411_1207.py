# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-11 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_test', '0008_auto_20180411_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='duration',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='is_transcode',
            field=models.IntegerField(choices=[(0, 'not transcode'), (1, 'transcoded without DRM'), (2, 'transcoded with DRM')], default=0),
        ),
        migrations.AddField(
            model_name='video',
            name='publish_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='release_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='src_url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='video_hash',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
