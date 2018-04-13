# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-11 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_test', '0009_auto_20180411_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='create_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='derivate_rights',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'allow'), (1, 'not allow')], null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='disable_cause',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='disable_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='download_rights',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'allow'), (1, 'not allow')], null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='share_rights',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'allow'), (1, 'not allow')], null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='status',
            field=models.PositiveIntegerField(choices=[(0, 'to be completed'), (1, 'to be verified'), (2, 'to be published'), (3, 'online'), (4, 'disabled'), (5, 'transcoding'), (6, 'transcode failure')], default=0),
        ),
        migrations.AlterField(
            model_name='video',
            name='is_transcode',
            field=models.PositiveIntegerField(choices=[(0, 'not transcode'), (1, 'transcoded without DRM'), (2, 'transcoded with DRM')], default=0),
        ),
    ]
