from django.conf import settings
from django.db import models

from authapp.models import HHUser


class CompanyProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_logo = models.ImageField(null=True, blank=True, upload_to="company_logo")
    company_name = models.CharField(max_length=30, default='No name')
    legal_entity = models.CharField(max_length=30, blank=True)
    company_address = models.CharField(max_length=255, verbose_name='Адрес компании', default='Some address')
    email = models.EmailField(max_length=128, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    about_company = models.CharField(blank=True, max_length=512, verbose_name='О компании')


class Vacancy(models.Model):
    vacancy_name = models.CharField(max_length=30, unique=False, null=False, db_index=True, default='SOME STRING')
    city = models.CharField(max_length=30, unique=False, null=False, db_index=True, default='CITY N')
    company = models.ForeignKey(CompanyProfile, unique=False, null=False, db_index=True, on_delete=models.CASCADE)
    about_company = models.CharField(blank=True, max_length=512, verbose_name='О компании')
    duties_description = models.CharField(blank=True, max_length=512, verbose_name='Обязанности')
    requirements_description = models.CharField(blank=True, max_length=512, verbose_name='Требования')
    work_conditions = models.CharField(blank=True, max_length=512, verbose_name='Условия труда')
    created = models.DateTimeField(auto_now_add=True)
    salary_min = models.CharField(blank=True, max_length=512, verbose_name='Минимальная заралата')
    salary_max = models.CharField(blank=True, max_length=512, verbose_name='Максимальная заралата')
    is_active = models.BooleanField(verbose_name='активна', default=True)

    is_for_disabled = models.BooleanField(
        default=False,
        verbose_name='Вакансия для людей с инвалидностью',
        help_text=('Отметьте, вакансия подходит для людей с ограниченными физическими возможностями')
    )

    is_full_day = models.BooleanField(
        default=False,
        verbose_name='Полный рабочий день',
        help_text=('Отметьте, если вакансия полного рабочего дня')
    )
    is_intern = models.BooleanField(
        default=False,
        verbose_name='Cтажировка',
        help_text=('Отметьте, если вакансия является стажировкой')
    )
