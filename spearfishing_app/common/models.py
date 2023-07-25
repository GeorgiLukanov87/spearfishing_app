from django.contrib.auth import get_user_model
from django.db import models
from embed_video.fields import EmbedVideoField

from spearfishing_app.photos.models import Photo

UserModel = get_user_model()


# common/models.py
class Comment(models.Model):
    COMMENT_TEXT_MAX_LEN = 1500
    text = models.CharField(
        max_length=COMMENT_TEXT_MAX_LEN,
        null=False,
        blank=False,
    )

    date_time_of_publication = models.DateField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['-date_time_of_publication']


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Video(models.Model):
    VIDEO_TITLE_MAX_LEN = 100

    title = models.CharField(max_length=VIDEO_TITLE_MAX_LEN)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['added']
