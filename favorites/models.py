from django.db import models
from django.conf import settings
from companyapp.models import Vacancy


class Favorites(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vacancy')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
