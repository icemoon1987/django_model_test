# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-13 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_test2', '0019_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_id',
            field=models.CharField(max_length=81, primary_key=True, serialize=False),
        ),
    ]
