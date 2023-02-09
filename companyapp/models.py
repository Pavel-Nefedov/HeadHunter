from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models

from authapp.models import HHUser
from mainapp.models import AppCanvasModel

NULLABLE = {'null': True, 'blank': True}


class CompanyProfile(AppCanvasModel):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    is_moderated = models.BooleanField(default=False, verbose_name='Профайл прошел модерацию')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    company_logo = models.ImageField(upload_to="company_logo/", verbose_name="Логотип", **NULLABLE)
    company_name = models.CharField(max_length=100, default='No name', verbose_name="Наименование компании")
    legal_entity = models.CharField(max_length=100, blank=True, verbose_name="Юридическое лицо")
    company_address = models.CharField(max_length=255, default='Some address', verbose_name='Адрес компании')
    email = models.EmailField(max_length=128, blank=True, verbose_name='Email')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name='Телефон')
    about_company = models.CharField(blank=True, max_length=512, verbose_name='О компании')


class Vacancy(AppCanvasModel):
    is_moderated = models.BooleanField(default=False, verbose_name='Вакансия прошла модерацию')
    company = models.ForeignKey(CompanyProfile, unique=False, null=False, db_index=True, on_delete=models.CASCADE)
    vacancy_name = models.CharField(max_length=300, unique=False, null=False, db_index=True, default='SOME STRING')
    city = models.CharField(max_length=100, db_index=True, default='', verbose_name='Город размещения')
    duties_description = models.TextField(blank=True, verbose_name='Обязанности')
    requirements_description = models.TextField(verbose_name='Требования', **NULLABLE)
    work_conditions = models.TextField(verbose_name='Условия труда', **NULLABLE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания вакансии')
    salary_min = models.PositiveIntegerField(verbose_name='Минимальная заралата', **NULLABLE)
    salary_max = models.PositiveIntegerField(verbose_name='Максимальная заралата', **NULLABLE)
    currency = models.CharField(max_length=10, **NULLABLE)
    is_active = models.BooleanField(verbose_name='Открыта', default=False)

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
