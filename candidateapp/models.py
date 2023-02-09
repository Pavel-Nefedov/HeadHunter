from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from authapp.models import HHUser
from mainapp.models import AppCanvasModel


class MovingChoices(models.TextChoices):
    POSSIBLE = 'PO', _('возможен')
    IMPOSSIBLE = 'IM', _('невозможен')
    UNDESIRABLE = 'UN', _('нежелателен')


class BusinessTripChoices(models.TextChoices):
    IMPOSSIBLE = 'NR', _('не готов')
    POSSIBLE = 'RE', _('готов')
    NOT_FREQUENT = 'SO', _('не частые командировки')


class LaborBusinessChoices(models.TextChoices):
    FULL = 'FE', _('полная занятость')
    PARTIAL = 'PE', _('частичная занятость')
    PROJECT_WORK = 'PW', _('проектная работа')
    VOLUNTEERING = 'V', _('волонтерство')
    INTERNSHIP = 'I', _('стажировка')


class WorkScheduleChoices(models.TextChoices):
    FULL_TIME = 'FD', _('полный день')
    SHIFT_SCHEDULE = 'SS', _('сменный график')
    FLEXIBLE_SCHEDULE = 'FS', _('гибкий график')
    REMOTE = 'DW', _('удаленная работа')


class EducationLevelChoices(models.TextChoices):
    SECONDARY = 'SE', _('Среднее')
    SECONDARY_SPECIAL = 'SSE', _('Среднее специальное')
    INCOMPLETE_HIGHER = 'IHE', _('Неоконченное высшее')
    HIGHER = 'HE', _('Высшее')
    BACHELOR = 'BE', _('Бакалавр')
    MASTER = 'ME', _('Магистр')
    CANDIDATE_OF_SCIENCES = 'CSE', _('Кандидат наук')
    DOCTOR_OF_SCIENCES = 'DSE', _('Доктор наук')


class Resume(AppCanvasModel):
    is_moderated = models.BooleanField(default=False, verbose_name='Резюме прошло модерацию')
    candidate = models.ForeignKey(HHUser,
                                  unique=False, null=False, db_index=True, on_delete=models.CASCADE,
                                  verbose_name='Владелец резюме')
    moving = models.CharField(max_length=2, choices=MovingChoices.choices,
                              default=MovingChoices.IMPOSSIBLE,
                              verbose_name='Возможен ли переезд')

    business_trips = models.CharField(max_length=2, choices=BusinessTripChoices.choices,
                                      default=BusinessTripChoices.IMPOSSIBLE,
                                      verbose_name='Командировки')
    """
    Желаемая должность и зарплата - для резюме
    """
    desired_position = models.CharField(blank=True, max_length=180, null=False, verbose_name='Желаемая должность')
    salary = models.IntegerField(blank=True, verbose_name='Зарплата')

    busyness = models.CharField(max_length=5, choices=LaborBusinessChoices.choices,
                                default=LaborBusinessChoices.FULL, verbose_name='Варниант занятости')
    work_schedule = models.CharField(max_length=5, choices=WorkScheduleChoices.choices,
                                     default=WorkScheduleChoices.FULL_TIME, verbose_name='График работы')
    """
        Опыт работы - для резюме
        """
    getting_started = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Начало работы')
    end_work = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Окончание работы')
    working = models.BooleanField(verbose_name='Работаю по настоящее время', default=False)
    organization = models.CharField(max_length=150, blank=True, verbose_name='Организация')
    post = models.CharField(max_length=150, blank=True, verbose_name='Должность')
    responsibilities = models.TextField(blank=True, verbose_name='Обязанности на рабочем месте')
    skills = models.TextField(blank=True, verbose_name='Ключевые навыки')
    about_me = models.TextField(blank=True, verbose_name='О себе')
    """
        Образование - для резюме
        """
    level = models.CharField(
        max_length=3,
        choices=EducationLevelChoices.choices,
        default=EducationLevelChoices.SECONDARY,
        verbose_name='Образование'
    )
    educational_institution = models.CharField(max_length=150, blank=True, verbose_name='Учебное заведение')
    faculty = models.CharField(max_length=150, blank=True, verbose_name='Факультет')
    specialization = models.CharField(max_length=150, blank=True, verbose_name='Специализация')
    year_graduation = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Год окончания')
    """
       Повышение квалификации, курсы - для резюме
       """
    course_name = models.CharField(max_length=150, blank=True, verbose_name='Название курса')
    organization_conducted = models.CharField(max_length=150, blank=True, verbose_name='Проводившая организация')
    specialization_course = models.CharField(max_length=150, blank=True, verbose_name='Специализация')
    year_graduation_course = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Год окончания')

    is_draft = models.BooleanField(default=False, verbose_name='Черновик')


    def __str__(self):
        return f"Резюме {self.candidate.username}"



# class Candidate(models.Model):
#     """
#     search_area - район/область поиска работы
#     """
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     # profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
#     email = models.EmailField(max_length=128)
#     phone_number = models.CharField(max_length=12)
#     search_area = models.CharField(verbose_name='Адрес', max_length=256)
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'


