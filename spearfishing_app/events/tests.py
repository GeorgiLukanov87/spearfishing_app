# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from django.urls import reverse
# from spearfishing_app.events.models import Event
# from spearfishing_app.events.forms import EventCreateForm, EventEditForm, EventDeleteForm
#
# UserModel = get_user_model()
#
#
# class EventsViewTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.user = UserModel.objects.create_user(username='testuser', email='testuser@example.com', password='testpass')
#         cls.staff_user = UserModel.objects.create_user(username='staffuser', email='staffuser@example.com',
#                                                        password='testpass', is_staff=True)
#         cls.event = Event.objects.create(name='Test Event', location='Test Location')
#
#     def test_event_form_validation(self):
#         create_url = reverse('create-event')
#         data = {
#             'name': '',
#             'location': 'Test Location',
#         }
#         response = self.client.post(create_url, data=data)
#         self.assertEqual(response.status_code, 302)
#
#         edit_url = reverse('edit-event', kwargs={'pk': self.event.pk})
#         data = {
#             'name': '',
#             'location': 'Test Location',
#         }
#         response = self.client.post(edit_url, data=data)
#         self.assertEqual(response.status_code, 302)
#
#     def test_delete_event_view_post_success(self):
#         self.client.force_login(self.staff_user)
#         url = reverse('delete-event', kwargs={'pk': self.event.pk})
#         response = self.client.post(url)
#         self.assertRedirects(response, reverse('events-list'))
#         self.assertFalse(Event.objects.filter(pk=self.event.pk).exists())
#
#     def test_delete_event_view_post_cancel(self):
#         self.client.force_login(self.staff_user)
#         url = reverse('delete-event', kwargs={'pk': self.event.pk})
#         data = {'cancel': True}
#         response = self.client.post(url, data=data)
#         self.assertRedirects(response, reverse('events-list'))
#
#     def test_gift_page_view(self):
#         url = reverse('gift-page')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'common/gift-page.html')
#
#     def test_events_list_view(self):
#         url = reverse('events-list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'events/events-list.html')
#         self.assertContains(response, 'Test Event')
#         self.assertContains(response, 'Test Location')
#
#     def test_events_list_view_with_staff_user(self):
#         self.client.force_login(self.staff_user)
#         url = reverse('events-list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'events/events-list.html')
#         self.assertContains(response, 'Test Event')
#         self.assertContains(response, 'Test Location')
#
#     def test_events_list_view_with_non_staff_user(self):
#         self.client.force_login(self.user)
#         url = reverse('events-list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'events/events-list.html')
#         self.assertContains(response, 'Test Event')
#         self.assertContains(response, 'Test Location')
#         self.assertNotContains(response, 'Add Competitors')
#
#     def test_create_event_view_redirects_unauthenticated_user(self):
#         url = reverse('create-event')
#         response = self.client.get(url)
#         self.assertRedirects(response, f'/accounts/login/?next={url}')
#
#     def test_create_event_view_get(self):
#         self.client.force_login(self.user)
#         url = reverse('create-event')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'events/create-event.html')
#         self.assertIsInstance(response.context['form'], EventCreateForm)
#
#     def test_create_event_view_post_success(self):
#         self.client.force_login(self.staff_user)
#         url = reverse('create-event')
#         data = {
#             'name': 'New Event',
#             'location': 'New Location',
#         }
#         response = self.client.post(url, data=data)
#         self.assertRedirects(response, reverse('events-list'))
#         self.assertEqual(Event.objects.count(), 2)
#         new_event = Event.objects.last()
#         self.assertEqual(new_event.name, 'New Event')
#         self.assertEqual(new_event.location, 'New Location')
#
#     def test_edit_event_view_redirects_unauthenticated_user(self):
#         url = reverse('edit-event', kwargs={'pk': self.event.pk})
#         response = self.client.get(url)
#         self.assertRedirects(response, f'/accounts/login/?next={url}')
#
#     def test_edit_event_view_get(self):
#         self.client.force_login(self.staff_user)
#         url = reverse('edit-event', kwargs={'pk': self.event.pk})
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'events/edit-event.html')
#         self.assertIsInstance(response.context['form'], EventEditForm)
#
#     def test_edit_event_view_post_success(self):
#         self.client.force_login(self.staff_user)
#         url = reverse('edit-event', kwargs={'pk': self.event.pk})
#         data = {
#             'name': 'Updated Event',
#             'location': 'Updated Location',
#         }
#         response = self.client.post(url, data=data)
#         self.assertRedirects(response, reverse('events-list'))
#         self.event.refresh_from_db()
#         self.assertEqual(self.event.name, 'Updated Event')
#         self.assertEqual(self.event.location, 'Updated Location')
#
#     def test_delete_event_view_redirects_unauthenticated_user(self):
#         url = reverse('delete-event', kwargs={'pk': self.event.pk})
#         response = self.client.get(url)
#         self.assertRedirects(response, f'/accounts/login/?next={url}')
#
#     def test_delete_event_view_get(self):
#         self.client.force_login(self.staff_user)
#         url = reverse('delete-event', kwargs={'pk': self.event.pk})
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'events/delete-event.html')
#         self.assertIsInstance(response.context['form'], EventDeleteForm)
#
#     def test_delete_event_view_post_success(self):
#         self.client.force_login(self.staff_user)
#         url = reverse('delete-event', kwargs={'pk': self.event.pk})
#         response = self.client.post(url)
#         self.assertRedirects(response, reverse('events-list'))
#         self.assertFalse(Event.objects.filter(pk=self.event.pk).exists())
