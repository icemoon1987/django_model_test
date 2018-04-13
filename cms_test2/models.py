# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from gm2m import GM2MField

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

ID_LENGTH_MAX = 80
NAME_LENGTH_MAX = 100
DESCRIPTION_LENGTH_MAX = 1000
URL_LENGTH_MAX = 300


class Category(models.Model):

    category_id = models.CharField(max_length=ID_LENGTH_MAX, primary_key=True)
    category_name = models.CharField(max_length=NAME_LENGTH_MAX, null=False, blank=False)
    level = models.PositiveIntegerField(null=False, blank=False)
    father = models.ForeignKey("self", on_delete=models.PROTECT)

    def __str__(self):
        return "%s %s" % (self.category_id, self.category_name)


class Director(models.Model):

    director_id = models.CharField(max_length=ID_LENGTH_MAX, primary_key=True)
    director_name = models.CharField(max_length=NAME_LENGTH_MAX, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.director_id, self.director_name)


class Actor(models.Model):

    actor_id = models.CharField(max_length=ID_LENGTH_MAX, primary_key=True)
    actor_name = models.CharField(max_length=NAME_LENGTH_MAX, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.director_id, self.director_name)


class Composer(models.Model):

    composer_id = models.CharField(max_length=ID_LENGTH_MAX, primary_key=True)
    composer_name = models.CharField(max_length=NAME_LENGTH_MAX, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.composer_id, self.composer_name)


class Lyricist(models.Model):

    lyricist_id = models.CharField(max_length=ID_LENGTH_MAX, primary_key=True)
    lyricist_name = models.CharField(max_length=NAME_LENGTH_MAX, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.lyricist_id, self.lyricist_name)


class RecordLabel(models.Model):

    recordlabel_id = models.CharField(max_length=ID_LENGTH_MAX, primary_key=True)
    recordlabel_name = models.CharField(max_length=NAME_LENGTH_MAX, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.recordlabel_id, self.recordlabel_name)


class Publisher(models.Model):

    publisher_id = models.CharField(max_length=ID_LENGTH_MAX, primary_key=True)
    publisher_name = models.CharField(max_length=NAME_LENGTH_MAX, null=False, blank=False)
    description = models.CharField(max_length=DESCRIPTION_LENGTH_MAX, null=True, blank=True)
    poster = models.CharField(max_length=URL_LENGTH_MAX, null=True, blank=True)
    icon = models.CharField(max_length=URL_LENGTH_MAX, null=True, blank=True)
    

    def __str__(self):
        return "%s %s" % (self.publisher_id, self.publisher_name)


class Language(models.Model):

    language_id = models.CharField(max_length=ID_LENGTH_MAX, primary_key=True)
    language_name = models.CharField(max_length=NAME_LENGTH_MAX, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.language_id, self.language_name)


class Genre(models.Model):

    genre_id = models.CharField(max_length=ID_LENGTH_MAX, primary_key=True)
    genre_name = models.CharField(max_length=NAME_LENGTH_MAX, null=False, blank=False)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)
    level = models.PositiveIntegerField()
    father = models.ForeignKey("self", on_delete=models.PROTECT)

    def __str__(self):
        return "%s %s" % (self.genre_id, self.genre_name)


class Thumbnail(models.Model):

    thumbnail_id = models.AutoField(primary_key=True)
    width = models.PositiveIntegerField(null=False, blank=False)
    height = models.PositiveIntegerField(null=False, blank=False)
    url = models.CharField(max_length=URL_LENGTH_MAX, null=True, blank=True)

    def __str__(self):
        return "%s" % (self.thumbnail_id)


class MusicAlbumInfo(models.Model):

    musicalbum_info_id = models.AutoField(primary_key=True)

    def __str__(self):
        return "%s" % (self.musicalbum_info_id)


