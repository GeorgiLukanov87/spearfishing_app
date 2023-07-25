from django.contrib.auth import get_user_model
from django.test import TestCase
from spearfishing_app.common.models import Video

UserModel = get_user_model()


class VideoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.video = Video.objects.create(title='Test Video', url='https://www.youtube.com/watch?v=abcdefghijk')

    def test_video_title(self):
        video = Video.objects.get(id=self.video.id)
        self.assertEqual(video.title, 'Test Video')

    def test_video_url(self):
        video = Video.objects.get(id=self.video.id)
        self.assertEqual(video.url, 'https://www.youtube.com/watch?v=abcdefghijk')

    def test_str_representation(self):
        video = Video.objects.get(id=self.video.id)
        self.assertEqual(str(video), 'Test Video')
