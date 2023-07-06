from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

UserModel = get_user_model()


class Story(models.Model):
    STORY_TITLE_MAX_LEN = 50
    STORY_TITLE_MIN_LEN = 3

    STORY_DESCRIPTION_MAX_LEN = 1500
    STORY_DESCRIPTION_MIN_LEN = 3

    title = models.CharField(
        max_length=STORY_TITLE_MAX_LEN,
        validators=[
            validators.MinLengthValidator(
                STORY_TITLE_MIN_LEN,
                message='Story title must be at least 3 characters!'
            ),
        ]
    )

    date = models.DateField(
        auto_now_add=True,
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )

    description = models.TextField(
        max_length=STORY_DESCRIPTION_MAX_LEN,
        validators=[
            validators.MinLengthValidator(
                STORY_DESCRIPTION_MIN_LEN,
                message='Story description must be at least 3 characters!'
            ),
        ]
    )

    creator = models.ForeignKey(
        UserModel,
        on_delete=models.PROTECT
    )
