import json

from file_processors.headhunter_file_processor import HeadHunterFileProcessor
from file_processors.superjob_file_processor import SuperJobFileProcessor


class CombinationFileProcessor:

    def save_vacancies_to_file(self):
        hh_data = HeadHunterFileProcessor().load_vacancies_from_file()
        sj_data = SuperJobFileProcessor().load_vacancies_from_file()
        with open("vacancies_all.json", "w", encoding="UTF-8") as file:
            combined_data = []
            for item in zip(hh_data, sj_data):
                for dict in item:
                    combined_data.append(dict)

            json.dump(combined_data, file, indent=2, ensure_ascii=False)

    def load_vacancies_from_file(self) -> list[dict]:
        """
        Загружает список словарей с данными вакансий из json-файла
        :param filename: имя файла для открытия
        :type filename: str
        :return: список словарей с данными вакансий
        :rtype: dict
        """
        with open("vacancies_all.json", "r", encoding="UTF-8") as file:
            vacancies_data: list[dict] = json.load(file)
            return vacancies_data

    def delete_vacancy_from_file(self, *args, **kwargs) -> None:
        """
        Удаляет вакансию из файла по id вакансии
        :param vacancy_id: id вакансии
        :type vacancy_id: str
        :return: None
        :rtype: None
        """
        vacancy_id = kwargs["vacancy_id"]
        data: list[dict] = self.load_vacancies_from_file()

        with open("vacancies_all.json", "w+",
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