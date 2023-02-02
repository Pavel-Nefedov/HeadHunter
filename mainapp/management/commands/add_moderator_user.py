import os

from django.core.management import BaseCommand
from django.db import IntegrityError

from authapp.models import HHUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        moderator_login = os.getenv("DJANGO_MODERATOR_USERNAME", default='moderator')
        moderator_password = os.getenv("DJANGO_MODERATOR_PASSWORD", default='123')
        moderator_email = os.getenv("DJANGO_MODERATOR_EMAIL", default='moderator_no@mail.com')

        print(" Start add moderator user ".center(79, '-'))

        try:
            HHUser.objects.create_user(
                username=moderator_login,
                first_name='Модератор',
                last_name='Модератович',
                password=moderator_password,
                email=moderator_email,
                is_moderator=True,
            )
            print(f" Added moderator user".center(79, '-'))
            print(f"\tLogin: {moderator_login}")
            print(f"\tPassword: {moderator_password}")

        except IntegrityError as inst:
            print(f"Moderator user now is not added.")
            for item in inst.args:
                print(f"{item}")
            print(f"Maybe he is already exists. Check in DB.")
