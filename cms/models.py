# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Video(models.Model):

    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.id


class Album(models.Model):

    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=1000)
    videos = models.ManyToManyField(Video, through='VideoAlbum')

    def __str__(self):
        return self.id


class VideoAlbum(models.Model):

    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    rank = models.IntegerField()

    class Meta:
        unique_together=("video","album")

