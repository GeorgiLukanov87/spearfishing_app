from django.contrib.auth import get_user_model
from django.test import TestCase

from django.test import TestCase
from django.urls import reverse

from spearfishing_app.common.models import Comment, Like
from spearfishing_app.photos.models import Photo
from spearfishing_app.common.forms import CommentForm

UserModel = get_user_model()


class CommonAppTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = UserModel.objects.create_user(username='testuser', password='testpassword')

        # Create a test photo
        self.photo = Photo.objects.create(photo='Test Photo', description='Test Description', user=self.user)

    def test_index_view(self):
        # Test the index view
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/home-page.html')

    def test_like_functionality_view(self):
        # Test the like functionality view
        url = reverse('like', args=[self.photo.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Expect a redirect after liking a photo

    def test_add_comment_view(self):
        # Test the add comment view
        url = reverse('add-comment', args=[self.photo.id])
        data = {'text': 'Test Comment'}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)  # Expect a redirect after adding a comment

    def test_delete_comment_view(self):
        # Create a test comment
        comment = Comment.objects.create(text='Test Comment', to_photo=self.photo, user=self.user)

        # Test the delete comment view
        url = reverse('delete-comment', args=[self.photo.id, comment.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Expect a redirect after deleting a comment

    def test_all_users_cbv(self):
        # Test the AllUsersCBV view
        url = reverse('users-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/users-list.html')

    def test_band_calculator_cbv(self):
        # Test the BandCalculator CBV view
        url = reverse('calculator')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/Band-calculator.html')

    def test_apnea_trainer_cbv(self):
        # Test the ApneaTrainer CBV view
        url = reverse('apnea-trainer')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/apnea-trainer.html')

    def test_comment_form(self):
        # Test the CommentForm
        form = CommentForm(data={'text': 'Test Comment'})
        self.assertTrue(form.is_valid())
