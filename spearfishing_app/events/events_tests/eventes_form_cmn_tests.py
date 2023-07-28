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

    def test_event_form_validation(self):
        create_url = reverse('create-event')
        data = {
            'name': '',
            'location': 'Test Location',
        }
        response = self.client.post(create_url, data=data)
        self.assertEqual(response.status_code, 302)

        edit_url = reverse('edit-event', kwargs={'pk': self.event.pk})
        data = {
            'name': '',
            'location': 'Test Location',
        }
        response = self.client.post(edit_url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_gift_page_view(self):
        url = reverse('gift-page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/gift-page.html')

    def test_events_list_view(self):
        url = reverse('events-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/events-list.html')
        self.assertContains(response, 'Test Event')
        self.assertContains(response, 'Test Location')

    def test_events_list_view_with_staff_user(self):
        self.client.force_login(self.staff_user)
        url = reverse('events-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/events-list.html')
        self.assertContains(response, 'Test Event')
        self.assertContains(response, 'Test Location')

    def test_events_list_view_with_non_staff_user(self):
        self.client.force_login(self.user)
        url = reverse('events-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/events-list.html')
        self.assertContains(response, 'Test Event')
        self.assertContains(response, 'Test Location')
        self.assertNotContains(response, 'Add Competitors')
