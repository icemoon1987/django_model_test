# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-12 12:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms_test2', '0013_auto_20180412_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.PositiveIntegerField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_test2.Album')),
            ],
        ),
        migrations.RemoveField(
            model_name='channel',
            name='channel_name',
        ),
        migrations.AddField(
            model_name='channel',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_test2.Category'),
        ),
        migrations.AddField(
            model_name='channel',
            name='genres',
            field=models.ManyToManyField(to='cms_test2.Genre'),
        ),
        migrations.AddField(
            model_name='channel',
            name='is_end',
            field=models.PositiveIntegerField(choices=[(0, 'not end'), (1, 'end')], default=0),
        ),
        migrations.AddField(
            model_name='channel',
            name='platform_id',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Android'), (2, 'IOS'), (3, 'Web')], default=1, null=True),
        ),
        migrations.AddField(
            model_name='channel',
            name='status',
            field=models.PositiveIntegerField(choices=[(0, 'Offline'), (1, 'Online')], default=0),
        ),
        migrations.AlterField(
            model_name='channel',
            name='channel_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='channelalbum',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_test2.Channel'),
        ),
        migrations.AddField(
            model_name='channel',
            name='albums',
            field=models.ManyToManyField(through='cms_test2.ChannelAlbum', to='cms_test2.Album'),
        ),
        migrations.AlterUniqueTogether(
            name='channelalbum',
            unique_together=set([('channel', 'album')]),
        ),
    ]
