import json

import requests

from base_classes.parser_base_class import BaseApiParser

class HeadHunterParser(BaseApiParser):
    # def __init__(self, search_keyword):
    #     self.search_keyword = search_keyword

    def get_vacancies_data(self, search_keyword, experience=None, schedule=None, area=None) -> dict:
        params = {
            "per_page": 100,
            "page": 0,
            "period": 30,
            "text": search_keyword,
            "experience": experience,
            "schedule": schedule,
            "area": area
        }
        response = requests.get("https://api.hh.ru/vacancies", params=params)  # получение ответа
        vacancies_description = response.json()["items"]  # получение вакансий из ответа
        pages = response.json()["pages"]  # получение количества страниц из ответа

        for page in range(1, pages):
            params["page"] = page # обновление номера страницы в запросе к API
            response = requests.get("https://api.hh.ru/vacancies", params=params)
            vacancies_description.extend(response.json()["items"])

        return vacancies_description

