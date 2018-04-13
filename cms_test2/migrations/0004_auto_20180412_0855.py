# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-12 08:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms_test2', '0003_auto_20180412_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='audio_language',
            field=models.ManyToManyField(related_name='_video_audio_language_+', to='cms_test2.Language'),
        ),
        migrations.AddField(
            model_name='video',
            name='subtitle_language',
            field=models.ManyToManyField(related_name='_video_subtitle_language_+', to='cms_test2.Language'),
        ),
        migrations.AlterField(
            model_name='video',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='cms_test2.Language'),
        ),
    ]