# class ContactInfo(models.Model):
#     """
#     Модель контактной информации для резюме
#     """
#     # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
#     name = models.CharField(blank=True, max_length=30, null=False, verbose_name='Имя')
#     surname = models.CharField(blank=True, max_length=30, null=False, verbose_name='Фамилия')
#     patronymic = models.CharField(blank=True, max_length=30, null=False, verbose_name='Отчество')
#     birthday = models.DateField(blank=True, max_length=30, default=date.today, verbose_name='Дата рождения')
#     city = models.CharField(blank=True, max_length=180, null=False, verbose_name='Город')
#     GENDER_CHOICES = (
#         ('W', 'Женщина'),
#         ('M', 'Мужчина'),
#     )
#     MOVING_CHOICES = (
#         ('PO', 'возможен'),
#         ('IM', 'невозможен'),
#         ('UN', 'нежелателен'),
#     )
#     BUSINESS_TRIPS_CHOICES = (
#         ('NR', 'не готов'),
#         ('RE', 'готов'),
#         ('SO', 'иногда'),
#     )
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, verbose_name='Гендер')
#     moving = models.CharField(max_length=2, choices=MOVING_CHOICES, blank=True, verbose_name='Возможен ли переезд')
#     business_trips = models.CharField(max_length=2, choices=BUSINESS_TRIPS_CHOICES, blank=True,
#                                       verbose_name='Командировки')
#
#     def __str__(self):
#         return f'User №{self.id}'


# class PositionAndSalary(models.Model):
#     """
#     Желаемая должность и зарплата - для резюме
#     """
#     desired_position = models.CharField(blank=True, max_length=180, null=False, verbose_name='Желаемая должность')
#     salary = models.IntegerField(blank=True, verbose_name='Зарплата')
#     BUSYNESS_CHOICES = (
#         ('FE', 'полная занятость'),
#         ('PE', 'частичная занятость'),
#         ('PW', 'проектная работа'),
#         ('V', 'волонтерство'),
#         ('I', 'стажировка'),
#     )
#     WORK_SCHEDULE = (
#         ('FD', 'полный день'),
#         ('SS', 'сменный график'),
#         ('FS', 'гибкий график'),
#         ('DW', 'удаленная работа'),
#         ('SM', 'вахтовый метод'),
#     )
#     busyness = models.CharField(max_length=5, choices=BUSYNESS_CHOICES, blank=True, verbose_name='Варниант занятости')
#     work_schedule = models.CharField(max_length=5, choices=WORK_SCHEDULE, blank=True, verbose_name='График работы')
#
#     def __str__(self):
#         return f'User №{self.id}'


# class WorkExperience(models.Model):
#     """
#     Опыт работы - для резюме
#     """
#     getting_started = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Начало работы')
#     end_work = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Окончание работы')
#     working = models.BooleanField(verbose_name='Работаю по настоящее время')
#     organization = models.CharField(max_length=150, blank=True, verbose_name='Организация')
#     post = models.CharField(max_length=150, blank=True, verbose_name='Должность')
#     responsibilities = models.TextField(blank=True, verbose_name='Обязанности на рабочем месте')
#     skills = models.TextField(blank=True, verbose_name='Ключевые навыки')
#     about_me = models.TextField(blank=True, verbose_name='О себе')
#
#     def __str__(self):
#         return f'User №{self.id}'


# class Education(models.Model):
#     """
#     Образование - для резюме
#     """
#     SECONDARY = 'SE'
#     SECONDARY_SPECIAL = 'SSE'
#     INCOMPLETE_HIGHER = 'IHE'
#     HIGHER = 'HE'
#     BACHELOR = 'BE'
#     MASTER = 'ME'
#     CANDIDATE_OF_SCIENCES = 'CSE'
#     DOCTOR_OF_SCIENCES = 'DSE'
#     LEVEL_CHOICES = (
#         (SECONDARY, 'Среднее'),
#         (SECONDARY_SPECIAL, 'Среднее специальное'),
#         (INCOMPLETE_HIGHER, 'Неоконченное высшее'),
#         (HIGHER, 'Высшее'),
#         (BACHELOR, 'Бакалавр'),
#         (MASTER, 'Магистр'),
#         (CANDIDATE_OF_SCIENCES, 'Кандидат наук'),
#         (DOCTOR_OF_SCIENCES, 'Доктор наук'),
#     )
#     level = models.CharField(max_length=3, choices=LEVEL_CHOICES, default='SR', verbose_name='Образование')
#     educational_institution = models.CharField(max_length=150, blank=True, verbose_name='Учебное заведение')
#     faculty = models.CharField(max_length=150, blank=True, verbose_name='Факультет')
#     specialization = models.CharField(max_length=150, blank=True, verbose_name='Специализация')
#     year_graduation = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Год окончания')
#
#     def __str__(self):
#         return f'User №{self.id}'


# class AdvancedTraining(models.Model):
#     """
#     Повышение квалификации, курсы - для резюме
#     """
#     course_name = models.CharField(max_length=150, blank=True, verbose_name='Название курса')
#     organization_conducted = models.CharField(max_length=150, blank=True, verbose_name='Проводившая организация')
#     specialization = models.CharField(max_length=150, blank=True, verbose_name='Специализация')
#     year_graduation = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Год окончания')
#
#     def __str__(self):
#         return f'User №{self.id}'
