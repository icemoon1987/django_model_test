# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-12 09:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms_test2', '0004_auto_20180412_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('actor_id', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('actor_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Composer',
            fields=[
                ('composer_id', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('composer_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('director_id', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('director_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EpisodeInfo',
            fields=[
                ('episode_info_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='EpisodeLangPack',
            fields=[
                ('episode_langpack_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_default', models.PositiveIntegerField(blank=True, choices=[(0, 'not default language'), (1, 'is default language')], null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('episode_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_test2.EpisodeInfo')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_test2.Language')),
                ('thumbnails', models.ManyToManyField(to='cms_test2.Thumbnail')),
            ],
        ),
        migrations.CreateModel(
            name='Lyricist',
            fields=[
                ('lyricist_id', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('lyricist_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RecordLabel',
            fields=[
                ('recordlabel_id', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('recordlabel_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='shortvideolangpack',
            old_name='short_video_lang_pack_id',
            new_name='short_video_langpack_id',
        ),
    ]
