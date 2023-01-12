import scrapy
from scrapy.http import HtmlResponse
from vacancyparser.items import VacancyparserItem

class VacancyhhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['https://hh.ru/search/vacancy?text=python&area=1&salary=&currency_code=RUR&experience=doesNotMatter&'
                  'order_by=relevance&search_period=0&items_on_page=20&no_magic=true&L_save_area=true']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath("//a[@class='serp-item__title']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):
        name = response.css("h1::text").get()
        salary = response.xpath("//div[@data-qa='vacancy-salary']//text()").getall()
        employer = response.xpath("//a[@data-qa='vacancy-serp__vacancy-employer']/text()").get()
        location = response.xpath("//div[@data-qa='vacancy-serp__vacancy-address']/text()").get()
        responsibility = response.xpath("//div[@data-qa='vacancy-serp__vacancy_snippet_responsibility']/text()").get()
        requirements = response.xpath("//div[@data-qa='vacancy-serp__vacancy_snippet_requirement']/text()").get()
        yield VacancyparserItem(name=name, salary=salary, employer=employer, location=location,
                                responsibility=responsibility, requirements=requirements)