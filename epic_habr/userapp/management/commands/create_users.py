import json
import os
from mimesis import Person, Generic

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from userapp.models import User


JSON_PATH = 'common/fixtures'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-16') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = load_from_json('users')
        User.objects.all().delete()
        for user in users:
            new_user = User(**user)
            new_user.password = '12345678aA'
            print(user)
            new_user.save()
        super_user = User.objects.create_superuser('admin', 'admin@admin.ru', 'admin')
