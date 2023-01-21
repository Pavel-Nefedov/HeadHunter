from django.test import TestCase
from authapp.models import HHUser
from authapp.forms import RegisterUserForm

USERNAME = 'maks21'
EMAIL = 'maks21@localhost'
USER_ROLE = 'is_company'
PASSWORD1 = 'Fourty47'
PASSWORD2 = 'Fourty47'


class SetupClass(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = HHUser.objects.create(
            username=USERNAME,
            email=EMAIL,
            user_role=USER_ROLE,
            password1=PASSWORD1,
            password2=PASSWORD2
        )


class UserFormTest(TestCase):

    def test_UserForm_valid(self):
        form = RegisterUserForm(data={
            'username': USERNAME,
            'email': EMAIL,
            'user_role': USER_ROLE,
            'password1': PASSWORD1,
            'password2': PASSWORD2,
        })
        self.assertTrue(form.is_valid())

    def test_UserForm_invalid(self):
        form = RegisterUserForm(data={
            'username': USERNAME,
            'email': EMAIL,
            'user_role': USER_ROLE,
            'password1': PASSWORD1,
            'password2': 1,
        })
        self.assertFalse(form.is_valid())