class MusicAlbumLangPack(models.Model):

    musicalbum_langpack_id = models.AutoField(primary_key=True)
    musicalbum_info = models.ForeignKey("MusicAlbumInfo", on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey("Language", on_delete=models.SET_NULL, null=True, blank=True)

    is_default = models.PositiveIntegerField(
        choices=(
            (0, "not default language"),
            (1, "is default language"),
        ),
        default=0, null=False, blank=False
    )

    title = models.CharField(max_length=NAME_LENGTH_MAX, null=True, blank=True)
    description = models.CharField(max_length=DESCRIPTION_LENGTH_MAX, null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.musicalbum_info_id, self.title)


class SequelInfo(models.Model):

    sequel_info_id = models.AutoField(primary_key=True)

    def __str__(self):
        return "%s" % (self.sequel_info_id)


class SequelLangPack(models.Model):

    sequel_langpack_id = models.AutoField(primary_key=True)
    sequel_info = models.ForeignKey("SequelInfo", on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey("Language", on_delete=models.SET_NULL, null=True, blank=True)

    is_default = models.PositiveIntegerField(
        choices=(
            (0, "not default language"),
            (1, "is default language"),
        ),
        default=0, null=False, blank=False
    )

    title = models.CharField(max_length=NAME_LENGTH_MAX, null=True, blank=True)
    description = models.CharField(max_length=DESCRIPTION_LENGTH_MAX, null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.sequel_info_id, self.title)


class ArtistInfo(models.Model):

    ARTIST_TYPE = (
        (0, "Group"),
        (1, "Artist"),
    )

    artist_info_id = models.AutoField(primary_key=True)

    artist_type = models.PositiveIntegerField(choices=ARTIST_TYPE, default=1, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.artist_info_id, self.artist_type)


class ArtistLangPack(models.Model):

    artist_langpack_id = models.AutoField(primary_key=True)
    artist_info = models.ForeignKey("artistInfo", on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey("Language", on_delete=models.SET_NULL, null=True, blank=True)

    is_default = models.PositiveIntegerField(
        choices=(
            (0, "not default language"),
            (1, "is default language"),
        ),
        default=0, null=False, blank=False
    )

    title = models.CharField(max_length=NAME_LENGTH_MAX, null=True, blank=True)
    description = models.CharField(max_length=DESCRIPTION_LENGTH_MAX, null=True, blank=True)
    icon = models.CharField(max_length=URL_LENGTH_MAX, null=True, blank=True)
    channel_pic = models.CharField(max_length=URL_LENGTH_MAX, null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.artist_info_id, self.title)


class ShowInfo(models.Model):

    show_info_id = models.AutoField(primary_key=True)

    def __str__(self):
        return "%s" % (self.show_info_id)


class ShowLangPack(models.Model):

    show_langpack_id = models.AutoField(primary_key=True)
    show_info = models.ForeignKey("ShowInfo", on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey("Language", on_delete=models.SET_NULL, null=True, blank=True)

    is_default = models.PositiveIntegerField(
        choices=(
            (0, "not default language"),
            (1, "is default language"),
        ),
        default=0, null=False, blank=False
    )

    title = models.CharField(max_length=NAME_LENGTH_MAX, null=True, blank=True)
    description = models.CharField(max_length=DESCRIPTION_LENGTH_MAX, null=True, blank=True)
    icon = models.CharField(max_length=URL_LENGTH_MAX, null=True, blank=True)
    channel_pic = models.CharField(max_length=URL_LENGTH_MAX, null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.show_info_id, self.title)


class SeasonInfo(models.Model):

    season_info_id = models.AutoField(primary_key=True)

    def __str__(self):
        return "%s" % (self.season_info_id)


class SeasonLangPack(models.Model):

    season_langpack_id = models.AutoField(primary_key=True)
    season_info = models.ForeignKey("SeasonInfo", on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey("Language", on_delete=models.SET_NULL, null=True, blank=True)

    is_default = models.PositiveIntegerField(
        choices=(
            (0, "not default language"),
            (1, "is default language"),
        ),
        default=0, null=False, blank=False
    )

    title = models.CharField(max_length=NAME_LENGTH_MAX, null=True, blank=True)
    description = models.CharField(max_length=DESCRIPTION_LENGTH_MAX, null=True, blank=True)
    icon = models.CharField(max_length=URL_LENGTH_MAX, null=True, blank=True)
    album_pic = models.CharField(max_length=URL_LENGTH_MAX, null=True, blank=True)
    directors = models.ManyToManyField("Director")
    actors = models.ManyToManyField("Actor")

    def __str__(self):
        return "%s %s" % (self.season_info_id, self.title)


class MusicInfo(models.Model):

    music_info_id = models.AutoField(primary_key=True)

    def __str__(self):
        return "%s" % (self.music_info_id)


class MusicLangPack(models.Model):

    music_langpack_id = models.AutoField(primary_key=True)
    music_info = models.ForeignKey("MusicInfo", on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey("Language", on_delete=models.SET_NULL, null=True, blank=True)

    is_default = models.PositiveIntegerField(
        choices=(
            (0, "not default language"),
            (1, "is default language"),
        ),
        default=0, null=False, blank=False
    )

    title = models.CharField(max_length=NAME_LENGTH_MAX, null=True, blank=True)
    description = models.CharField(max_length=DESCRIPTION_LENGTH_MAX, null=True, blank=True)
    thumbnails = models.ManyToManyField("Thumbnail")
    composers = models.ManyToManyField("Composer")
    lyricists = models.ManyToManyField("Lyricist")
    recordlabels = models.ManyToManyField("RecordLabel")

    def __str__(self):
        return "%s %s" % (self.music_info_id, self.title)


class MovieInfo(models.Model):

    movie_info_id = models.AutoField(primary_key=True)

    def __str__(self):
        return "%s" % (self.movie_info_id)


class MovieLangPack(models.Model):

    movie_langpack_id = models.AutoField(primary_key=True)
    movie_info = models.ForeignKey("MovieInfo", on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey("Language", on_delete=models.SET_NULL, null=True, blank=True)

    is_default = models.PositiveIntegerField(
        choices=(
            (0, "not default language"),
            (1, "is default language"),
        ),
        default=0, null=False, blank=False
    )

    title = models.CharField(max_length=NAME_LENGTH_MAX, null=True, blank=True)
    description = models.CharField(max_length=DESCRIPTION_LENGTH_MAX, null=True, blank=True)
    thumbnails = models.ManyToManyField("Thumbnail")
    directors = models.ManyToManyField("Director")
    actors = models.ManyToManyField("Actor")

    def __str__(self):
        return "%s %s" % (self.movie_info_id, self.title)


class EpisodeInfo(models.Model):

    episode_info_id = models.AutoField(primary_key=True)

    def __str__(self):
        return "%s" % (self.episode_info_id)


class EpisodeLangPack(models.Model):

    episode_langpack_id = models.AutoField(primary_key=True)
    episode_info = models.ForeignKey("EpisodeInfo", on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey("Language", on_delete=models.SET_NULL, null=True, blank=True)

    is_default = models.PositiveIntegerField(
        choices=(
            (0, "not default language"),
            (1, "is default language"),
        ),
        default=0, null=False, blank=False
    )

    title = models.CharField(max_length=NAME_LENGTH_MAX, null=True, blank=True)
    description = models.CharField(max_length=DESCRIPTION_LENGTH_MAX, null=True, blank=True)
    thumbnails = models.ManyToManyField("Thumbnail")
    directors = models.ManyToManyField("Director")
    actors = models.ManyToManyField("Actor")

    def __str__(self):
        return "%s %s" % (self.episode_info_id, self.title)


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

    short_video_langpack_id = models.AutoField(primary_key=True)
    short_video_info = models.ForeignKey("ShortVideoInfo", on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey("Language", on_delete=models.SET_NULL, null=True, blank=True)

    is_default = models.PositiveIntegerField(
        choices=(
            (0, "not default language"),
            (1, "is default language"),
        ),
        default=0, null=False, blank=False
    )

    title = models.CharField(max_length=NAME_LENGTH_MAX, null=True, blank=True)
    description = models.CharField(max_length=DESCRIPTION_LENGTH_MAX, null=True, blank=True)
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

    video_id = models.CharField(max_length=NAME_LENGTH_MAX, primary_key=True)

    categories = models.ManyToManyField("Category")
    publisher = models.ForeignKey("Publisher", on_delete=models.SET_NULL, null=True, blank=True)
    genres = models.ManyToManyField("Genre")
    language = models.ForeignKey("Language", related_name="+", on_delete=models.SET_NULL, null=True, blank=True)
    audio_language = models.ManyToManyField("Language", related_name="+")
    subtitle_language = models.ManyToManyField("Language", related_name="+")

    duration = models.PositiveIntegerField(null=True, blank=True)
    src_url = models.CharField(max_length=URL_LENGTH_MAX, null=True, blank=True)
    video_hash = models.CharField(max_length=ID_LENGTH_MAX, null=True, blank=True)
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
    episode_info = models.OneToOneField("EpisodeInfo", on_delete=models.SET_NULL, null=True, blank=True)
    movie_info = models.OneToOneField("MovieInfo", on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return "%s, %s" % (self.video_id, self.video_name)


class Album(models.Model):

    PLATFORM = (
        (1, "Android"),
        (2, "IOS"),
        (3, "Web"),
    )

    STATUS = (
        (0, "Offline"),
        (1, "Online"),
    )

    END_STATUS = (
        (0, "not end"),
        (1, "end"),
    )

    album_id = models.CharField(max_length=NAME_LENGTH_MAX, primary_key=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)
    platform_id = models.PositiveIntegerField(choices=PLATFORM, default=1, null=True, blank=True)
    genres = models.ManyToManyField("Genre")
    videos = models.ManyToManyField("Video", through="AlbumVideo")
    status = models.PositiveIntegerField(choices=STATUS, default=0, null=False, blank=False)
    is_end = models.PositiveIntegerField(choices=END_STATUS, default=0, null=False, blank=False)

    season_info = models.OneToOneField("SeasonInfo", on_delete=models.SET_NULL, null=True, blank=True)
    sequel_info = models.OneToOneField("SequelInfo", on_delete=models.SET_NULL, null=True, blank=True)
    musicalbum_info = models.OneToOneField("MusicAlbumInfo", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "%s" % (self.album_id)


class AlbumVideo(models.Model):

    album = models.ForeignKey("Album", on_delete=models.CASCADE)
    video = models.ForeignKey("Video", on_delete=models.CASCADE)

    rank = models.PositiveIntegerField(null=False, blank=False)

    class Meta:
        unique_together=("album", "video")

    def __str__(self):
        return "%s, %s" % (self.album, self.video)



class Channel(models.Model):

    PLATFORM = (
        (1, "Android"),
        (2, "IOS"),
        (3, "Web"),
    )

    STATUS = (
        (0, "Offline"),
        (1, "Online"),
    )

    END_STATUS = (
        (0, "not end"),
        (1, "end"),
    )

    channel_id = models.CharField(max_length=NAME_LENGTH_MAX, primary_key=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)
    platform_id = models.PositiveIntegerField(choices=PLATFORM, default=1, null=True, blank=True)
    genres = models.ManyToManyField("Genre")
    albums = models.ManyToManyField("Album", through="ChannelAlbum")
    publisher = models.ForeignKey("Publisher", on_delete=models.SET_NULL, null=True, blank=True)
    status = models.PositiveIntegerField(choices=STATUS, default=0, null=False, blank=False)
    is_end = models.PositiveIntegerField(choices=END_STATUS, default=0, null=False, blank=False)

    show_info = models.OneToOneField("ShowInfo", on_delete=models.SET_NULL, null=True, blank=True)
    artist_info = models.OneToOneField("ArtistInfo", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "%s" % (self.channel_id)



class ChannelAlbum(models.Model):

    channel = models.ForeignKey("Channel", on_delete=models.CASCADE)
    album = models.ForeignKey("Album", on_delete=models.CASCADE)

    rank = models.PositiveIntegerField(null=False, blank=False)

    class Meta:
        unique_together=("channel", "album")

    def __str__(self):
        return "%s, %s" % (self.channel, self.album)



class Playlist(models.Model):

    PLATFORM = (
        (1, "Android"),
        (2, "IOS"),
        (3, "Web"),
    )

    playlist_id = models.CharField(max_length=ID_LENGTH_MAX, primary_key=True)
    playlist_name = models.CharField(max_length=NAME_LENGTH_MAX, null=False, blank=False)
    playlist_cover = models.CharField(max_length=URL_LENGTH_MAX, null=True, blank=True)
    platform_id = models.PositiveIntegerField(choices=PLATFORM, default=1, null=True, blank=True)
    videos = models.ManyToManyField("Video", through="PlaylistVideo")

    def __str__(self):
        return "%s" % (self.channel_id)


class PlaylistVideo(models.Model):

    playlist = models.ForeignKey("Playlist", on_delete=models.CASCADE)
    video = models.ForeignKey("Video", on_delete=models.CASCADE)

    rank = models.PositiveIntegerField(null=False, blank=False)

    class Meta:
        unique_together=("playlist", "video")

    def __str__(self):
        return "%s, %s" % (self.playlist, self.video)


class Banner(models.Model):

    PLATFORM = (
        (1, "Android"),
        (2, "IOS"),
        (3, "Web"),
    )

    POSITION = (
        (1, "home"),
        (2, "buzz"),
        (3, "music"),
        (4, "browser"),
    )

    STATUS = (
        (0, "Offline"),
        (1, "Online"),
    )

    CONTENT_TYPE = (
        (1, "publisher"),
        (2, "tv show"),
        (21, "channel-->tv show"),
        (22, "album-->season"),
        (23, "video-->episode"),
        (3, "music"),
        (31, "channel-->artist"),
        (32, "album-->album"),
        (33, "music-->music video"),
        (34, "playlist"),
        (4, "movie"),
        (41, "album-->sequel"),
        (42, "video-->movie video"),
        (5, "short video"),
    )

    banner_id = models.CharField(max_length=ID_LENGTH_MAX, primary_key=True)
    banner_name = models.CharField(max_length=NAME_LENGTH_MAX, null=False, blank=False)
    poster = models.CharField(max_length=URL_LENGTH_MAX, null=True, blank=True)
    status = models.PositiveIntegerField(choices=STATUS, default=0, null=False, blank=False)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    platform_id = models.PositiveIntegerField(choices=PLATFORM, default=1, null=False, blank=False)
    position_id = models.PositiveIntegerField(choices=POSITION, default=1, null=False, blank=False)
    order = models.PositiveIntegerField(null=True, blank=True)
    description = models.CharField(max_length=DESCRIPTION_LENGTH_MAX, null=True, blank=True)
    content_type = models.PositiveIntegerField(choices=CONTENT_TYPE, null=True, blank=True)

    content = GenericForeignKey(ct_field='content_ct', fk_field='content_fk')
    content_ct = models.ForeignKey(ContentType, null=True, blank=True)
    content_fk = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return "%s" % (self.banner_id)


class CardItem(models.Model):

    UNIT_TYPE = (
        (1, "publisher publisher"),
        (2, "tvshow category"),
        (21, "tvshow channnel"),
        (22, "season album"),
        (23, "episode video"),
    )

    CONTENT_TYPE = (
        (1, "Publisher"),
        (2, "Language"),
        (3, "Genre"),
        (4, "Actor"),
        (5, "Director"),
        (6, "Singer"),
        (7, "Record_Label"),
        (8, "Lyricist"),
        (9, "Composer"),
        (10, "Video"),
        (11, "Album"),
        (12, "Channel"),
    )
    
    carditem_id = models.AutoField(primary_key=True)
    card = models.ForeignKey("Card", null=True, blank=True)
    rank = models.IntegerField()
    
    unit_type = models.PositiveIntegerField(choices=UNIT_TYPE, default=1, null=False, blank=False)
    content_type = models.PositiveIntegerField(choices=UNIT_TYPE, default=1, null=False, blank=False)

    contents = GM2MField(through="CardItemContent")

    def __str__(self):
        return "%s" % (self.carditem_id)


class CardItemContent(models.Model):

    carditem = models.ForeignKey(CardItem)

    content = GenericForeignKey(ct_field='content_ct', fk_field='content_fk')
    content_ct = models.ForeignKey(ContentType, null=True, blank=True)
    content_fk = models.CharField(max_length=255, null=True, blank=True)

    rank = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.carditem, content_ct)


class Card(models.Model):

    RECALL_TYPE = (
        (1, "Title"),
        (2, "Label"),
    )

    STATUS = (
        (0, "Offline"),
        (1, "Online"),
    )

    card_id = models.CharField(max_length=ID_LENGTH_MAX, primary_key=True)
    card_name = models.CharField(max_length=NAME_LENGTH_MAX, null=False, blank=False)
    recall_type = models.PositiveIntegerField(choices=RECALL_TYPE, default=0, null=False, blank=False)
    status = models.PositiveIntegerField(choices=STATUS, default=0, null=False, blank=False)

    def __str__(self):
        return "%s" % (self.card_id)


class CardList(models.Model):

    PLATFORM = (
        (1, "Android"),
        (2, "IOS"),
        (3, "Web"),
    )

    POSITION = (
        (1, "home"),
        (2, "buzz"),
        (3, "music"),
        (4, "browser"),
    )

    TAB_STYLE = (
        ("1", "tab style 1"),
        ("2", "tab style 2"),
    )

    cardlist_id = models.CharField(max_length=ID_LENGTH_MAX, primary_key=True)
    cardlist_name = models.CharField(max_length=NAME_LENGTH_MAX, null=False, blank=False)
    position_id = models.PositiveIntegerField(choices=POSITION, default=1, null=False, blank=False)
    platform_id = models.PositiveIntegerField(choices=PLATFORM, default=1, null=False, blank=False)
    cards = models.ManyToManyField("Card", through="CardlistCard")

    tab_style = models.CharField(max_length=NAME_LENGTH_MAX, choices=TAB_STYLE, null=True, blank=True)

    def __str__(self):
        return "%s" % (self.cardlist_id)


class CardlistCard(models.Model):

    LIST_STYLE = (
        ("1", "list style 1"),
        ("2", "list style 2"),
    )

    MORE_STYLE = (
        ("1", "more style 1"),
        ("2", "more style 2"),
    )

    STATUS = (
        (0, "Offline"),
        (1, "Online"),
    )

    cardlist = models.ForeignKey("CardList", on_delete=models.CASCADE)
    card = models.ForeignKey("Card", on_delete=models.CASCADE)
    rank = models.IntegerField()

    status = models.PositiveIntegerField(choices=STATUS, default=0, null=False, blank=False)
    list_style = models.CharField(max_length=NAME_LENGTH_MAX, choices=LIST_STYLE, null=True, blank=True)
    more_style = models.CharField(max_length=NAME_LENGTH_MAX, choices=MORE_STYLE, null=True, blank=True)

    class Meta:
        unique_together=("cardlist", "card")


