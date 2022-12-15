from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Company(models.Model):
    # company = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # company_logo = models.ImageField(null=True, blank=True, upload_to="company_logo")
    company_name = models.CharField(max_length=30)
    legal_entity = models.CharField(max_length=30)
    company_address = models.CharField(max_length=255, verbose_name='Адрес компании')
    email = models.EmailField(max_length=128)
    phone_number = models.CharField(max_length=12)


class CompanyProfile(models.Model):
    company = models.OneToOneField(Company, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    about = models.CharField(blank=True, max_length=512, verbose_name='обо мне')

    @receiver(post_save, sender=Company)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            CompanyProfile.objects.create(user=instance)

    @receiver(post_save, sender=Company)
    def save_user_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()
