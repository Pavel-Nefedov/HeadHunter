from django.db import models


# Create your models here.
class Candidate(models.Model):
    """
    search_area - район/область поиска работы
    """
    # user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    email = models.EmailField(max_length=128)
    phone_number = models.CharField(max_length=12)
    search_area = models.CharField(verbose_name='адрес', max_length=256)
