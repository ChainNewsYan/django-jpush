from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class AdminTestCase(APITestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_admin_list(self):
        uri = reverse('service:')
        pass
