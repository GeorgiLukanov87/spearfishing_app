from django.contrib.auth import get_user_model

from django.test import TestCase
from django.urls import reverse

from spearfishing_app.common.models import Comment, Video
from spearfishing_app.photos.models import Photo
from spearfishing_app.common.forms import CommentForm

UserModel = get_user_model()


class CommonAppTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(username='testuser', password='testpassword')
        self.photo = Photo.objects.create(photo='Test Photo', description='Test Description', user=self.user)

    def test_index_view(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/home-page.html')

    def test_like_functionality_view(self):
        url = reverse('like', args=[self.photo.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_add_comment_view(self):
        url = reverse('add-comment', args=[self.photo.id])
        data = {'text': 'Test Comment'}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_delete_comment_view(self):
        comment = Comment.objects.create(text='Test Comment', to_photo=self.photo, user=self.user)
        url = reverse('delete-comment', args=[self.photo.id, comment.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Expect a redirect after deleting a comment

    def test_all_users_cbv(self):
        # Test the AllUsersCBV view
        url = reverse('users-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/users-list.html')

    class BandCalculatorCBVTest(TestCase):
        def test_band_calculator_cbv(self):
            # Test the BandCalculator CBV view
            url = reverse('calculator')
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'common/Band-calculator.html')

    class ApneaTrainerCBVTest(TestCase):
        def test_apnea_trainer_cbv(self):
            # Test the ApneaTrainer CBV view
            url = reverse('apnea-trainer')
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'common/apnea-trainer.html')

    def test_comment_form(self):
        form = CommentForm(data={'text': 'Test Comment'})
        self.assertTrue(form.is_valid())
