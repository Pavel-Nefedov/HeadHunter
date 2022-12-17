from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True)
    birthday = models.DateField
    banned_before = models.DateTimeField(verbose_name='Забанен до', null=True, blank=True)
