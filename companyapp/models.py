from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from authapp.models import HHUser


class CompanyProfile(models.Model):
    user = models.OneToOneField(HHUser, null=True, on_delete=models.CASCADE)
    company_logo = models.ImageField(null=True, blank=True, upload_to="company_logo")
    company_name = models.CharField(max_length=30, default='No name')
    legal_entity = models.CharField(max_length=30, blank=True)
    company_address = models.CharField(max_length=255, verbose_name='Адрес компании', default='Some address')
    email = models.EmailField(max_length=128, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    about_company = models.CharField(blank=True, max_length=512, verbose_name='О компании')

    @receiver(post_save, sender=HHUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            CompanyProfile.objects.create(company=instance)

    @receiver(post_save, sender=HHUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.companyprofile.save()

# class Company(models.Model):
#     # company = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     # company_logo = models.ImageField(null=True, blank=True, upload_to="company_logo")
#     company_name = models.CharField(max_length=30)
#     legal_entity = models.CharField(max_length=30)
#     company_address = models.CharField(max_length=255, verbose_name='Адрес компании')
#     email = models.EmailField(max_length=128)
#     phone_number = models.CharField(max_length=12)
#
#
# class CompanyProfile(models.Model):
#     company = models.OneToOneField(Company, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
#     about = models.CharField(blank=True, max_length=512, verbose_name='обо мне')
#
#     @receiver(post_save, sender=Company)
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             CompanyProfile.objects.create(company=instance)
#
#     @receiver(post_save, sender=Company)
#     def save_user_profile(sender, instance, **kwargs):
#         instance.companyprofile.save()


class Vacancy(models.Model):
    vacancy_name = models.CharField(max_length=30, unique=False, null=False, db_index=True, default='SOME STRING')
    city = models.CharField(max_length=30, unique=False, null=False, db_index=True, default='CITY N')
    company = models.OneToOneField(CompanyProfile, unique=False, null=False, db_index=True, on_delete=models.CASCADE)
    about_company = models.CharField(blank=True, max_length=512, verbose_name='О компании')
    duties_description = models.CharField(blank=True, max_length=512, verbose_name='Обязанности')
    requirements_description = models.CharField(blank=True, max_length=512, verbose_name='Требования')
    work_conditions = models.CharField(blank=True, max_length=512, verbose_name='Условия труда')
    created = models.DateTimeField(auto_now_add=True)
    salary_min = models.CharField(blank=True, max_length=512, verbose_name='Минимальная заралата')
    salary_max = models.CharField(blank=True, max_length=512, verbose_name='Максимальная заралата')
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()

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

    @receiver(post_save, sender=HHUser)
    def create_vacancy(sender, instance, created, **kwargs):
        if created:
            Vacancy.objects.create(company=instance)

    @receiver(post_save, sender=HHUser)
    def save_vacancy(sender, instance, **kwargs):
        instance.vacancy.save()
