import json

from base_classes.file_interface_base_class import FileInterfaceBaseClass

from parsers.headhunter_parser import HeadHunterParser


class HeadHunterFileProcessor(FileInterfaceBaseClass):
    """
    Класс для работы с файлами вакансий, полученных через API
    """

    def save_vacancies_to_file(self, **kwargs) -> None:
        """
        Сохраняет полученный послемаппинга список словарей с данными вакансий в json-файл
        :param kwargs: опциональные параметры запроса к API: text, salary, area, experience
        :type kwargs: text: str, salary: int, area: str, experience: str
        :return:  None
        :rtype: None
        """
        with open("vacancies_headhunter.json", "w", encoding="UTF-8") as file:
            data = self.map_json_data(**kwargs)
            json.dump(data, file, indent=2, ensure_ascii=False)

    @staticmethod
    def map_json_data(**kwargs) -> list[dict]:
        """
        Маппит полученный от API список словарей с данными вакансий.
        :param kwargs: опциональные параметры запроса к API: text, salary, area, experience
        :type kwargs: text: str, salary: int, area: str, experience: str
        :return:  None
        :rtype: None
        """
        data: list[dict] = HeadHunterParser().get_vacancies_data(**kwargs)
        formatted_dicts_list = []
        for item in data:
            formatted_dicts_list.append(
                {
                    "service": "HeadHunter",
                    "id": item["id"],
                    "name": item["name"],
                    "city": {
                        "id": item["area"]["id"],
                        "name": item["area"]["name"]
                    },
                    "salary_from": item["salary"]["from"],
                    "salary_to": item["salary"]["to"],
                    "url": item["alternate_url"],
                    "employer": item["employer"]["name"],
                    "requirement": item["snippet"]["requirement"],
                    "responsibility": item["snippet"]["responsibility"],
                    "experience": {
                        "id": item["experience"]["id"],
                        "name": item["experience"]["name"]
                    },
                    "employment": {
                        "id": item["employment"]["id"],
                        "name": item["employment"]["name"]
                    }

                }
            )
        return formatted_dicts_list

    def load_vacancies_from_file(self) -> list[dict]:
        """
        Загружает список словарей с данными вакансий из json-файла
        :return: список словарей с данными вакансий
        :rtype: list[dict]
        """
        with open("vacancies_headhunter.json", "r", encoding="UTF-8") as file:
            vacancies_data: list[dict] = json.load(file)
            return vacancies_data

    def delete_vacancy_from_file(self, vacancy_id: str) -> None:
        """
        Удаляет вакансию из файла по id вакансии
        :param vacancy_id: id вакансии
        :type vacancy_id: str
        :return: None
        :rtype: None
        """
        data: list[dict] = self.load_vacancies_from_file()

        with open("vacancies_headhunter.json", "w+",
                  encoding="UTF-8"
                  ) as file:

            for item in data:
                if item["id"] == str(vacancy_id):
                    item_index = data.index(item)
                    del data[item_index]
                    print(f"Вакансия id={vacancy_id} удалена")
                    break
                else:
                    print(f"Вакансия id={vacancy_id} не найдена")
                    break
            json.dump(data, file, indent=2, ensure_ascii=False)
