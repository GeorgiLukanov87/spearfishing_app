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

    def test_story_details_cbv_unauthenticated_user(self):
        url = reverse('details-story', kwargs={'pk': self.story.pk})
        response = self.client.get(url)
        self.assertRedirects(response, f'/accounts/login/?next={url}')

    def test_story_details_cbv_authenticated_user(self):
        self.client.force_login(self.user)
        url = reverse('details-story', kwargs={'pk': self.story.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stories/details-story.html')
        self.assertEqual(response.context['story'], self.story)
        self.assertEqual(response.context['is_owner'], True)

    def test_story_list_cbv(self):
        url = reverse('all-stories')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stories/story-list.html')
        self.assertQuerysetEqual(response.context['object_list'], [self.story])
