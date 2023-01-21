from django.test import TestCase
from mainapp.models import News


class NewsModelTest(TestCase):

    @classmethod
    def setUpTestData(self):
        self.news_1 = News.objects.create(title='Starting 2023 with momentum, thanks to you!',
                link='https://pyfound.blogspot.com/2023/01/starting-2023-with-momentum-thanks-to.html',
                date='2023-10-01', 
                description='Test news')

    def test_news_title_get(self):
        news_1 = News.objects.get(title='Starting 2023 with momentum, thanks to you!')
        self.assertEqual(news_1, self.news_1)

    def test_news_link_get(self):
        news_1 = News.objects.get(link='https://pyfound.blogspot.com/2023/01/starting-2023-with-momentum-thanks-to.html')
        self.assertEqual(news_1, self.news_1)

    def test_news_date_get(self):
        news_1 = News.objects.get(date='2023-10-01')
        self.assertEqual(news_1, self.news_1)

    def test_news_description_get(self):
        news_1 = News.objects.get(description='Test news')
        self.assertEqual(news_1, self.news_1)