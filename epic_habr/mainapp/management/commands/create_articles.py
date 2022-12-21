import json
import os
import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from mainapp.models import Article, Hub
from userapp.models import User


JSON_PATH = 'common/fixtures'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-16') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        articles = load_from_json('articles')
        hubs = load_from_json('hubs')
        Hub.objects.all().delete()
        Article.objects.all().delete()
        for hub in hubs:
            print(hub)
            new_hub = Hub(**hub)
            new_hub.save()
        hubs_num = Hub.objects.count()
        for article in articles:
            hubs = [hub for hub in random.choices(Hub.objects.all(), k=random.randint(1, 5))]
            article['author'] = random.choice(User.objects.all())
            new_article = Article(**article)
            new_article.save()
            new_article.hubs.set(hubs)
            print(article)


