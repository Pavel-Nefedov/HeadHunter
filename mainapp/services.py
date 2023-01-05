import locale
import time
from abc import ABC, abstractmethod
from datetime import datetime

import requests
from lxml.html import fromstring


class Status:
    """HTTP statuses"""

    NOT_FOUND_404 = 404
    OK_200 = 200


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
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }

    def __init__(self, url: str):
        self.url = url

    def __get_response_text(self):
        response = requests.get(self.url, headers=self.HEADERS)
        if response.status_code != Status.OK_200:
            raise ConnectionError(
                f"HTTP status not 200. Server return "
                f"{response.status_code} status code for "
                f"url {self.url}"
            )
        return response.text

    @staticmethod
    def get_response_text(url: str):
        return HTTPResponse(url).__get_response_text()


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
        dom = fromstring(HTTPResponse.get_response_text(self.URL_FOR_SCRAPING))

        items = dom.xpath(self.MAIN_NEWS_XPATH)
        for item in items:
            item_news_title = item.xpath(self.PART_NEWS_TITLE_XPATH)[0]
            item_news_link = self.BASE_URL + item.xpath(self.PART_NEWS_HREF_XPATH)[0]
            item_news_date, item_news_description = self.__get_news_date_description_and_content(
                item_news_link
            )

            self._news_list.append(
                NewsItemDTO(
                    news_title=item_news_title,
                    news_link=item_news_link,
                    news_date=item_news_date,
                    news_description=item_news_description,
                )
            )

    def __get_news_date_description_and_content(self, link_to_news: str):
        """Get news source from news site by news link"""
        description_xpath = "//div[contains(@class, 'cms-lead cms-lead_alt')]//text()"
        datetime_xpath = (
            "//span[contains(@class, 'cms-header-content__date')]//text()"
        )
        time.sleep(1)
        dom = fromstring(HTTPResponse.get_response_text(link_to_news))

        return (
            datetime.strptime(dom.xpath(datetime_xpath)[0].title(), "%d %B %Y"),
            dom.xpath(description_xpath)[0],
        )

    def det_list_of_news_dto(self) -> list:
        return self._news_list


if __name__ == "__main__":
    print("This is service file. You must include her as module.")
