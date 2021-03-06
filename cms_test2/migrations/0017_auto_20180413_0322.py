# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-13 03:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms_test2', '0016_channel_artist_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('playlist_id', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('playlist_name', models.CharField(max_length=100)),
                ('playlist_cover', models.CharField(blank=True, max_length=300, null=True)),
                ('platform_id', models.PositiveIntegerField(blank=True, choices=[(1, 'Android'), (2, 'IOS'), (3, 'Web')], default=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlaylistVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.PositiveIntegerField()),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_test2.Playlist')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_test2.Video')),
            ],
        ),
        migrations.AddField(
            model_name='playlist',
            name='videos',
            field=models.ManyToManyField(through='cms_test2.PlaylistVideo', to='cms_test2.Video'),
        ),
        migrations.AlterUniqueTogether(
            name='playlistvideo',
            unique_together=set([('playlist', 'video')]),
        ),
    ]
