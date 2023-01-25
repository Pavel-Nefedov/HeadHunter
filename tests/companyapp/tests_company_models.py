from django.test import TestCase
from companyapp.models import CompanyProfile, Vacancy
from authapp.models import HHUser


class CompanyProfileModelTest(TestCase):

    @classmethod
    def setUpTestData(self):
        self.test_user = HHUser.objects.create(first_name='Max', 
                            last_name='Trent')
        self.test_user.save()

        self.company = CompanyProfile.objects.create(
                            user=self.test_user,
                            company_name='Avito',
                            legal_entity='ООО',
                            company_address='Moscow, Lesnaya st.7',
                            email='support@avito.ru',
                            phone_number='+7 (495) 228-36-30',
                            about_company='IT')

        self.vacancy = Vacancy.objects.create(
                            company=self.company,
                            vacancy_name='Python developer',
                            city='Moscow',
                            duties_description='Code review',
                            requirements_description='Work experience 1-3 years',
                            work_conditions='Full time',
                            # created=,
                            salary_min=1000,
                            salary_max=2000,
                            currency='USD',
                            is_active=False)
    
    
    # @classmethod
    # def test_company_user_get(self):
    #     self.test_user_1 = HHUser.objects.create(first_name='Max', 
    #                         last_name='Power')
    #     self.test_user_1.save()
    #     company = CompanyProfile.objects.get(user=self.test_user_1)
    #     self.assertEqual(company, self.company)
    
    def test_company_name_get(self):
        company = CompanyProfile.objects.get(company_name='Avito')
        self.assertEqual(company, self.company)
    
    def test_company_legal_entity_get(self):
        company = CompanyProfile.objects.get(legal_entity='ООО')
        self.assertEqual(company, self.company)

    def test_company_address_get(self):
        company = CompanyProfile.objects.get(company_address='Moscow, Lesnaya st.7')
        self.assertEqual(company, self.company)

    def test_company_email_get(self):
        company = CompanyProfile.objects.get(email='support@avito.ru')
        self.assertEqual(company, self.company)

    def test_company_phone_number_get(self):
        company = CompanyProfile.objects.get(phone_number='+7 (495) 228-36-30')
        self.assertEqual(company, self.company)

    def test_company_about_get(self):
        company = CompanyProfile.objects.get(about_company='IT')
        self.assertEqual(company, self.company)

    def test_vacancy_name_get(self):
        vacancy = Vacancy.objects.get(vacancy_name='Python developer')
        self.assertEqual(vacancy, self.vacancy)
    
    def test_vacancy_city_get(self):
        vacancy = Vacancy.objects.get(city='Moscow')
        self.assertEqual(vacancy, self.vacancy)

    def test_vacancy_duties_get(self):
        vacancy = Vacancy.objects.get(duties_description='Code review')
        self.assertEqual(vacancy, self.vacancy)

    def test_vacancy_requirements_get(self):
        vacancy = Vacancy.objects.get(requirements_description='Work experience 1-3 years')
        self.assertEqual(vacancy, self.vacancy)

    def test_vacancy_conditions_get(self):
        vacancy = Vacancy.objects.get(work_conditions='Full time')
        self.assertEqual(vacancy, self.vacancy)

    # def test_vacancy_created_get(self):
    #     vacancy = Vacancy.objects.get(created=)
    #     self.assertEqual(vacancy, self.vacancy)

    def test_vacancy_salary_min_get(self):
        vacancy = Vacancy.objects.get(salary_min=1000)
        self.assertEqual(vacancy, self.vacancy)

    def test_vacancy_salary_max_get(self):
        vacancy = Vacancy.objects.get(salary_max=2000)
        self.assertEqual(vacancy, self.vacancy)

    def test_vacancy_currency_get(self):
        vacancy = Vacancy.objects.get(currency='USD')
        self.assertEqual(vacancy, self.vacancy)
    
    def test_vacancy_active_get(self):
        vacancy = Vacancy.objects.get(is_active=False)
        self.assertEqual(vacancy, self.vacancy)

    def test_vacancy_is_disabled_get(self):
        is_for_disabled = False
        Vacancy.is_for_disabled = True
        self.assertNotEqual(is_for_disabled, Vacancy.is_for_disabled)

    def test_vacancy_is_full_day_get(self):
        is_full_day = True
        Vacancy.is_full_day = True
        self.assertEqual(is_full_day, Vacancy.is_full_day)

    def test_vacancy_is_intern_get(self):
        is_intern = False
        Vacancy.is_intern = False
        self.assertEqual(is_intern, Vacancy.is_intern)