from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Event(models.Model):
    NAME_MAX_LEN = 20
    LOCATION_MAX_LEN = 20

    name = models.CharField(
        max_length=NAME_MAX_LEN,
    )

    created = models.DateTimeField(
        auto_now=True,
    )

    location = models.CharField(
        max_length=LOCATION_MAX_LEN,
    )

    competitors = models.ManyToManyField(
        UserModel,
        blank=True,
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )

    start_date = models.DateField(
        default='2023-06-06'
    )

    def __str__(self):
        return self.name
