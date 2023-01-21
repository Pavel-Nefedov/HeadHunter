from http import HTTPStatus
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from authapp.models import HHUser
from authapp.views import LoginUser, RegisterUser, SuccessLogin

User = get_user_model()



class TaskURLTests(TestCase):
    def setUp(self):
        # Создаем неавторизованный клиент
        self.guest_client = HHUser()

    # Проверяем общедоступные страницы
    def test_home_url_exists_at_desired_location(self):
        """Страница / доступна любому пользователю."""
        response = self.guest_client.get('/')
        self.assertEqual(response.status_code, 200)

    # def test_task_added_url_exists_at_desired_location(self):
    #     """Страница /added/ доступна любому пользователю."""
    #     response = self.guest_client.get('/index/')
    #     self.assertEqual(response.status_code, 200)


# class StaticURLTests(TestCase):
#
#     def setUp(self):
#         self.user = HHUser.objects.create_user(username='user')
#
#     def test_static_page(self):
#         """Страница доступна по URL."""
#         pages: tuple = ('/auth/login/', '/auth/register/')
#         for page in pages:
#             response = self.user.get(page)
#             error_name: str = f'Ошибка: нет доступа до страницы {page}'
#             self.assertEqual(response.status_code, HTTPStatus.OK, error_name)
#
#     def test_urls_uses_correct_template(self):
#         """URL-адрес использует соответствующий шаблон."""
#         templates_url_names: dict = {
#             '/auth/login/': 'authapp/login.html',
#             '/auth/register/': 'authapp/register.html',
#         }
#         for adress, template in templates_url_names.items():
#             with self.subTest(adress=adress):
#                 response = self.user.get(adress)
#                 error_name: str = f'Ошибка: {adress} ожидал шаблон {template}'
#                 self.assertTemplateUsed(response, template, error_name)
