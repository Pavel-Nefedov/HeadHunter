from django.conf import settings
from django.db import models

from companyapp.models import Vacancy


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="favorite")
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    add_datetime = models.DateTimeField(verbose_name="время добавления", auto_now_add=True)
