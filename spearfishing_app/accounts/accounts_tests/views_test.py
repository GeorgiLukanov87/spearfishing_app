from django.contrib.auth import get_user_model
from django.test import RequestFactory
from django.test import TestCase
from django.urls import reverse, resolve

UserModel = get_user_model()


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
