import json

from file_processors.headhunter_file_processors import HeadHunterFileProcessor

from parsers.superjob_parser import SuperJobParser


class SuperJobFileProcessor(HeadHunterFileProcessor):
    """
    Класс для работы с файлами вакансий, полученных через API
    """

    def save_vacancies_to_file(self, **kwargs) -> None:
        """
        Сохраняет полученный послемаппинга список словарей с данными вакансий в json-файл
        :param kwargs: опциональные параметры запроса к API: keyword, payment_from, town, experience
        :type kwargs: keyword: str, payment_from: int, town: int, experience: str
        :return:  None
        :rtype: None
        """
        with open("vacancies.json", "w", encoding="UTF-8") as file:
            data = self.map_json_data(**kwargs)
            json.dump(data, file, indent=2, ensure_ascii=False)

    @staticmethod
    def map_json_data(**kwargs) -> list[dict]:
        """
        Маппит полученный от API список словарей с данными вакансий.
        :param kwargs: опциональные параметры запроса к API: keyword, payment_from, town, experience
        :type kwargs: keyword: str, payment_from: int, town: int, experience: str
        :return:  None
        :rtype: None
        """
        data: dict = SuperJobParser().get_vacancies_data(**kwargs)
        formatted_dicts_list = []
        for item in data["objects"]:
            formatted_dicts_list.append(
                {
                    "service": "SuperJob",
                    "id": item["id"],
                    "name": item["profession"],
                    "city": {
                        "id": item["town"]["id"],
                        "name": item["town"]["title"]
                    },
                    "salary_from": item["payment_from"],
                    "salary_to": item["payment_to"],
                    "url": item["link"],
                    "employer": item["client"]["title"],
                    "requirement": None,
                    "responsibility": item["candidat"],
                    "experience": {
                        "id": item["experience"]["id"],
                        "name": item["experience"]["title"]
                    },
                    "employment": {
                        "id": item["type_of_work"]["id"],
                        "name": item["type_of_work"]["title"]
                    }
                }
            )
        return formatted_dicts_list

    def load_vacancies_from_file(self) -> list[dict]:
        """
        Загружает словарь с данными вакансий из json-файла
        :return: словарь с данными вакансий
        :rtype: dict
        """
        with open("vacancies.json", "r", encoding="UTF-8") as file:
            vacancies_data: list[dict] = json.load(file)
            return vacancies_data

    def delete_vacancy_from_file(self, vacancy_id: int) -> None:
        """
        Удаляет вакансию из файла по id вакансии
        :param vacancy_id: id вакансии
        :type vacancy_id: int
        :return: None
        :rtype: None
        """
        data: list[dict] = self.load_vacancies_from_file()

        with open("vacancies.json", "w", encoding="UTF-8") as file:
            for item in data:
                if item["id"] == int(vacancy_id):
                    item_index = data.index(item)
                    del data[item_index]
                    print(f"Вакансия id={vacancy_id} удалена")
                    break
                else:
                    print(f"Вакансия id={vacancy_id} не найдена")
                    break
            json.dump(data, file, indent=2, ensure_ascii=False)
