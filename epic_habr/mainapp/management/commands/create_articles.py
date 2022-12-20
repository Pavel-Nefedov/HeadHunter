import json
import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from mainapp.models import Article
from userapp.models import User


JSON_PATH = 'common/fixtures'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-16') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        articles = load_from_json('articles')
        Article.objects.all().delete()
        for article in articles:
            print(article)
            new_article = Article(**article)
            new_article.save()

