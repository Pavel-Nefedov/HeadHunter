from django.test import TestCase
from authapp.models import HHUser


class HHUserModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Создаём тестовую запись в БД
        # и сохраняем созданную запись в качестве переменной класса
        cls.user = HHUser.objects.create_user(username='username',
                                              first_name='Name',
                                              last_name='Lastname',
                                              password='password',
                                              email='Email',
                                              patronymic="Patronymic",
                                              is_company=True,
                                              is_candidate=False,
                                              is_moderator=False
                                              )

    def test_title_label_HHUser(self):
        '''Проверка заполнения verbose_name'''
        field_verboses = {
                          'first_name': 'first name',
                          'last_name': 'last name',
                          'password': 'password',
                          'email': 'email address',
                          'patronymic': 'Отчество',
                          'is_company': 'Является компанией',
                          'is_candidate': 'Является соискателем',
                          'is_moderator': 'Является модератором'
                          }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                error_name = f'Поле {field} ожидало значение {expected_value}'
                self.assertEqual(
                    self.user._meta.get_field(field).verbose_name,
                    expected_value, error_name)

    def test_title_help_text(self):
        '''Проверка заполнения help_text'''
        field_help_texts = {'is_company': 'Отметьте, если пользователь находится в роли работодателя',
                            'is_candidate': 'Отметьте, если пользователь находится в роли соискателя',
                            'is_moderator': 'Отметьте, если пользователь находится в роли модератора'}
        for field, expected_value in field_help_texts.items():
            with self.subTest(field=field):
                error_name = f'Поле {field} ожидало значение {expected_value}'
                self.assertEqual(
                    self.user._meta.get_field(field).help_text,
                    expected_value, error_name)

    def test_models_have_correct_object_names(self):
        '''Проверка __str__'''
        error_name = f"Error username"
        self.assertEqual(self.user.__str__(),
                         self.user.username,
                         error_name)

    def test_max_length(self):
        user = HHUser.objects.get(id=1)
        max_length_name = user._meta.get_field('first_name').max_length
        max_length_last_name = user._meta.get_field('last_name').max_length
        max_length_password = user._meta.get_field('password').max_length
        self.assertEquals(max_length_name, 150)
        self.assertEquals(max_length_last_name, 150)
        self.assertEquals(max_length_password, 128)


