import locale
import time
from abc import ABC, abstractmethod
from concurrent.futures import Future, ThreadPoolExecutor
from datetime import datetime
from enum import Enum
from typing import List

import requests
from lxml.html import fromstring
from tqdm import tqdm


class Status:
    """HTTP statuses"""

    NOT_FOUND_404 = 404
    OK_200 = 200


class FileMode(Enum):
    """ DTO for file mod  """
    READ = "r"
    WRITE = "w"
    APPEND_WRITE = "a"


class AbstractScrapper(ABC):
    _news_list = []

    def __init__(self):
        print(f"Начал работать {self.__class__}")

    @abstractmethod
    def start_scraping(self):
        """Start scraping process."""
        pass


class NewsItemDTO:
    """DTO class for one news"""

    def __init__(
            self, news_title: str, news_link: str, news_date: datetime, news_description: str,
    ):
        self.news_title = news_title
        self.news_link = news_link
        self.news_date = news_date
        self.news_description = news_description

    def __str__(self):
        return (
            f"News: {self.news_title}, in link {self.news_link}, date {self.news_date}"
        )

    def __repr__(self):
        return (
            f"NewsItemDTO({self.news_title}, {self.news_link},"
            f" {self.news_date}, {self.news_description})"
        )


class HTTPResponse:
    def __init__(self, url: str, response_headers=None, response_params=None):
        self.url = url
        self.headers = response_headers
        self.params = response_params

    def __get_response(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        if response.status_code != Status.OK_200:
            print(f"{self.url=}\n{self.headers=}\n{self.params}")
            raise ConnectionError(
                f"HTTP status not 200. Server return "
                f"{response.status_code} status code for "
                f"url {self.url}"
            )
        return response

    @staticmethod
    def get_response(url: str, headers=None, params=None):
        return HTTPResponse(url, headers, params).__get_response()


class HHNewsScrapper(AbstractScrapper):
    """Mail news scrapper"""

    BASE_URL = "https://hh.ru"
    URL_FOR_SCRAPING = "https://hh.ru/articles"

    MAIN_NEWS_XPATH = (
        '//div[contains(@class, "cms-announce-tiles")]/a'
    )
    PART_NEWS_HREF_XPATH = "./@href"
    PART_NEWS_TITLE_XPATH = "./span[contains(@class, 'bloko-link')]//text()"

    def __init__(self):
        locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
        super().__init__()
        self.start_scraping()

    def start_scraping(self):
        """Start scraping process."""
        request_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
        }

        dom = fromstring(HTTPResponse.get_response(url=self.URL_FOR_SCRAPING, headers=request_headers).text)

        items = dom.xpath(self.MAIN_NEWS_XPATH)
        for item in tqdm(items):
            item_news_title = item.xpath(self.PART_NEWS_TITLE_XPATH)[0]
            item_news_link = self.BASE_URL + item.xpath(self.PART_NEWS_HREF_XPATH)[0]
            item_news_date, item_news_description = self.__get_news_date_description_and_content(
                item_news_link,
                request_headers,
            )

            self._news_list.append(
                NewsItemDTO(
                    news_title=item_news_title,
                    news_link=item_news_link,
                    news_date=item_news_date,
                    news_description=item_news_description,
                )
            )

    def __get_news_date_description_and_content(self, link_to_news: str, request_headers):
        """Get news source from news site by news link"""
        description_xpath = "//div[contains(@class, 'cms-lead cms-lead_alt')]//text()"
        datetime_xpath = (
            "//span[contains(@class, 'cms-header-content__date')]//text()"
        )
        time.sleep(1)
        dom = fromstring(HTTPResponse.get_response(link_to_news, headers=request_headers).text)

        return (
            datetime.strptime(dom.xpath(datetime_xpath)[0].title(), "%d %B %Y"),
            dom.xpath(description_xpath)[0],
        )

    def det_list_of_news_dto(self) -> list:
        return self._news_list


class HHVacancyParser:
    BASE_URL = "https://api.hh.ru/vacancies"

    thread_pool_executor = ThreadPoolExecutor(max_workers=4)

    def __init__(self, count_of_vacansy: int = 10, search_text: str = ''):
        self.headers = {
            "Content-Type": "application/json",
        }

        self.params = {
            'per_page': count_of_vacansy,
            'text': search_text
        }
        try:
            with HTTPResponse.get_response(self.BASE_URL, headers=self.headers, params=self.params) as get_request:
                # Получим список с id вакансий
                vacancy_ids = [vacancy_id['id'] for vacancy_id in get_request.json()['items']]
        except ConnectionError:
            raise ValueError(
                f'Too many vacancies count in param count_of_vacansy. '
                f'Please specify a smaller number then {count_of_vacansy}. '
                f'Maximum 100.'
            )
        self.vacancy_data: list = []
        futeres_responce: List[Future] = []
        for vacancy_id in vacancy_ids:
            futeres_responce.append(
                self.thread_pool_executor.submit(self.__get_vacancy_data_for_id, vacancy_id)
            )

        print(f"Starting {len(vacancy_ids)} asynchrone requests to HH API. Wait please")

        flag: bool = True
        while flag:
            if all([futures.done() for futures in futeres_responce]):
                flag = False

        self.vacancy_data = [futures.result() for futures in futeres_responce]

    # Пройдемся по списку id и получим полные данные по каждой вакансии
    def __get_vacancy_data_for_id(self, vacancy_id: str) -> list:
        with HTTPResponse.get_response(f"{self.BASE_URL}/{vacancy_id}", headers=self.headers) as get_request:
            return get_request.json()

    def get_vacancy_data(self):
        self.thread_pool_executor.shutdown()
        return self.vacancy_data


if __name__ == "__main__":
    print("This is service file. You must include her as module.")

    print(HHVacancyParser(count_of_vacansy=1, search_text='python').get_vacancy_data())
