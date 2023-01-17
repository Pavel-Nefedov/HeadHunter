from django.test import TestCase
from authapp.models import HHUser
from authapp.forms import RegisterUserForm


class Setup_Class(TestCase):

    def setUp(self):
        self.user = HHUser.objects.create(
            username='username',
            email='email',
            user_role='user_role',
            password1='password1',
            password2='password2'
        )


class User_Form_Test(TestCase):

    def test_UserForm_valid(self):
        form = RegisterUserForm(data={
            'username': "username",
            'email': 'email',
            'user_role': 'user_role',
            'password1': 'password1',
            'password2': 'password2',
        })
        self.assertTrue(form.is_valid())

    def test_UserForm_invalid(self):
        form = RegisterUserForm(data={
            'username': " ",
            'email': ' ',
            'user_role': ' ',
            'password1': ' ',
            'password2': ' ',
        })
        self.assertFalse(form.is_valid())
