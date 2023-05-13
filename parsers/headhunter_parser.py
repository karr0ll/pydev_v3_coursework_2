import requests

from base_classes.parser_base_class import BaseApiParser


class HeadHunterParser(BaseApiParser):

    def get_vacancies_data(self):
        headers = {
            "User-Agent": "api-test-agent",
        }
        response = requests.get(f"https://api.hh.ru/vacancies/", headers=headers)
        return response.json()
