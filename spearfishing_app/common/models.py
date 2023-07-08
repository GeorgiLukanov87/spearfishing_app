from django.contrib.auth import get_user_model
from django.db import models

from spearfishing_app.photos.models import Photo

UserModel = get_user_model()


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
