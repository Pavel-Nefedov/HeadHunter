import json
import os
from mimesis import Person, Generic

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from mimesis.enums import Locale
from mimesis.enums import Gender

from userapp.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        g = Generic(locale=Locale.RU)
        gender_dict = {'Муж.': Gender.MALE,
                       'Жен.': Gender.FEMALE}
        for _ in range(3):
            gender = g.person.gender()
            gender = gender_dict[gender]
            user = {
                'username': g.person.username(),
                'password': g.person.password(),
                'first_name': g.person.first_name(gender=gender),
                'last_name': g.person.last_name(gender=gender),
                'email': g.person.email(),
            }
            new_user = User(**user)
            print(user)
            new_user.save()
