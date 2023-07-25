# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from django.urls import reverse
# from spearfishing_app.equipment.models import Equipment
# from spearfishing_app.equipment.forms import EquipmentAddForm
#
# UserModel = get_user_model()
#
#
# class EquipmentViewTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.user = UserModel.objects.create_user(username='testuser', password='testpass')
#         cls.add_equipment_url = reverse('add-equipment')
#
#     def test_add_equipment_view_redirects_unauthenticated_user(self):
#         response = self.client.get(self.add_equipment_url)
#         self.assertRedirects(response, f'/accounts/login/?next={self.add_equipment_url}')
#
#     def test_add_equipment_view_get(self):
#         self.client.force_login(self.user)
#         response = self.client.get(self.add_equipment_url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'equipment/add-equipment.html')
#         self.assertIsInstance(response.context['form'], EquipmentAddForm)
#
#     def test_add_equipment_view_post_success(self):
#         self.client.force_login(self.user)
#         data = {
#             'gun_model': 'Cressi',
#             'gun_material': 'Wood',
#             'gun_length': '65cm',
#             'bands': '13mm',
#             'bands_brand': 'SigalSub',
#             'fins_model': 'Cressi',
#             'fins_material': 'Plastic',
#         }
#         response = self.client.post(self.add_equipment_url, data=data)
#         self.assertRedirects(response, reverse('index'))
#         self.assertEqual(Equipment.objects.count(), 1)
#         equipment = Equipment.objects.first()
#         self.assertEqual(equipment.gun_model, 'Cressi')
#         self.assertEqual(equipment.gun_material, 'Wood')
#         self.assertEqual(equipment.gun_length, '65cm')
#         self.assertEqual(equipment.bands, '13mm')
#         self.assertEqual(equipment.bands_brand, 'SigalSub')
#         self.assertEqual(equipment.fins_model, 'Cressi')
#         self.assertEqual(equipment.fins_material, 'Plastic')
#         self.assertEqual(equipment.owner, self.user)
#
#     def test_add_equipment_view_post_invalid_form(self):
#         self.client.force_login(self.user)
#         data = {}  # Empty data to trigger form validation error
#         response = self.client.post(self.add_equipment_url, data=data)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'equipment/add-equipment.html')
#         self.assertIsInstance(response.context['form'], EquipmentAddForm)
#
#
# class EquipmentEditViewTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.user = UserModel.objects.create_user(username='testuser', password='testpass')
#         cls.equipment = Equipment.objects.create(
#             gun_model='Cressi',
#             gun_material='Wood',
#             gun_length='65cm',
#             bands='13mm',
#             bands_brand='SigalSub',
#             fins_model='Cressi',
#             fins_material='Plastic',
#             owner=cls.user
#         )
#         cls.edit_equipment_url = reverse('edit-equipment', kwargs={'pk': cls.equipment.pk})
#
#     def test_edit_equipment_view_get(self):
#         self.client.force_login(self.user)
#         response = self.client.get(self.edit_equipment_url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'equipment/edit-equipment.html')
#
#     def test_edit_equipment_view_post_success(self):
#         self.client.force_login(self.user)
#         data = {
#             'gun_model': 'Beuchat',
#             'gun_material': 'Aluminium',
#             'gun_length': '70cm',
#             'bands': '14mm',
#             'bands_brand': 'Cressi',
#             'fins_model': 'Omer',
#             'fins_material': 'Carbon',
#         }
#         response = self.client.post(self.edit_equipment_url, data=data)
#         self.assertRedirects(response, reverse('profile details', kwargs={'pk': self.user.pk}))
#         self.equipment.refresh_from_db()
#         self.assertEqual(self.equipment.gun_model, 'Beuchat')
#         self.assertEqual(self.equipment.gun_material, 'Aluminium')
#         self.assertEqual(self.equipment.gun_length, '70cm')
#         self.assertEqual(self.equipment.bands, '14mm')
#         self.assertEqual(self.equipment.bands_brand, 'Cressi')
#         self.assertEqual(self.equipment.fins_model, 'Omer')
#         self.assertEqual(self.equipment.fins_material, 'Carbon')
#
#     def test_edit_equipment_view_post_invalid_form(self):
#         self.client.force_login(self.user)
#         data = {}  # Empty data to trigger form validation error
#         response = self.client.post(self.edit_equipment_url, data=data)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'equipment/edit-equipment.html')
