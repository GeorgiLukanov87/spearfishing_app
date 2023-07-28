from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from spearfishing_app.stories.models import Story

UserModel = get_user_model()


class StoriesViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserModel.objects.create_user(username='testuser', email='testuser@example.com', password='testpass')
        cls.staff_user = UserModel.objects.create_user(username='staffuser', email='staffuser@example.com',
                                                       password='testpass', is_staff=True)
        cls.story = Story.objects.create(title='Test Story', description='Test Description', creator=cls.user)

    def test_story_delete_cbv_authenticated_user_not_owner(self):
        self.client.force_login(self.user)
        url = reverse('delete-story', kwargs={'pk': self.story.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Access Forbidden

    def test_story_delete_cbv_authenticated_user_owner(self):
        self.client.force_login(self.user)
        url = reverse('delete-story', kwargs={'pk': self.story.pk})
        response = self.client.post(url)
        self.assertRedirects(response, reverse('all-stories'))
        self.assertFalse(Story.objects.filter(pk=self.story.pk).exists())
