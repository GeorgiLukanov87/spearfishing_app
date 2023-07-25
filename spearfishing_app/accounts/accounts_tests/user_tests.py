from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.test import TestCase

UserModel = get_user_model()


class AppUserModelTests(TestCase):
    def test_last_name_min_length(self):
        with self.assertRaises(ValidationError):
            user = UserModel(last_name='D')
            user.full_clean()

    def test_last_name_max_length(self):
        with self.assertRaises(ValidationError):
            user = UserModel(last_name='L' * (UserModel.LAST_NAME_MAX_LEN + 1))
            user.full_clean()

    def test_last_name_only_letters(self):
        with self.assertRaises(ValidationError):
            user = UserModel(last_name='Doe123')
            user.full_clean()

    def test_email_unique(self):
        UserModel.objects.create(
            username='testuser',
            email='test@example.com',
            password='test123'
        )

        # Try to create another user with the same email
        with self.assertRaises(ValidationError):
            user = UserModel(
                username='anotheruser',
                email='test@example.com',
                password='password123'
            )
            user.full_clean()

    def test_gender_choices_invalid(self):
        with self.assertRaises(ValidationError):
            user = UserModel(gender='invalid')
            user.full_clean()
