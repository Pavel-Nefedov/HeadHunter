import uuid
from datetime import date

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

    def get_absolute_url(self):
        return f'/candidate/user_profile/{self.id}'


class ContactInfo:
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(blank=True, max_length=30, null=False) # имя
    surname = models.CharField(blank=True, max_length=30, null=False) # фамилия
    patronymic = models.CharField(blank=True, max_length=30, null=False) # отчество
    birthday = models.DateField(blank=True, max_length=30, default=date.today) # дата рождения
    city = models.CharField(blank=True, max_length=180, null=False)  # город
    GENDER_CHOICES = (
        ('М', 'Women'),
        ('Ж', 'Man'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True) # гендер
    MOVING_CHOICES = (
        ('1', 'Возможен'),
        ('2', 'Невозможен'),
        ('3', 'Желателен'),
        ('4', 'Нежелателен'),
    )
    moving = models.CharField(max_length=1, choices=MOVING_CHOICES, blank=True) # возможен ли переезд
    BUSINESS_TRIPS_CHOICES = (
        ('1', 'Никогда'),
        ('2', 'Готов'),
        ('3', 'Иногда'),
    )
    business_trips = models.CharField(max_length=1, choices=BUSINESS_TRIPS_CHOICES, blank=True) # командировки

    def __str__(self):
        return self.name

class Resume(models.Model):
    contact = models.ForeignKey(ContactInfo, on_delete=models.CASCADE, primary_key=True)


    # Желаемая должность и зарплата
    desired_position = models.CharField(blank=True, max_length=180, null=False) # желаемая должность
    salary = models.IntegerField(blank=True) # зарплата
    COLORS = (
        ('R', 'Полная занятость'),
        ('B', 'Частичная занятость'),
        ('G', 'Проектная работа'),
    )
    color = models.CharField(max_length=3, choices=COLORS, blank=True)


