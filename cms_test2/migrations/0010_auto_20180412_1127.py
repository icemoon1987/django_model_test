# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-12 11:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms_test2', '0009_musicinfo_musiclangpack'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('album_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('platform_id', models.PositiveIntegerField(blank=True, choices=[(1, 'Android'), (2, 'IOS'), (3, 'Web')], default=1, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_test2.Category')),
                ('genres', models.ManyToManyField(related_name='_album_genres_+', to='cms_test2.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='AlbumVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.PositiveIntegerField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_test2.Album')),
            ],
        ),
        migrations.AlterField(
            model_name='video',
            name='categories',
            field=models.ManyToManyField(related_name='_video_categories_+', to='cms_test2.Category'),
        ),
        migrations.AlterField(
            model_name='video',
            name='genres',
            field=models.ManyToManyField(related_name='_video_genres_+', to='cms_test2.Genre'),
        ),
        migrations.AddField(
            model_name='albumvideo',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_test2.Video'),
        ),
        migrations.AddField(
            model_name='album',
            name='videos',
            field=models.ManyToManyField(through='cms_test2.AlbumVideo', to='cms_test2.Video'),
        ),
        migrations.AlterUniqueTogether(
            name='albumvideo',
            unique_together=set([('album', 'video')]),
        ),
    ]
