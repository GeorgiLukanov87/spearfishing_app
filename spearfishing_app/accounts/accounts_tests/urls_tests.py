from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from spearfishing_app.accounts.views import SingInView, SignInView, SignOutView, UserDetailsView, UserEditView, \
    UserDeleteView, to_github

UserModel = get_user_model()


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
