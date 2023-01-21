from django.test import TestCase
from companyapp.models import CompanyProfile, Vacancy
from authapp.models import HHUser


class CompanyProfileModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = HHUser.objects.create(first_name='Max', 
                            last_name='Trent')
        test_user.save()

        CompanyProfile.objects.create(user=test_user,
                            company_name='Avito',
                            legal_entity='ООО',
                            company_address='Moscow, Lesnaya st.7',
                            email='support@avito.ru',
                            phone_number='+7 (495) 228-36-30',
                            about_company='IT')
        
    def test_company_name_get(self):
        company_1 = CompanyProfile.objects.get(id=1)
        self.assertEqual(company_1, self.company_1)

'''
    def test_company_name_label(self):
        company = CompanyProfile.objects.get(id=1)
        field_label = company._meta.get_field('company_name').verbose_name
        self.assertEquals(field_label, 'company_name')
'''
