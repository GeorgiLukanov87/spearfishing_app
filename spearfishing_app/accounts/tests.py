from spearfishing_app.accounts.models import AppUser
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.test import RequestFactory
from django.test import TestCase
from django.urls import reverse, resolve
from spearfishing_app.accounts.views import SingInView, SignInView, SignOutView, UserDetailsView, UserEditView, \
    UserDeleteView, to_github

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
        AppUser.objects.create(
            username='testuser',
            email='test@example.com',
            password='test123'
        )

        # Try to create another user with the same email
        with self.assertRaises(ValidationError):
            user = AppUser(
                username='anotheruser',
                email='test@example.com',
                password='password123'
            )
            user.full_clean()

    def test_gender_choices_invalid(self):
        with self.assertRaises(ValidationError):
            user = AppUser(gender='invalid')
            user.full_clean()


class AccountsViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = UserModel.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword',
        )

    def test_sing_in_view(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register-page.html')

        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword',
            'password2': 'newpassword',
        }
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/home-page.html')

    def test_sing_in_view_invalid_form(self):
        url = reverse('register')
        response = self.client.post(url, data={}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register-page.html')
        self.assertFormError(response, 'form', 'username', 'This field is required.')
        self.assertFalse(response.context['user'].is_authenticated)

    def test_sign_in_view(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login-page.html')

    def test_sign_out_view(self):
        url = reverse('logout')
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/home-page.html')
        self.assertFalse(response.context['user'].is_authenticated)

    def test_user_details_view(self):
        url = reverse('profile details', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile-details-page.html')

    def test_user_edit_view(self):
        url = reverse('profile edit', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile-edit-page.html')

    def test_user_delete_view(self):
        url = reverse('profile delete', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile-delete-page.html')

    def test_to_github_view(self):
        url = reverse('go to github')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, 'https://github.com/GeorgiLukanov87')


class UrlsTestCase(TestCase):
    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class, SingInView)

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, SignInView)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, SignOutView)

    def test_profile_details_url_resolves(self):
        url = reverse('profile details', args=[1])  # Replace 1 with the appropriate user ID
        self.assertEqual(resolve(url).func.view_class, UserDetailsView)

    def test_profile_edit_url_resolves(self):
        url = reverse('profile edit', args=[1])  # Replace 1 with the appropriate user ID
        self.assertEqual(resolve(url).func.view_class, UserEditView)

    def test_profile_delete_url_resolves(self):
        url = reverse('profile delete', args=[1])  # Replace 1 with the appropriate user ID
        self.assertEqual(resolve(url).func.view_class, UserDeleteView)

    def test_to_github_url_resolves(self):
        url = reverse('go to github')
        self.assertEqual(resolve(url).func, to_github)
