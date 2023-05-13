import os

import requests
from dotenv import load_dotenv

from base_classes.parser_base_class import BaseApiParser


class SuperJobParser(BaseApiParser):

    def get_vacancies_data(self) -> dict:
        load_dotenv()
        api_token: str = os.environ.get("SJ_API_KEY")
        headers = {
            "X-Api-App-Id": f"{api_token}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.get(f"https://api.superjob.ru/2.0/vacancies/", headers=headers)
        return response.json()



