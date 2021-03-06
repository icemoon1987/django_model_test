# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-12 07:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms_test', '0013_auto_20180412_0630'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('thumbnail_id', models.AutoField(primary_key=True, serialize=False)),
                ('width', models.PositiveIntegerField()),
                ('height', models.PositiveIntegerField()),
                ('url', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='shortvideolangpack',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='shortvideolangpack',
            name='is_default',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'not default language'), (1, 'is default language')], null=True),
        ),
        migrations.AddField(
            model_name='shortvideolangpack',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_test.Language'),
        ),
        migrations.AddField(
            model_name='shortvideolangpack',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shortvideolangpack',
            name='thumbnails',
            field=models.ManyToManyField(to='cms_test.Thumbnail'),
        ),
    ]
