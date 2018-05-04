from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK


class AdminTestCase(APITestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_admin_list(self):
        pass
        # uri = reverse('djpush-admin:list')
        # res = self.client.get(uri, format='json')
        # self.assertEqual(res.json(), '')
        # self.assertEqual(res.status_code, HTTP_200_OK)
