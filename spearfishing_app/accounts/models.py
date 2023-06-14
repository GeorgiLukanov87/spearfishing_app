from enum import Enum

from django.contrib.auth import models as auth_models
from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Only letters allowed!')


class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


class Gender(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'
    Do_Not_Show = 'Do not show'


class AppUser(auth_models.AbstractUser):
    FIRST_NAME_MAX_LEN = 20
    FIRST_NAME_MIN_LEN = 3

    LAST_NAME_MAX_LEN = 20
    LAST_NAME_MIN_LEN = 3

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_only_letters,
        )
    )

    email = models.EmailField(
        unique=True,
    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len(),
    )
