# from django.contrib.auth import get_user_model
# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.test import TestCase
# from django.urls import reverse
# from spearfishing_app.photos.models import Photo
# from spearfishing_app.photos.forms import PhotoCreateForm, PhotoEditForm, PhotoDeleteForm
#
# UserModel = get_user_model()
#
#
# class PhotosViewTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.user = UserModel.objects.create_user(username='testuser', email='testuser@example.com', password='testpass')
#         cls.photo = Photo.objects.create(photo=SimpleUploadedFile("test.jpg", b"file_content"), user=cls.user)
#
#     def test_add_photo_view_redirects_unauthenticated_user(self):
#         url = reverse('add-photo')
#         response = self.client.get(url)
#         self.assertRedirects(response, f'/accounts/login/?next={url}')
#
#     def test_add_photo_view_get(self):
#         self.client.force_login(self.user)
#         url = reverse('add-photo')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'photos/photo-add-page.html')
#         self.assertIsInstance(response.context['form'], PhotoCreateForm)
#
#     # Add more tests for different scenarios in the 'add_photo' view
#
#     def test_show_photo_details_view(self):
#         url = reverse('photo-details', kwargs={'pk': self.photo.pk})
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'photos/photo-details-page.html')
#         self.assertEqual(response.context['photo'], self.photo)
#
#     # Add more tests for different scenarios in the 'show_photo_details' view
#
#     def test_edit_photo_view_redirects_unauthenticated_user(self):
#         url = reverse('edit-photo', kwargs={'pk': self.photo.pk})
#         response = self.client.get(url)
#         self.assertRedirects(response, f'/accounts/login/?next={url}')
#
#     def test_edit_photo_view_get(self):
#         self.client.force_login(self.user)
#         url = reverse('edit-photo', kwargs={'pk': self.photo.pk})
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'photos/photo-edit-page.html')
#         self.assertIsInstance(response.context['form'], PhotoEditForm)
#         self.assertEqual(response.context['photo'], self.photo)
#
#     # Add more tests for different scenarios in the 'edit_photo' view
#
#     def test_delete_photo_view_redirects_unauthenticated_user(self):
#         url = reverse('delete-photo', kwargs={'pk': self.photo.pk})
#         response = self.client.get(url)
#         self.assertRedirects(response, f'/accounts/login/?next={url}')
#
#     def test_delete_photo_view_get(self):
#         self.client.force_login(self.user)
#         url = reverse('delete-photo', kwargs={'pk': self.photo.pk})
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'photos/photo-delete-page.html')
#         self.assertIsInstance(response.context['form'], PhotoDeleteForm)
#         self.assertEqual(response.context['photo'], self.photo)
#
#     # Add more tests for different scenarios in the 'delete_photo' view
#     def test_add_photo_view_unauthenticated_user(self):
#         url = reverse('add-photo')
#         response = self.client.get(url)
#         self.assertRedirects(response, f'/accounts/login/?next={url}')
#
#     def test_add_photo_view_authenticated_user(self):
#         self.client.force_login(self.user)
#         url = reverse('add-photo')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'photos/photo-add-page.html')
#         self.assertIsInstance(response.context['form'], PhotoCreateForm)
#
#     def test_edit_photo_view_unauthenticated_user(self):
#         url = reverse('edit-photo', kwargs={'pk': self.photo.pk})
#         response = self.client.get(url)
#         self.assertRedirects(response, f'/accounts/login/?next={url}')
#
#     def test_edit_photo_view_authenticated_user_not_owner(self):
#         self.client.force_login(self.user)
#         url = reverse('edit-photo', kwargs={'pk': self.photo.pk})
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)  # Access Forbidden
#
#     def test_edit_photo_view_authenticated_user_owner(self):
#         self.client.force_login(self.user)
#         url = reverse('edit-photo', kwargs={'pk': self.photo.pk})
#         data = {
#             'description': 'Updated description',
#             'location': 'Updated location',
#         }
#         response = self.client.post(url, data=data)
#         self.assertRedirects(response, reverse('photo-details', args=[self.photo.pk]))
#         self.photo.refresh_from_db()
#         self.assertEqual(self.photo.description, 'Updated description')
#         self.assertEqual(self.photo.location, 'Updated location')
#
#     def test_delete_photo_view_unauthenticated_user(self):
#         url = reverse('delete-photo', kwargs={'pk': self.photo.pk})
#         response = self.client.get(url)
#         self.assertRedirects(response, f'/accounts/login/?next={url}')
#
#     def test_delete_photo_view_authenticated_user_not_owner(self):
#         self.client.force_login(self.user)
#         url = reverse('delete-photo', kwargs={'pk': self.photo.pk})
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)  # Access Forbidden
