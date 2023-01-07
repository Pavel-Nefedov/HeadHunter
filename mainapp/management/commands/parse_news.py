from django.core.management import BaseCommand
from django.db import IntegrityError

from mainapp.models import News
from mainapp.services import HHNewsScrapper


class Command(BaseCommand):
    def handle(self, *args, **options):
        print(" Start getting news from news site ".center(79, '-'))
        news_list = HHNewsScrapper().det_list_of_news_dto()
        print(" Add news in DB ".center(79, '-'))
        counter = 0
        for news in news_list:
            try:
                News.objects.create(
                    title=news.news_title,
                    link=news.news_link,
                    date=news.news_date,
                    description=news.news_description,
                )
                counter += 1
            except IntegrityError:
                print(f'---> News with title "{news.news_title}" already exists')
        print(f" Added {counter} news".center(79, '-'))
