import uuid
from datetime import date

from django.conf import settings
from django.db import models


# Create your models here.
class Candidate(models.Model):
    """
    search_area - район/область поиска работы
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    email = models.EmailField(max_length=128)
    phone_number = models.CharField(max_length=12)
    search_area = models.CharField(verbose_name='Адрес', max_length=256)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class ContactInfo(models.Model):
    """
    Модель контактной информации для резюме
    """
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(blank=True, max_length=30, null=False, verbose_name='Имя')
    surname = models.CharField(blank=True, max_length=30, null=False, verbose_name='Фамилия')
    patronymic = models.CharField(blank=True, max_length=30, null=False, verbose_name='Отчество')
    birthday = models.DateField(blank=True, max_length=30, default=date.today, verbose_name='Дата рождения')
    city = models.CharField(blank=True, max_length=180, null=False, verbose_name='Город')
    GENDER_CHOICES = (
        ('М', 'Women'),
        ('Ж', 'Man'),
    )
    MOVING_CHOICES = (
        ('1', 'Возможен'),
        ('2', 'Невозможен'),
        ('3', 'Желателен'),
        ('4', 'Нежелателен'),
    )
    BUSINESS_TRIPS_CHOICES = (
        ('1', 'Никогда'),
        ('2', 'Готов'),
        ('3', 'Иногда'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, verbose_name='Гендер')
    moving = models.CharField(max_length=1, choices=MOVING_CHOICES, blank=True, verbose_name='Возможен ли переезд')
    business_trips = models.CharField(max_length=1, choices=BUSINESS_TRIPS_CHOICES, blank=True,
                                      verbose_name='Командировки')

    def __str__(self):
        return f'User №{self.id}'


class PositionAndSelery(models.Model):
    """
    Желаемая должность и зарплата - для резюме
    """
    desired_position = models.CharField(blank=True, max_length=180, null=False, verbose_name='Желаемая должность')
    salary = models.IntegerField(blank=True, verbose_name='Зарплата')
    BUSYNESS_CHOICES = (
        ('FE', 'Полная занятость'),
        ('PE', 'Частичная занятость'),
        ('PW', 'Проектная работа'),
        ('V', 'Волонтерство'),
        ('I', 'Стажировка'),
    )
    WORK_SCHEDULE = (
        ('FD', 'Полный день'),
        ('SS', 'Сменный график'),
        ('FS', 'Гибкий график'),
        ('DW', 'Удаленная работа'),
        ('SM', 'Вахтовый метод'),
    )
    busyness = models.CharField(max_length=5, choices=BUSYNESS_CHOICES, blank=True, verbose_name='Варниант занятости')
    work_schedule = models.CharField(max_length=5, choices=WORK_SCHEDULE, blank=True, verbose_name='График работы')

    def __str__(self):
        return f'User №{self.id}'


class WorkExperience(models.Model):
    """
    Опыт работы - для резюме
    """
    getting_started = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Начало работы')
    end_work = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Окончание работы')
    working = models.BooleanField(verbose_name='Работаю по настоящее время')
    organization = models.CharField(max_length=150, blank=True, verbose_name='Организация')
    post = models.CharField(max_length=150, blank=True, verbose_name='Должность')
    responsibilities = models.TextField(blank=True, verbose_name='Обязанности на рабочем месте')
    skills = models.TextField(blank=True, verbose_name='Ключевые навыки')
    about_me = models.TextField(blank=True, verbose_name='О себе')

    def __str__(self):
        return f'User №{self.id}'


class Education(models.Model):
    """
    Образование - для резюме
    """
    SECONDARY = 'SE'
    SECONDARY_SPECIAL = 'SSE'
    INCOMPLETE_HIGHER = 'IHE'
    HIGHER = 'HE'
    BACHELOR = 'BE'
    MASTER = 'ME'
    CANDIDATE_OF_SCIENCES = 'CSE'
    DOCTOR_OF_SCIENCES = 'DSE'
    LEVEL_CHOICES = (
        (SECONDARY, 'Среднее'),
        (SECONDARY_SPECIAL, 'Среднее специальное'),
        (INCOMPLETE_HIGHER, 'Неоконченное высшее'),
        (HIGHER, 'Высшее'),
        (BACHELOR, 'Бакалавр'),
        (MASTER, 'Магистр'),
        (CANDIDATE_OF_SCIENCES, 'Кандидат наук'),
        (DOCTOR_OF_SCIENCES, 'Доктор наук'),
    )
    level = models.CharField(max_length=3, choices=LEVEL_CHOICES, default='SR', verbose_name='Варниант занятости')
    educational_institution = models.CharField(max_length=150, blank=True, verbose_name='Учебное заведение')
    faculty = models.CharField(max_length=150, blank=True, verbose_name='Факультет')
    specialization = models.CharField(max_length=150, blank=True, verbose_name='Специализация')
    year_graduation = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Год окончания')

    def __str__(self):
        return f'User №{self.id}'


class AdvancedTraining(models.Model):
    """
    Повышение квалификации, курсы - для резюме
    """
    course_name = models.CharField(max_length=150, blank=True, verbose_name='Название курса')
    organization_conducted = models.CharField(max_length=150, blank=True, verbose_name='Проводившая организация')
    specialization = models.CharField(max_length=150, blank=True, verbose_name='Специализация')
    year_graduation = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Год окончания')

    def __str__(self):
        return f'User №{self.id}'


class Resume(models.Model):
    candidate = models.ForeignKey(Candidate,
                                  on_delete=models.CASCADE,
                                  null=True, blank=True,
                                  verbose_name='Владелец резюме')
    contact_info = models.ForeignKey(ContactInfo,
                                     on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     verbose_name='Контактная информация')
    position_and_selery = models.ForeignKey(PositionAndSelery,
                                            on_delete=models.SET_NULL,
                                            null=True, blank=True,
                                            verbose_name='Желаемая должность и зарплата')
    work_experience = models.ForeignKey(WorkExperience,
                                        on_delete=models.SET_NULL,
                                        null=True, blank=True,
                                        verbose_name='Опыт работы')
    education = models.ForeignKey(Education,
                                  on_delete=models.SET_NULL,
                                  null=True, blank=True,
                                  verbose_name='Образованеие')
    advanced_training = models.ForeignKey(AdvancedTraining,
                                          on_delete=models.SET_NULL,
                                          null=True, blank=True,
                                          verbose_name='Повышение квалификации, курсы')

    def __str__(self):
        return f'User №{self.id}'
