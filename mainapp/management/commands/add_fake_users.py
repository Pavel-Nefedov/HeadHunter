from django.core.management import BaseCommand
from faker import Faker

from authapp.models import HHUser


class Command(BaseCommand):
    faker = Faker()

    def add_arguments(self, app):
        app.add_argument(
            'number_of_fake_users',
            type=int,
            help='Number of fake users',
        )

    def generate_fake_users(
            self,
            number_of_users: int,
            is_company: bool = False,
            is_candidate: bool = False
    ) -> None:
        for fake_user in range(number_of_users):
            temp_first_name = self.faker.first_name()
            temp_username = temp_first_name + self.faker.bothify(text='-????')
            fake_password = self.faker.color_name()

            HHUser.objects.create_user(
                username=temp_username,
                email=self.faker.ascii_free_email(),
                password=fake_password,
                first_name=temp_first_name,
                last_name=self.faker.last_name(),
                is_company=is_company,
                is_candidate=is_candidate,
            )
            print(
                f"\tUser {temp_first_name} :: ({is_company=}, {is_candidate=}) created [login: {temp_username} password: {fake_password}]")

    def handle(self, *args, **options):
        print(" Start adding fake user data ".center(79, '-'))
        number_of_fake_users = options['number_of_fake_users']

        # Generate company profiles
        self.generate_fake_users(number_of_fake_users, is_company=True)

        print("-".center(79, '-'))

        # Generate candidate profiles
        self.generate_fake_users(number_of_fake_users, is_company=True)

        print(" End adding fake user data ".center(79, '-'))
