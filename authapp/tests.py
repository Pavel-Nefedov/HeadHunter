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