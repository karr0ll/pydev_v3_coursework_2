import os

import requests
from dotenv import load_dotenv

from base_classes.parser_base_class import BaseApiParser

from datetime import datetime, timedelta


class SuperJobParser(BaseApiParser):

    def get_vacancies_data(self, search_keyword, experience=None, schedule=None, area=None) -> dict:
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
            "place_of_work": schedule,
            "town": area

        }
        response = requests.get("https://api.superjob.ru/2.0/vacancies/", params=params, headers=headers)
        all_vacancies = response.json()["objects"]
        vacancies_left = True

        #  цикл выполняется, пока не получим от API 'more': False
        while vacancies_left is True:
            response = requests.get("https://api.superjob.ru/2.0/vacancies/", params=params, headers=headers)
            params["page"] += 1
            all_vacancies.extend(response.json()["objects"])
            vacancies_left = response.json()["more"]  # цикл закончился

        return response.json()
