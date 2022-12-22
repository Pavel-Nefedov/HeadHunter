import sys
from pprint import pprint
from uuid import uuid4

from django.db import models
from datetime import datetime

from django.utils.timezone import now

from common.utils import from_cyrillic_to_eng

sys.path.append('../')
from userapp.models import User
from common.variables import MENU_LIST





# Класс Хабов(Тэгов или ключевых слов)
class Hub(models.Model):
    name = models.CharField(max_length=50, blank=True, unique=True)
    name_slug = models.CharField(max_length=50, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.name_slug:
            self.name_slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Хаб(ключевое слово) {self.name}'


# Класс статей
class Article(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    # Тема или поток, большие категории из верхнего меню. Все берется из констант в common\variables.py
    SUBJECT_CHOICES = tuple([(subject, subject) for subject in MENU_LIST if subject != 'Главная'])
    subject = models.CharField(verbose_name='Тема статьи', max_length=32, choices=SUBJECT_CHOICES, default='Другое')

    # Хабы статьи (ключевые слова)
    hubs = models.ManyToManyField(Hub, verbose_name='Хабы статьи', blank=True)

    # Название статьи
    title = models.CharField(verbose_name='Название статьи', max_length=128)

    # Дата публикации, если не заполнено, то это черновик
    # Todo: Решить, как статья будет автоматически выкладываться, если будет проставлена posted_at в будущем
    # Todo: Реализовать отображения статуса черновик, убрать auto_now_add=True
    posted_at = models.DateTimeField(verbose_name='Дата публикации', null=True, blank=True, auto_now_add=True)

    # Для нежного удаления, если проставлено, значит статья не показывается
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    text = models.TextField(verbose_name='Статья', blank=True)

    # todo think maybe list of authors
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    is_posted = models.BooleanField(verbose_name='размещена', default=False, blank=True)

    def __str__(self):
        return f'Статья {self.title}, Автор {self.author}, Тема {self.subject}'


    def save(self, *args, **kwargs):
        if self.deleted_at:
            self.is_posted = False
            self.posted_at = None
        if self.posted_at and self.posted_at < now():
            self.is_posted = True
        if self.is_posted:
            self.posted_at = now()
        super().save(*args, **kwargs)


    @staticmethod
    def get_items():
        return Article.objects.filter(is_posted=True).order_by('-posted_at')
