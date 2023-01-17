from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from django.conf import settings
from django import forms
from authapp.models import HHUser

TEST_OF_POST: int = 13


class PaginatorViewsTest(TestCase):

    def setUp(self):
        self.guest_client = Client()
        self.user = HHUser.objects.create_user(username='auth')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)
        # self.group = Group.objects.create(title='Тестовая группа',
        #                                   slug='test_group')
        # bilk_post: list = []
        # for i in range(TEST_OF_POST):
        #     bilk_post.append(Post(text=f'Тестовый текст {i}',
        #                           group=self.group,
        #                           author=self.user))
        # Post.objects.bulk_create(bilk_post)

    # def test_correct_page_context_guest_client(self):
    #     '''Проверка количества постов на первой и второй страницах незарегистрированного пользователя. '''
    #     pages: tuple = (reverse('mainapp:index'))
    #     for page in pages:
    #         response1 = self.guest_client.get(page)
    #         response2 = self.guest_client.get(page + '?page=2')
    #         count_posts1 = len(response1.context['page_obj'])
    #         count_posts2 = len(response2.context['page_obj'])
    #         error_name1 = (f'Ошибка: {count_posts1} постов,'
    #                        f' должно {settings.FIRST_OF_POSTS}')
    #         error_name2 = (f'Ошибка: {count_posts2} постов,'
    #                        f'должно {TEST_OF_POST - settings.FIRST_OF_POSTS}')
    #         self.assertEqual(count_posts1,
    #                          settings.FIRST_OF_POSTS,
    #                          error_name1)
    #         self.assertEqual(count_posts2,
    #                          TEST_OF_POST - settings.FIRST_OF_POSTS,
    #                          error_name2)

    # def test_correct_page_context_authorized_client(self):
    #     '''Проверка контекста страниц авторизованного пользователя'''
    #     pages = [reverse('posts:index'),
    #              reverse('posts:profile',
    #                      kwargs={'username': f'{self.user.username}'})
    #              ]
    #     for page in pages:
    #         response1 = self.authorized_client.get(page)
    #         response2 = self.authorized_client.get(page + '?page=2')
    #         count_posts1 = len(response1.context['page_obj'])
    #         count_posts2 = len(response2.context['page_obj'])
    #         error_name1 = (f'Ошибка: {count_posts1} постов,'
    #                        f' должно {settings.FIRST_OF_POSTS}')
    #         error_name2 = (f'Ошибка: {count_posts2} постов,'
    #                        f'должно {TEST_OF_POST - settings.FIRST_OF_POSTS}')
    #         self.assertEqual(count_posts1,
    #                          settings.FIRST_OF_POSTS,
    #                          error_name1)
    #         self.assertEqual(count_posts2,
    #                          TEST_OF_POST - settings.FIRST_OF_POSTS,
    #                          error_name2)
