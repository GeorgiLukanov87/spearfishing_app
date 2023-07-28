from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from spearfishing_app.events.models import Event
from spearfishing_app.events.forms import EventCreateForm, EventEditForm, EventDeleteForm

UserModel = get_user_model()


class EventsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserModel.objects.create_user(username='testuser', email='testuser@example.com', password='testpass')
        cls.staff_user = UserModel.objects.create_user(username='staffuser', email='staffuser@example.com',
                                                       password='testpass', is_staff=True)
        cls.event = Event.objects.create(name='Test Event', location='Test Location')

    def test_edit_event_view_redirects_unauthenticated_user(self):
        url = reverse('edit-event', kwargs={'pk': self.event.pk})
        response = self.client.get(url)
        self.assertRedirects(response, f'/accounts/login/?next={url}')

    def test_edit_event_view_get(self):
        self.client.force_login(self.staff_user)
        url = reverse('edit-event', kwargs={'pk': self.event.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/edit-event.html')
        self.assertIsInstance(response.context['form'], EventEditForm)

    def test_edit_event_view_post_success(self):
        self.client.force_login(self.staff_user)
        url = reverse('edit-event', kwargs={'pk': self.event.pk})
        data = {
            'name': 'Updated Event',
            'location': 'Updated Location',
        }
        response = self.client.post(url, data=data)
        self.assertRedirects(response, reverse('events-list'))
        self.event.refresh_from_db()
        self.assertEqual(self.event.name, 'Updated Event')
        self.assertEqual(self.event.location, 'Updated Location')
