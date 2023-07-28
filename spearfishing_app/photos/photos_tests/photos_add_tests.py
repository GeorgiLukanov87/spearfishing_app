from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from spearfishing_app.photos.models import Photo
from spearfishing_app.photos.forms import PhotoCreateForm

UserModel = get_user_model()


class PhotosViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserModel.objects.create_user(username='testuser', email='testuser@example.com', password='testpass')
        cls.photo = Photo.objects.create(photo=SimpleUploadedFile("test.jpg", b"file_content"), user=cls.user)

    def test_add_photo_view_redirects_unauthenticated_user(self):
        url = reverse('add-photo')
        response = self.client.get(url)
        self.assertRedirects(response, f'/accounts/login/?next={url}')

    def test_add_photo_view_get(self):
        self.client.force_login(self.user)
        url = reverse('add-photo')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/photo-add-page.html')
        self.assertIsInstance(response.context['form'], PhotoCreateForm)

    def test_add_photo_view_unauthenticated_user(self):
        url = reverse('add-photo')
        response = self.client.get(url)
        self.assertRedirects(response, f'/accounts/login/?next={url}')

    def test_add_photo_view_authenticated_user(self):
        self.client.force_login(self.user)
        url = reverse('add-photo')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/photo-add-page.html')
        self.assertIsInstance(response.context['form'], PhotoCreateForm)
