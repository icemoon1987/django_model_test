# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-13 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_test2', '0018_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('card_id', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('card_name', models.CharField(max_length=100)),
                ('recall_type', models.PositiveIntegerField(choices=[(1, 'Title'), (2, 'Label')], default=0)),
                ('status', models.PositiveIntegerField(choices=[(0, 'Offline'), (1, 'Online')], default=0)),
            ],
        ),
    ]
