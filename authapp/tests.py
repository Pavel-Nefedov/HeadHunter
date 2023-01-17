# Create your tests here.
from urllib import response
from django.test import TestCase
from django.test.client import Client
from django.core.management import call_command
from authapp.models import HHUser

class TestUserManagement(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = HHUser.objects.create_user('Tarantino', password='12345')
        # self.user = HHUser.objects.create_user(first_name='Quentin', last_name='Tarantino', \
        #     password='12345', is_candidate=True)
    
    def test_user_login(self):
        # главная страница без логина
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        # self.assertTrue(response.context['user'].is_anonymous)
        # self.assertEqual(response.context['title'], 'главная')
        self.assertNotContains(response, 'Пользователь', status_code=200)
        self.client.login(username='Tarantino', password='12345')

        # логинимся
        response = self.client.get('/auth/login')
        # self.assertFalse(response.context['user'].is_anonymous)
        # self.assertEqual(response.context['user'], self.user)

        # главная страница после логина
        response = self.client.get('')
        # self.assertContains(response, 'Пользователь', status_code=200)
        self.assertEqual(response.context['user'], self.user)

    # def tearDown(self):
    #     call_command('mainapp', 'authapp', 'candidateapp', 'companyapp')