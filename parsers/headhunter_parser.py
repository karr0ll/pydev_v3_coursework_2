import json

import requests

from base_classes.parser_base_class import BaseApiParser


class HeadHunterParser(BaseApiParser):
    """
    Класс получения данных по API HeadHunter
    """

    def get_vacancies_data(
                           self,
                           search_keyword,
                           experience=None,
                           schedule=None,
                           area=None,
                           salary=None
                           ) -> list[dict]:
        """
        Получает отфильтрованные данные по вакансии по API HeadHunter
        :param search_keyword: ключевое слово для поиска в полях вакансий
        :type search_keyword: str
        :param experience: опциональный параметр, означает требуемый опыт,
        указывается id из справочника, получаемый методом get_additional_dicts()
        :type experience: str
        :param schedule: опциональный параметр, означает график работы,
        указывается id из справочника, получаемый методом get_additional_dicts()
        :type schedule: str
        :param area: опциональный параметр, означает регион,
        указывается id из справочника, получаемый методом get_area_dicts()
        :type area: str
        :param salary: опциональный параметр, означает размер зарплаты
        :type salary: int
        :return: список словарей с данными по найденным вакансиям
        :rtype: list[dict]
        """

        params = {
            "per_page": 100,
            "page": 0,
            "period": 30,
            "text": search_keyword,
            "experience": experience,
            "schedule": schedule,
            "area": area,
            "salary": salary
        }
        response = requests.get("https://api.hh.ru/vacancies", params=params)
        if not response.status_code == 200:
            print(response.text)
        vacancies_description = response.json()["items"]

        # получение количества страниц из ответа
        pages = response.json()["pages"]

        for page in range(1, pages):

            # обновление номера страницы в запросе к API
            params["page"] = page
            response = requests.get("https://api.hh.ru/vacancies", params=params)
            vacancies_description.extend(response.json()["items"])
        return vacancies_description

    def get_additional_dicts(self) -> dict:
        """
        Получает справочник дополнительных параметров запросов к API
        :return: словарь с дополнительными параметрами для запросов к API
        :rtype: dict
        """
        response = requests.get("https://api.hh.ru/dictionaries")
        if not response.status_code == 200:
            print(response.text)
        additional_dicts = response.json()
        return additional_dicts

    def get_area_dicts(self) -> dict:
        """
        Получает справочник городов для запроса к API
        :return: словарь с справочником городов для запросов к API
        :rtype: dict
        """
        response = requests.get("https://api.hh.ru/areas")
        if not response.status_code == 200:
            print(response.text)
        area_dicts = response.json()
        return area_dicts
