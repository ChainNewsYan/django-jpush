from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class DeviceTestCase(APITestCase):
    def test_alias_get(self):
        payload = {
            'alias': 'alias1',
            'platform': 'android,ios',
        }
        uri = reverse('djpush-device:alias')
        res = self.client.get(uri, data=payload)
        self.assertEqual(res.json().get('registration_ids'), [])
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_alias_delete(self):
        payload = {
            'alias': 'alias1',
            'platform': 'android,ios',
        }
        uri = reverse('djpush-device:alias')
        res = self.client.delete(uri, data=payload)
        self.assertEqual(res.json(), 'success')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_device_get(self):
        payload = {
            'reg_id': '171976fa8aad9180f73',
        }
        uri = reverse('djpush-device:device')
        res = self.client.get(uri, data=payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_device_set(self):
        payload = {
            'reg_id': '171976fa8aad9180f73',
            'tags': 'tag1'
        }
        uri = reverse('djpush-device:device')
        res = self.client.post(uri, data=payload)
        self.assertEqual(res.json(), 'success')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_tag_list_get(self):
        uri = reverse('djpush-device:tag')
        res = self.client.get(uri)
        self.assertEqual(all(res.json().get('tags', None)), True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_tag_check_true(self):
        payload = {
            'tag': 'tag1',
            'reg_id': '171976fa8aad9180f73',
        }
        uri = reverse('djpush-device:check')
        res = self.client.get(uri, data=payload)
        self.assertEqual(res.json(), {'result': True})
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_tag_check_false(self):
        payload = {
            'tag': 'tag2',
            'reg_id': '171976fa8aad9180f73',
        }
        uri = reverse('djpush-device:check')
        res = self.client.get(uri, data=payload)
        self.assertEqual(res.json(), {'result': False})
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_platform_tag_delete(self):
        payload = {
            'tag': 'tag2',
            'platform': 'android,ios',
        }
        uri = reverse('djpush-device:tag')
        res = self.client.delete(uri, data=payload)
        self.assertEqual(res.json(), 'success')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_user_tag_update(self):
        payload = {
            'tag': 'tag3',
            'reg_id': '171976fa8aad9180f73',
        }
        uri = reverse('djpush-device:user')
        res = self.client.post(uri, data=payload)
        self.assertEqual(res.json(), 'success')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_device_mobile(self):
        payload = {
            'reg_id': '171976fa8aad9180f73',
            'mobile': '',
        }
        uri = reverse('djpush-device:mobile')
        res = self.client.post(uri, data=payload)
        self.assertEqual(res.json(), 'success')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
