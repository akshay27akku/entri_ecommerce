from django.test import TestCase

class TestUrl(TestCase):
    def testhome(self):
        response = self.client.get('/')
        # self.assertEqual(response.status_code,200)
        self.assertEqual(response.status_code, 404)