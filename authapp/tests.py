# Create your tests here.
from urllib import response

from django.core.management import call_command
from django.test import TestCase
from django.test.client import Client

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

# from django.test import TestCase
# from authapp.models import HHUser
#
#
# class AuthorModelTest(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         HHUser.objects.create(first_name='maks', last_name='maks')
#
#     def test_first_name_label(self):
#         user = HHUser.objects.get(id=1)
#         field_label = user._meta.get_field('first_name').verbose_name
#         self.assertEquals(field_label, 'first name')
#
#     def test_last_name_label(self):
#         user = HHUser.objects.get(id=1)
#         field_label = user._meta.get_field('last_name').verbose_name
#         self.assertEquals(field_label, 'last name')
#
#     def test_password_label(self):
#         password = HHUser.objects.get(id=1)
#         field_label = password._meta.get_field('password').verbose_name
#         self.assertEquals(field_label, 'password')
#
#     def test_first_name_max_length(self):
#         user = HHUser.objects.get(id=1)
#         max_length = user._meta.get_field('first_name').max_length
#         self.assertEquals(max_length, 150)
#
#     def test_last_name_max_length(self):
#         user = HHUser.objects.get(id=1)
#         max_length = user._meta.get_field('last_name').max_length
#         self.assertEquals(max_length, 150)
#
#     def test_password_max_length(self):
#         password = HHUser.objects.get(id=1)
#         max_length = password._meta.get_field('password').max_length
#         self.assertEquals(max_length, 128)
#
#
#     # def test_get_absolute_url(self):
#     #     user = HHUser.objects.get(id=1)
#     #     # This will also fail if the urlconf is not defined.
#     #     self.assertEquals(user.get_absolute_url(), '/catalog/author/1')
