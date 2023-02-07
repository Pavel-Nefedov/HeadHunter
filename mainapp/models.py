from django.db import models

NULLABLE = {'null': True, 'blank': True}


class AppCanvasModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создано',
        editable=False,
        null=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Обновлено',
        editable=False,
        null=False,
    )

    class Meta:
        abstract = True
        ordering = ['-updated_at']


class News(models.Model):
    title = models.CharField(max_length=1024, verbose_name='Заголовок новости', unique=True)
    link = models.CharField(max_length=2048, verbose_name='Ссылка на новость', unique=True)
    date = models.DateField(verbose_name='Дата публикации', **NULLABLE)
    description = models.TextField(verbose_name='Краткое описание новости', **NULLABLE)
