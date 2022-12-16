import sys
from pprint import pprint
from django.db import models

sys.path.append('../')

from common.variables import MENU_LIST


# Create your models here.

# todo: think about authors and users. May be authors are childs of users?

class Author(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=32)
    last_name = models.CharField(verbose_name='Фамилия', max_length=64)
    is_active = models.BooleanField(verbose_name='Активен', default=False)

    # todo status user, registred user, or something more
    def __str__(self):
        return f'{self.name} {self.last_name}'


class Article(models.Model):
    SUBJECT_CHOICES = tuple([(subject, subject) for subject in MENU_LIST])
    title = models.CharField(verbose_name='Название статьи', max_length=128)
    posted_at = models.DateTimeField(verbose_name='Дата публикации', blank=True)
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # todo think maybe list of subjects or we can use keywords
    subject = models.CharField(verbose_name='Тема статьи', max_length=32, choices=SUBJECT_CHOICES, default='Другое')
    text = models.TextField(verbose_name='Статья', blank=True)
    # todo think maybe list of authors
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_posted = models.BooleanField(verbose_name='размещена', default=True)

    def __str__(self):
        return f'Статья {self.title}, Автор {self.author}, Тема {self.subject}'

    @staticmethod
    def get_items():
        return Article.objects.filter(is_posted=True).order_by('-posted_at')
