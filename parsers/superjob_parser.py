import os

import requests
from dotenv import load_dotenv

from base_classes.parser_base_class import BaseApiParser

from datetime import datetime, timedelta


class SuperJobParser(BaseApiParser):
    """
    Класс получения данных по API SuperJob
    """

    def get_vacancies_data(self,
                           search_keyword,
                           experience=None,
                           place_of_work=None,
                           town=None,
                           payment_from=None
                           ) -> dict:
        """
        Получает отфильтрованные данные по вакансии по API SuperJob
        :param search_keyword: ключевое слово для поиска
        :type search_keyword: str
        :param experience: опциональный параметр,
        означает требуемый опыт, указывается id из справочника,
        получаемый методом get_additional_dicts()
        :type experience: int
        :param place_of_work: тип работы (в офисе/удаленно и пр.).
        Опциональный параметр, означает требуемый опыт,
        указывается id из справочника,
        получаемый методом get_additional_dicts()
        :type place_of_work: int
        :param town: опциональный параметр,
        означает id города поиска вакансии,
        получается из справочника через метод
        get_towns_dict()
        :type town: int
        :param payment_from: нижняя граница вилки зарплаты
        :type payment_from: int
        :return: словарь с данными по вакансиям
        :rtype: dict
        """
        load_dotenv()
        api_token: str = os.environ.get("SJ_API_KEY")
        headers = {
            "X-Api-App-Id": f"{api_token}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        params = {
            "count": 100,
            "page": 0,
            "date_published_from": datetime.today() - timedelta(days=30),
            "keyword": search_keyword,
            "experience": experience,
            "place_of_work": place_of_work,
            "town": town,
            "payment_from": payment_from

        }
        response = requests.get("https://api.superjob.ru/2.0/vacancies/",
                                params=params,
                                headers=headers
                                )
        all_vacancies = response.json()["objects"]
        vacancies_left = True

        #  цикл получения всех вакансий,
        #  выполняется, пока не получим от API 'more': False
        while vacancies_left:
            response = requests.get("https://api.superjob.ru/2.0/vacancies/",
                                    params=params,
                                    headers=headers
                                    )
            params["page"] += 1
            all_vacancies.extend(response.json()["objects"])

            # цикл закончился
            vacancies_left = response.json()["more"]
        return response.json()

    def get_additional_dicts(self) -> dict:
        """
        Получает словарь со справочниками
        дополнительных параметров запросов к API
        :return: словарь со справочниками
        :rtype: dict
        """
        load_dotenv()
        api_token: str = os.environ.get("SJ_API_KEY")
        headers = {
            "X-Api-App-Id": f"{api_token}",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.get("https://api.superjob.ru/2.0/references/",
                                headers=headers
                                )
        additional_dicts = response.json()
        return additional_dicts

    def get_towns_dict(self) -> dict:
        """
        Получает словарь со справочниками городов
        :return: словарь со справочниками
        :rtype: dict
        """
        load_dotenv()
        api_token: str = os.environ.get("SJ_API_KEY")
        headers = {
            "X-Api-App-Id": f"{api_token}",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.get("https://api.superjob.ru/2.0/towns/?all=true",
                                headers=headers
                                )
        towns_dict = response.json()
        return towns_dict
