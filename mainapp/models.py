from django.db import models

NULLABLE = {'null': True, 'blank': True}


class News(models.Model):
    title = models.CharField(max_length=1024, verbose_name='Заголовок новости', unique=True)
    link = models.CharField(max_length=2048, verbose_name='Ссылка на новость', unique=True)
    date = models.DateField(verbose_name='Дата публикации', **NULLABLE)
    description = models.TextField(verbose_name='Краткое описание новости', **NULLABLE)
