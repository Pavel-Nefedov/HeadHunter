import sys
from pprint import pprint
from django.db import models

sys.path.append('../')
from userapp.models import User
from common.variables import MENU_LIST


# Create your models here.

#
# class Author(models.Model):
#     name = models.CharField(verbose_name='Имя', max_length=32)
#     last_name = models.CharField(verbose_name='Фамилия', max_length=64)
#     is_active = models.BooleanField(verbose_name='Активен', default=False)
#
#     # def __str__(self):
#         return f'{self.name} {self.last_name}'


# Класс Хабов(Тэгов или ключевых слов)
class Hub(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'Хаб(ключевое слово) {self.name}'


# Класс статей
class Article(models.Model):
    # Тема или поток, большие категории из верхнего меню. Все берется из констант в common\variables.py
    SUBJECT_CHOICES = tuple([(subject, subject) for subject in MENU_LIST if subject != 'Главная'])
    subject = models.CharField(verbose_name='Тема статьи', max_length=32, choices=SUBJECT_CHOICES, default='Другое')

    # Хабы статьи (ключевые слова)
    hubs = models.ManyToManyField(Hub, verbose_name='Хабы статьи', blank=True)

    # Название статьи
    title = models.CharField(verbose_name='Название статьи', max_length=128)

    # Дата публикации, если не заполнено, то это черновик
    posted_at = models.DateTimeField(verbose_name='Дата публикации', blank=True)

    # Для нежного удаления, если проставлено, значит статья не показывается
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # todo think maybe list of subjects or we can use keywords

    text = models.TextField(verbose_name='Статья', blank=True)
    # todo think maybe list of authors
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_posted = models.BooleanField(verbose_name='размещена', default=True)

    def __str__(self):
        return f'Статья {self.title}, Автор {self.author}, Тема {self.subject}'

    @staticmethod
    def get_items():
        return Article.objects.filter(is_posted=True).order_by('-posted_at')
