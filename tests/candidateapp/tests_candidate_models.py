from django.test import TestCase
from authapp.models import HHUser
from candidateapp.models import Candidate, ContactInfo, PositionAndSelery, WorkExperience, \
                                Education, AdvancedTraining, Resume


class CandidateModelTestLength(TestCase):

    @classmethod
    def setUpTestData(cls):
        Candidate.objects.create()
        ContactInfo.objects.create()
        # PositionAndSelery.objects.create()
        # WorkExperience.objects.create()
        # Education.objects.create()
        # AdvancedTraining.objects.create()
        # Resume.objects.create()

    def test_max_length_candidate(self):
        candidate = Candidate.objects.get(id=1)
        max_length_name = candidate._meta.get_field('first_name').max_length
        max_length_last_name = candidate._meta.get_field('last_name').max_length
        max_length_email = candidate._meta.get_field('email').max_length
        max_length_phone = candidate._meta.get_field('phone_number').max_length
        max_length_area = candidate._meta.get_field('search_area').max_length
        self.assertEquals(max_length_name, 30)
        self.assertEquals(max_length_last_name, 30)
        self.assertEquals(max_length_email, 128)
        self.assertEquals(max_length_phone, 12)
        self.assertEquals(max_length_area, 256)

    def test_get_absolute_url(self):
        candidate = Candidate.objects.get(id=1)
        self.assertEquals(candidate.get_absolute_url(), '/candidate/user_profile/1')

    def test_max_length_contactinfo(self):
        candidate = ContactInfo.objects.get(id=1)
        max_length_name = candidate._meta.get_field('name').max_length
        max_length_surname = candidate._meta.get_field('surname').max_length
        max_length_patronymic = candidate._meta.get_field('patronymic').max_length
        max_length_birthday = candidate._meta.get_field('birthday').max_length
        max_length_city = candidate._meta.get_field('city').max_length
        self.assertEquals(max_length_name, 30)
        self.assertEquals(max_length_surname, 30)
        self.assertEquals(max_length_patronymic, 30)
        self.assertEquals(max_length_birthday, 30)
        self.assertEquals(max_length_city, 180)


    # def test_max_length_PositionAndSelery(self):
    #     candidate = PositionAndSelery.objects.get(id=1)
    #     max_length_desired_position = candidate._meta.get_field('desired_position').max_length
    #     self.assertEquals(max_length_desired_position, 180)

    # def test_max_length_WorkExperience(self):
    #     candidate = WorkExperience.objects.get(id=1)
    #     max_length_organization = candidate._meta.get_field('organization').max_length
    #     max_length_post = candidate._meta.get_field('post').max_length
    #     self.assertEquals(max_length_organization, 150)
    #     self.assertEquals(max_length_post, 150)






    # def setUp(self):
    #     self.candidate = Candidate.objects.create(first_name='Имя',
    #                                               last_name='Фамилия',
    #                                               email='Почтовый адрес',
    #                                               phone_number='Номер телефона',
    #                                               search_area='Адрес')

        # self.contactInfo = ContactInfo.objects.create(name='Имя',
        #                                               surname='Фамилия',
        #                                               patronymic='Отчество',
        #                                               birthday='2000-01-01',
        #                                               city='Город',
        #                                               gender='Пол',
        #                                               moving='Переезд',
        #                                               business_trips='Командировки')

        # self.position = PositionAndSelery.objects.create(desired_position='',
        #                                                  salary='',
        #                                                  busyness='',
        #                                                  work_schedule='')
        #
        # self.work = WorkExperience.objects.create(getting_started='',
        #                                           end_work='',
        #                                           busyness='',
        #                                           working='',
        #                                           organization='',
        #                                           post='',
        #                                           responsibilities='',
        #                                           skills='',
        #                                           about_me='')
        #
        # self.education = Education.objects.create(level='',
        #                                           educational_institution='',
        #                                           faculty='',
        #                                           specialization='',
        #                                           year_graduation='')
        #
        # self.advanced = AdvancedTraining.objects.create(course_name='',
        #                                                 organization_conducted='',
        #                                                 specialization='',
        #                                                 year_graduation='')
        #
        # self.resume = Resume.objects.create(contact_info='',
        #                                     position_and_selery='',
        #                                     work_experience='',
        #                                     education='',
        #                                     advanced_training='')



    # def test_title_label_contactInfo(self):
    #     '''Проверка заполнения verbose_name'''
    #     field_verboses = {'name': 'Имя',
    #                       'surname': 'Фамилия',
    #                       'patronymic': 'Отчество',
    #                       'birthday': 'Дата рождения',
    #                       'city': 'Город',
    #                       'gender': 'Гендер',
    #                       'moving': 'Возможен ли переезд',
    #                       'business_trips': 'Командировки'}
    #     for field, expected_value in field_verboses.items():
    #         with self.subTest(field=field):
    #             error_name = f'Поле {field} ожидало значение {expected_value}'
    #             self.assertEqual(
    #                 self.contactInfo._meta.get_field(field).verbose_name,
    #                 expected_value, error_name)

    # @classmethod
    # def setUpTestData(cls):
    #     Candidate.objects.create()
    #
    # def test_first_name_label(self):
    #     candidate = Candidate.objects.get(id=1)
    #     field_label = candidate._meta.get_field('first_name').verbose_name
    #     self.assertEquals(field_label, 'first name')
    #
    # def test_last_name_label(self):
    #     candidate = Candidate.objects.get(id=1)
    #     field_label = candidate._meta.get_field('last_name').verbose_name
    #     self.assertEquals(field_label, 'last name')
    #
    # def test_first_name_max_length(self):
    #     candidate = Candidate.objects.get(id=1)
    #     max_length = candidate._meta.get_field('first_name').max_length
    #     self.assertEquals(max_length, 30)
    #
    # def test_last_name_max_length(self):
    #     candidate = Candidate.objects.get(id=1)
    #     max_length = candidate._meta.get_field('last_name').max_length
    #     self.assertEquals(max_length, 30)
    #
    # def test_get_absolute_url(self):
    #     candidate = Candidate.objects.get(id=1)
    #     self.assertEquals(candidate.get_absolute_url(), '/candidate/user_profile/1')
