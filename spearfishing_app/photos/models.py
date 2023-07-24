from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from django.core.exceptions import ValidationError


def validate_file_size_5mb(image_object):
    if image_object.size > 5242880:
        raise ValidationError('The maximum file size that can be uploaded is 5MB')


UserModel = get_user_model()


# photos/models.py
class Photo(models.Model):
    PHOTO_DESCRIPTION_MAX_LEN = 300
    PHOTO_DESCRIPTION_MIN_LEN = 10
    PHOTO_LOCATION_MAX_LEN = 30

    photo = models.ImageField(
        upload_to='images',
        validators=(
            validate_file_size_5mb,
        ),
        blank=False,
        null=False,
    )

    description = models.TextField(
        max_length=PHOTO_DESCRIPTION_MAX_LEN,
        validators=(MinLengthValidator(PHOTO_DESCRIPTION_MIN_LEN),),
        blank=True,
        null=True,
    )

    location = models.CharField(
        max_length=PHOTO_LOCATION_MAX_LEN,
        blank=True,
        null=True,
    )

    date_of_publication = models.DateField(
        auto_now=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
