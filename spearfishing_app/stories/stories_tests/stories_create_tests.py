from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from spearfishing_app.stories.models import Story
from spearfishing_app.stories.forms import StoryCreateForm

UserModel = get_user_model()


class StoriesViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserModel.objects.create_user(username='testuser', email='testuser@example.com', password='testpass')
        cls.staff_user = UserModel.objects.create_user(username='staffuser', email='staffuser@example.com',
                                                       password='testpass', is_staff=True)
        cls.story = Story.objects.create(title='Test Story', description='Test Description', creator=cls.user)

    def test_story_create_cbv_unauthenticated_user(self):
        url = reverse('create-story')
        response = self.client.get(url)
        self.assertRedirects(response, f'/accounts/login/?next={url}')

    def test_story_create_cbv_authenticated_user(self):
        self.client.force_login(self.user)
        url = reverse('create-story')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stories/create-story.html')
        self.assertIsInstance(response.context['form'], StoryCreateForm)

    def test_story_create_cbv_post_authenticated_user(self):
        self.client.force_login(self.user)
        url = reverse('create-story')
        data = {
            'title': 'New Story',
            'description': 'New description',
        }
        response = self.client.post(url, data=data)
        self.assertRedirects(response, reverse('all-stories'))
        self.assertEqual(Story.objects.count(), 2)
        new_story = Story.objects.last()
        self.assertEqual(new_story.title, 'New Story')
        self.assertEqual(new_story.description, 'New description')
        self.assertEqual(new_story.creator, self.user)

    def test_story_create_cbv_post_authenticated_user_with_dirty_words(self):
        self.client.force_login(self.user)
        url = reverse('create-story')
        data = {
            'title': 'New Story',
            'description': 'This is a bad word: fuck',
        }
        response = self.client.post(url, data=data)
        self.assertRedirects(response, reverse('all-stories'))
        self.assertEqual(Story.objects.count(), 2)
        new_story = Story.objects.last()
        self.assertEqual(new_story.title, 'New Story')
        self.assertEqual(new_story.description, 'This is a bad word: f**k')
        self.assertEqual(new_story.creator, self.user)
