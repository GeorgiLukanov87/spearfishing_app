# from django.test import TestCase
# from django.urls import reverse
# from spearfishing_app.locations.models import Search
#
#
# class LocationsViewTest(TestCase):
#
#     def test_locations_view_post_valid_form(self):
#         url = reverse('locations')
#         data = {
#             'address': 'New York, USA',
#         }
#         response = self.client.post(url, data=data)
#         self.assertRedirects(response, reverse('locations'))
#         self.assertEqual(Search.objects.count(), 1)
#         new_search = Search.objects.last()
#         self.assertEqual(new_search.address, 'New York, USA')
#
#     def test_weather_view_get(self):
#         url = reverse('weather')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'locations/weather.html')
#
#     def test_weather_view_post_valid_city(self):
#         url = reverse('weather')
#         data = {
#             'city': 'New York',
#         }
#         response = self.client.post(url, data=data)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'locations/weather.html')
#         self.assertIn('weather_data', response.context)
#
#     def test_weather_view_post_empty_city(self):
#         url = reverse('weather')
#         data = {
#             'city': '',
#         }
#         response = self.client.post(url, data=data)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'locations/weather.html')
#         self.assertNotIn('weather_data', response.context)
#
#     def test_weather_view_post_invalid_city(self):
#         url = reverse('weather')
#         data = {
#             'city': 'Invalid City',
#         }
#         response = self.client.post(url, data=data)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'locations/wrong-data1.html')
#         self.assertNotIn('weather_data', response.context)
