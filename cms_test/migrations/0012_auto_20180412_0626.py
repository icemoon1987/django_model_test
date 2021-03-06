# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-12 06:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms_test', '0011_channel_shortvideoinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortVideoLangPack',
            fields=[
                ('short_video_lang_pack_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='video',
            name='video_name',
        ),
        migrations.AddField(
            model_name='shortvideoinfo',
            name='relation_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_test.Video'),
        ),
        migrations.AddField(
            model_name='shortvideoinfo',
            name='relation_type',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'tv show clip'), (1, 'tv show trailer'), (2, 'movie clip'), (3, 'movie trailer')], null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='short_video_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_test.ShortVideoInfo'),
        ),
        migrations.AddField(
            model_name='shortvideolangpack',
            name='short_video_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_test.ShortVideoInfo'),
        ),
    ]
