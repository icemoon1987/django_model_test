# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):

    category_id = models.CharField(max_length=80, primary_key=True)
    category_name = models.CharField(max_length=100, null=False, blank=False)
    level = models.PositiveIntegerField(null=False, blank=False)
    father = models.ForeignKey("self", on_delete=models.PROTECT)

    def __str__(self):
        return "%s %s" % (self.category_id, self.category_name)


class Publisher(models.Model):

    publisher_id = models.CharField(max_length=80, primary_key=True)
    publisher_name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=1000, null=True, blank=True)
    poster = models.CharField(max_length=300, null=True, blank=True)
    icon = models.CharField(max_length=300, null=True, blank=True)
    

    def __str__(self):
        return "%s %s" % (self.publisher_id, self.publisher_name)


class Language(models.Model):

    language_id = models.CharField(max_length=80, primary_key=True)
    language_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.language_id, self.language_name)


class Genre(models.Model):

    genre_id = models.CharField(max_length=80, primary_key=True)
    genre_name = models.CharField(max_length=100, null=False, blank=False)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)
    level = models.PositiveIntegerField()
    father = models.ForeignKey("self", on_delete=models.PROTECT)

    def __str__(self):
        return "%s %s" % (self.genre_id, self.genre_name)


class Channel(models.Model):

    channel_id = models.CharField(max_length=80, primary_key=True)
    channel_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.channel_id, self.channel_name)


class Thumbnail(models.Model):

    thumbnail_id = models.AutoField(primary_key=True)
    width = models.PositiveIntegerField(null=False, blank=False)
    height = models.PositiveIntegerField(null=False, blank=False)
    url = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return "%s" % (self.thumbnail_id)


class ShortVideoInfo(models.Model):

    RELATION_TYPE = (
        (0, "tv show clip"),
        (1, "tv show trailer"),
        (2, "movie clip"),
        (3, "movie trailer"),
    )

    short_video_info_id = models.AutoField(primary_key=True)
    relation_type = models.PositiveIntegerField(choices=RELATION_TYPE, null=True, blank=True)
    relation_video = models.ForeignKey("Video", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "%s" % (self.short_video_info_id)


class ShortVideoLangPack(models.Model):

    short_video_lang_pack_id = models.AutoField(primary_key=True)
    short_video_info = models.ForeignKey("ShortVideoInfo", on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey("Language", on_delete=models.SET_NULL, null=True, blank=True)

    is_default = models.PositiveIntegerField(
        choices=(
            (0, "not default language"),
            (1, "is default language"),
        ),
        null=True, blank=True
    )

    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    thumbnails = models.ManyToManyField("Thumbnail")

    def __str__(self):
        return "%s %s" % (self.short_video_info_id, self.title)
    

class Video(models.Model):

    TRANSCODE_STATUS = (
        (0, "not transcode"),
        (1, "transcoded without DRM"),
        (2, "transcoded with DRM"),
    )

    VIDEO_STATUS = (
        (0, "to be completed"),
        (1, "to be verified"),
        (2, "to be published"),
        (3, "online"),
        (4, "disabled"),
        (5, "transcoding"),
        (6, "transcode failure"),
    )

    ALLOW_STATUS = (
        (0, "allow"),
        (1, "not allow")
    )

    video_id = models.CharField(max_length=100, primary_key=True)

    categories = models.ManyToManyField("Category", through="VideoCategory")
    publisher = models.ForeignKey("Publisher", on_delete=models.SET_NULL, null=True, blank=True)
    genres = models.ManyToManyField("Genre", through="VideoGenre")
    language = models.ForeignKey("Language", on_delete=models.SET_NULL, null=True, blank=True)
    #audio_language = models.ManyToManyField("Language", through="VideoAudioLanguage")

    duration = models.PositiveIntegerField(null=True, blank=True)
    src_url = models.CharField(max_length=300, null=True, blank=True)
    video_hash = models.CharField(max_length=80, null=True, blank=True)
    is_transcode = models.PositiveIntegerField(choices=TRANSCODE_STATUS, default=0, null=False, blank=False)

    release_date = models.DateTimeField(null=True, blank=True)
    publish_time = models.DateTimeField(null=True, blank=True)
    disable_time = models.DateTimeField(null=True, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    
    disable_cause = models.CharField(max_length=200, null=True, blank=True)

    status = models.PositiveIntegerField(choices=VIDEO_STATUS, default=0, null=False, blank=False)

    download_rights = models.PositiveIntegerField(choices=ALLOW_STATUS, null=True, blank=True)
    share_rights = models.PositiveIntegerField(choices=ALLOW_STATUS, null=True, blank=True)
    derivate_rights = models.PositiveIntegerField(choices=ALLOW_STATUS, null=True, blank=True)

    short_video_info = models.OneToOneField("ShortVideoInfo", on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return "%s, %s" % (self.video_id, self.video_name)



class VideoCategory(models.Model):

    video = models.ForeignKey("Video", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    class Meta:
        unique_together=("video", "category")


class VideoGenre(models.Model):

    video = models.ForeignKey("Video", on_delete=models.CASCADE)
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)

    class Meta:
        unique_together=("video", "genre")




