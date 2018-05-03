from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class PushTestCase(APITestCase):

    def test_all(self):
        payload = {
            "alert": "Here test message.",
            "production": False,
            "extras": {"article_slug": "slug"}
        }
        uri = reverse('service-push:all')
        res = self.client.post(uri, data=payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
