import os

import requests
from dotenv import load_dotenv

from base_classes.parser_base_class import BaseApiParser


class SuperJobParser(BaseApiParser):
    def __init__(self):
        self.query_params = {}

    @classmethod
    def query_params(cls) -> dict:
        cls.query_params = {}
        return cls.query_params

    def get_vacancies_data(self) -> dict:
        load_dotenv()
        api_token: str = os.environ.get("SJ_API_KEY")
        headers = {
            "X-Api-App-Id": f"{api_token}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        params = self.query_params
        response = requests.get("https://api.superjob.ru/2.0/vacancies/", params, headers=headers)
        return response.json()

# site = SuperJobParser()
# print(site.get_vacancies_data())
#
# site.query_params = {"payment_from": 30000,
#                      "payment_to": 30000}
#
# print(site.get_vacancies_data())

