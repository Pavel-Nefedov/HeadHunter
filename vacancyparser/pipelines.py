# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class VacancyparserPipeline:
    pk_increment = 1

    def process_item(self, item, spider):
        data_dict = {
            "model": "companyapp.vacancy",
            "pk": self.pk_increment,
            "fields": {
                'name': item['name'],
                'salary': self.process_salary(item['salary']),
                'employer': item['employer'],
                'location': item['location'],
                'responsibility': item['responsibility'],
                'requirements': item['requirements'],
            }
        }
        try:
            with open('vacancies.json', 'a', encoding='utf-8') as json_file:
                line = json.dumps(data_dict, ensure_ascii=False, indent=4) + ","
                json_file.write(line)
        except TypeError:
            pass
        else:
            self.pk_increment += 1
        return item

    def process_salary(self, salary):
        res = []
        for i in salary:
            if i == 'до вычета налогов' or i == 'на руки' or i == 'з/п не указана':
                res.append(i)
            else:
                i = ''.join(i.split())
                res.append(i)
        return res
