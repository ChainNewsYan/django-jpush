from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker

f = Faker()

# class ServiceAPITestCase(APITestCase):
#     def setUp(self):
#         pass
#
#     def test_get_device_info(self):
#         data = {
#
#         }
#         path = reverse("api")
#         res = self.client.post(
#             data=data,
#             path=path,
#         )
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
#
#     def test_add_device(self):
#         data = {
#
#         }
#         path = reverse("api")
#         res = self.client.post(
#             data=data,
#             path=path,
#         )
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
#
#     def test_remove_device(self):
#         data = {
#
#         }
#         path = reverse("api")
#         res = self.client.post(
#             data=data,
#             path=path,
#         )
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
#
#     def test_get_device_tag(self):
#         data = {
#
#         }
#         path = reverse("api")
#         res = self.client.post(
#             data=data,
#             path=path,
#         )
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
#
#     def test_update_device_tag(self):
#         data = {
#
#         }
#         path = reverse("api")
#         res = self.client.post(
#             data=data,
#             path=path,
#         )
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
#
#     def test_delete_device_tag(self):
#         data = {
#
#         }
#         path = reverse("api")
#         res = self.client.post(
#             data=data,
#             path=path,
#         )
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
#
#     def test_push_message(self):
#         data = {
#
#         }
#         path = reverse("api")
#         res = self.client.post(
#             data=data,
#             path=path,
#         )
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
#
#     def test_push_message_to_all_device(self):
#         data = {
#
#         }
#         path = reverse("api")
#         res = self.client.post(
#             data=data,
#             path=path,
#         )
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
#
#     def test_push_message_to_special_device_by_tag(self):
#         data = {
#
#         }
#         path = reverse("api")
#         res = self.client.post(
#             data=data,
#             path=path,
#         )
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
