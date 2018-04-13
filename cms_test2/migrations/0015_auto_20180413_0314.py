# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-13 03:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms_test2', '0014_auto_20180412_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistInfo',
            fields=[
                ('artist_info_id', models.AutoField(primary_key=True, serialize=False)),
                ('artist_type', models.PositiveIntegerField(choices=[(0, 'Group'), (1, 'Artist')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ArtistLangPack',
            fields=[
                ('artist_langpack_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_default', models.PositiveIntegerField(choices=[(0, 'not default language'), (1, 'is default language')], default=0)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('icon', models.CharField(blank=True, max_length=300, null=True)),
                ('channel_pic', models.CharField(blank=True, max_length=300, null=True)),
                ('artist_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_test2.ArtistInfo')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_test2.Language')),
            ],
        ),
        migrations.CreateModel(
            name='ShowInfo',
            fields=[
                ('show_info_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ShowLangPack',
            fields=[
                ('show_langpack_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_default', models.PositiveIntegerField(choices=[(0, 'not default language'), (1, 'is default language')], default=0)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('icon', models.CharField(blank=True, max_length=300, null=True)),
                ('channel_pic', models.CharField(blank=True, max_length=300, null=True)),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_test2.Language')),
                ('show_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_test2.ShowInfo')),
            ],
        ),
        migrations.AddField(
            model_name='channel',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_test2.Publisher'),
        ),
        migrations.AddField(
            model_name='channel',
            name='show_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_test2.ShowInfo'),
        ),
    ]