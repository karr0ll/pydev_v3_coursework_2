import urllib.parse

import requests

from base_classes.parser_base_class import BaseApiParser


class HeadHunterParser(BaseApiParser):
    def __init__(self):
        self.query_params = {}

    @classmethod
    def query_params(cls) -> dict:
        cls.query_params = {}
        return cls.query_params

    def get_vacancies_data(self):
        headers = {
            "User-Agent": "api-test-agent",
        }
        params = self.query_params
        response = requests.get(f"https://api.hh.ru/vacancies", params, headers=headers)

        return response.json()