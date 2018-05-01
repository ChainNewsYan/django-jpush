from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class PushTestCase(APITestCase):

    def test_alias(self):
        pass
    # def test_alias(self):
    #     payload = {
    #         'alias': ['alias1'],
    #         'tags': ['tag'],
    #     }
    #     uri = reverse('service-push:alias')
    #     res = self.client.post(uri, data=payload)
    #     self.assertEqual(res.json(), '')
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
