# Create your tests here.

from django.test import TestCase
from django.test.client import Client

class TestMainappSmoke(TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_urls(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/auth/register/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/auth/login/')
        self.assertEqual(response.status_code, 200)
