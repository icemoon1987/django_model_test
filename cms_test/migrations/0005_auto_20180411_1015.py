# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-11 10:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms_test', '0004_auto_20180411_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('publisher_id', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('publisher_name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('poster', models.CharField(blank=True, max_length=300, null=True)),
                ('icon', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='category',
            old_name='id',
            new_name='category_id',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category_name',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='id',
            new_name='video_id',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='name',
            new_name='video_name',
        ),
        migrations.RenameField(
            model_name='videocategory',
            old_name='category',
            new_name='category_id',
        ),
        migrations.RenameField(
            model_name='videocategory',
            old_name='video',
            new_name='video_id',
        ),
        migrations.AlterUniqueTogether(
            name='videocategory',
            unique_together=set([('video_id', 'category_id')]),
        ),
        migrations.AddField(
            model_name='video',
            name='publisher_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_test.Publisher'),
        ),
    ]
