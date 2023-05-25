import json

from base_classes.file_interface_base_class import FileInterfaceBaseClass

from parsers.headhunter_parser import HeadHunterParser
from parsers.superjob_parser import SuperJobParser


class HeadHunterFileProcessor(FileInterfaceBaseClass):
    """
    Класс для работы с файлами вакансий, полученных через API
    """
    def __init__(self):
        self.search_keyword = None
        self.experience = None
        self.schedule = None
        self.area = None
        self.salary = None

    def save_vacancies_to_file(self,
                               search_keyword=None,
                               experience=None,
                               schedule=None,
                               area=None,
                               salary=None
                               ) -> None:
        """
        Сохраняет полученный список словарей с данными вакансий в json-файл
        :param search_keyword: ключевое слово для поиска в полях вакансий
        :type search_keyword: str
        :param experience: опциональный параметр,
        означает требуемый опыт, указывается id из справочника,
        получаемый методом get_additional_dicts()
        :type experience: str
        :param schedule: опциональный параметр,
        означает график работы,указывается id из справочника,
        получаемый методом get_additional_dicts()
        :type schedule: str
        :param area: опциональный параметр, означает регион,
        указывается id из справочника, получаемый методом get_area_dicts()
        :type area: str
        :param salary: опциональный параметр, означает размер зарплаты
        :type salary: int
        :return: None
        :rtype: None
        """

        with open("vacancies_headhunter.json", "w", encoding="UTF-8") as file:
            data = HeadHunterParser().get_vacancies_data(
                search_keyword=search_keyword,
                experience=experience,
                schedule=schedule,
                area=area,
                salary=salary
            )
            json.dump(data, file, indent=2, ensure_ascii=False)

    def load_vacancies_from_file(self) -> list[dict]:
        """
        Загружает список словарей с данными вакансий из json-файла
        :return: список словарей с данными вакансий
        :rtype: list[dict]
        """
        with open("vacancies_headhunter.json", "r", encoding="UTF-8") as file:
            open_file = json.load(file)
            return open_file

    def delete_vacancy_from_file(self, vacancy_id: str) -> None:
        """
        Удаляет вакансию из файла по id вакансии
        :param vacancy_id: id вакансии
        :type vacancy_id: str
        :return: None
        :rtype: None
        """
        data: list[dict] = self.load_vacancies_from_file()

        with open(f"vacancies_headhunter.json", "w+", encoding="UTF-8") as file:
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

#
class SuperJobFileProcessor(FileInterfaceBaseClass):
    """
    Класс для работы с файлами вакансий, полученных через API
    """
    def __init__(self, ):
        self.search_keyword = None
        self.experience = None
        self.place_of_work = None
        self.town = None
        self.payment_from = None

    def save_vacancies_to_file(self,
                               search_keyword=None,
                               experience=None,
                               place_of_work=None,
                               town=None,
                               payment_from=None
                               ) -> None:
        """
        Сохраняет полученный список словарей с данными вакансий в json-файл
        :param search_keyword: ключевое слово для поиска в полях вакансий
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
        :return: None
        :rtype: None
        """
        with open(f"vacancies_superjob.json", "w", encoding="UTF-8") as file:
            data = SuperJobParser().get_vacancies_data(
                search_keyword=search_keyword,
                experience=experience,
                place_of_work=place_of_work,
                town=town,
                payment_from=payment_from,
            )
            json.dump(data, file, indent=2, ensure_ascii=False)

    def load_vacancies_from_file(self) -> dict:
        """
        Загружает словарь с данными вакансий из json-файла
        :return: словарь с данными вакансий
        :rtype: dict
        """
        with open(f"vacancies_superjob.json", "r", encoding="UTF-8") as file:
            open_file = json.load(file)
            return open_file

    def delete_vacancy_from_file(self, vacancy_id: int):
        """
        Удаляет вакансию из файла по id вакансии
        :param vacancy_id: id вакансии
        :type vacancy_id: int
        :return: None
        :rtype: None
        """
        data = self.load_vacancies_from_file()

        with open(f"vacancies_superjob.json", "w", encoding="UTF-8") as file:
            for item in data["objects"]:
                try:
                    if item["id"] == int(vacancy_id):
                        item_index = data["objects"].index(item)
                        del data["objects"][item_index]
                        print(f"Вакансия id={vacancy_id} удалена")
                        break
                    else:
                        print(f"Вакансия id={vacancy_id} не найдена")
                        break
                except TypeError as e:
                    e = "id вакансии должен быть целым числом"
                    print(e)
            json.dump(data, file, indent=2, ensure_ascii=False)
