import datetime
import random
import time

from django.conf import settings
from django.core.management import BaseCommand
from django.db import transaction
from faker import Faker

from authapp.models import HHUser
from companyapp.models import CompanyProfile, Vacancy
from mainapp.services import FileMode, HHVacancyParser


class Command(BaseCommand):
    faker = Faker()

    user_info = []

    def add_arguments(self, app):
        app.add_argument(
            'number_of_fake_users',
            type=int,
            help='Number of fake users',
        )

    def __generate_fake_user(
            self,
            is_company: bool = False,
            is_candidate: bool = False
    ) -> HHUser:
        temp_first_name = self.faker.first_name()
        temp_username = temp_first_name + self.faker.bothify(text='-????')
        fake_password = self.faker.color_name()

        some_user = HHUser.objects.create_user(
            username=temp_username,
            email=self.faker.ascii_free_email(),
            password=fake_password,
            first_name=temp_first_name,
            last_name=self.faker.last_name(),
            is_company=is_company,
            is_candidate=is_candidate,
        )

        information = f"{'Company' if is_company is True else 'Candidate'} user {temp_first_name} created [login: {temp_username} password: {fake_password}]"

        print(information)
        self.user_info.append(information)

        return some_user

    def __generate_fake_company_profile(self, company_user: HHUser) -> CompanyProfile:
        company_name = self.faker.company()

        this_profile = CompanyProfile.objects.create(
            user=company_user,
            company_name=company_name,
            legal_entity=f"ООО {company_name}",
            company_address=self.faker.address(),
            email=self.faker.ascii_company_email(),
            phone_number=self.faker.msisdn(),
            about_company=self.faker.paragraph(nb_sentences=3),
        )

        print(f"\tCreated profile for company {company_name}")

        return this_profile

    def __generate_fake_vacancy(self, company_profile: CompanyProfile, vacancy_data: dict,
                                verbose: bool = False) -> None:

        if vacancy_data['salary'] is None:
            vacancy_data.update({'salary': {
                'from': None,
                'to': None,
                'currency': None,
            }})

        if verbose:
            print('/////////////////////')
            print(f"https://api.hh.ru/vacancies/{vacancy_data['id']}")
            print(f"{vacancy_data['name']=}")
            print(f"{vacancy_data['area']['name']=}")
            print(f"requirements_description={', '.join([item['name'] for item in vacancy_data['key_skills']])}")
            print(f"{vacancy_data['published_at']=}")
            print(f"salary_min={vacancy_data['salary']['from']=}")
            print(f"salary_max={vacancy_data['salary']['to']=}")
            print(f"currency={vacancy_data['salary']['currency']=}")
            print('/////////////////////')

        Vacancy.objects.create(
            company=company_profile,
            vacancy_name=vacancy_data['name'],
            city=vacancy_data['area']['name'],
            duties_description=vacancy_data['description'],
            requirements_description=', '.join([item['name'] for item in vacancy_data['key_skills']]),
            created=datetime.datetime.strptime(vacancy_data['published_at'], '%Y-%m-%dT%H:%M:%S%z'),
            salary_min=None if vacancy_data['salary'][
                                   'from'] is None else int(
                vacancy_data['salary']['from']
            ),
            salary_max=None if vacancy_data['salary'][
                                   'to'] is None else int(
                vacancy_data['salary']['to']
            ),
            currency=vacancy_data['salary']['currency'],
            is_active=True,
        )
        print(f"\t\t - Created vacancy '{vacancy_data['name']}'")

    def handle(self, *args, **options):

        max_number_of_vacancies_for_user = 4
        number_of_fake_users: int = options['number_of_fake_users']
        count_of_vacansy: int = number_of_fake_users * max_number_of_vacancies_for_user

        print(" Start vacancy parse ".center(79, '-'))
        job_opening = HHVacancyParser(count_of_vacansy=count_of_vacansy, search_text='python').get_vacancy_data()

        print(" Start adding fake user data ".center(79, '-'))
        # Generate company profiles
        for fake_user in range(number_of_fake_users):
            print("-".center(79, '-'))
            with transaction.atomic():
                temp_user = self.__generate_fake_user(is_company=True)

                temp_profile = self.__generate_fake_company_profile(company_user=temp_user)

                for item in range(random.randint(1, max_number_of_vacancies_for_user)):
                    this_vacancy = job_opening.pop()
                    self.__generate_fake_vacancy(
                        company_profile=temp_profile,
                        vacancy_data=this_vacancy
                    )
                print("-".center(79, '-'))

        # Generate candidate profiles
        for fake_user in range(number_of_fake_users):
            self.__generate_fake_user(is_candidate=True)

        # Safe user fake data to file
        fake_user_data_dir = settings.BASE_DIR / 'mainapp' / 'management' / 'data'
        if not fake_user_data_dir.is_dir():
            fake_user_data_dir.mkdir()

        fake_user_data_file = fake_user_data_dir / f'{time.time()}_fake_users_data.txt'

        with open(
                fake_user_data_file,
                mode=FileMode.WRITE.value,
                encoding=settings.PROJECT_ENCODING
        ) as info_file:
            for item in self.user_info:
                info_file.write(f"{item}\n")

        print(f"Fake user data store in file {fake_user_data_file}")

        print(" End adding fake user data ".center(79, '-'))
