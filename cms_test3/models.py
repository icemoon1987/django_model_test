# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.


class Video1(models.Model):

    id = models.CharField(max_length=80, primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.id, self.name)

class Video2(models.Model):

    id = models.CharField(max_length=80, primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.id, self.name)


class Video3(models.Model):

    id = models.CharField(max_length=80, primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.id, self.name)


class BannerTest(models.Model):

    id = models.CharField(max_length=80, primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    content_id = GenericForeignKey(ct_field='content_ct', fk_field='content_fk')
    content_ct = models.ForeignKey(ContentType, null=True, blank=True)
    content_fk = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.id, self.name)


