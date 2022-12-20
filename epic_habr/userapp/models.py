from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    birthday = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    # Todo: Решить, как пользователь будет автоматически разбаниваться
    banned_before = models.DateTimeField(verbose_name='Забанен до', null=True, blank=True)
