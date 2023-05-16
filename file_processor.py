import json

from base_classes.file_interface_base_class import FileInterfaceBaseClass

from parsers.headhunter_parser import HeadHunterParser
from parsers.superjob_parser import SuperJobParser


class FileProcessor(FileInterfaceBaseClass):
    api_service = None
    search_keyword = None

    def __init__(self, api_service, search_keyword, experience=None, schedule=None, area=None):
        self.api_service = api_service
        self.search_keyword = search_keyword,
        self.experience = experience
        self.schedule = schedule
        self.area = area

    def save_vacancies_to_file(self):
        with open(f"vacancies_{self.api_service}.json", "w", encoding="UTF-8") as file:
            if self.api_service == "HeadHunter":
                data = HeadHunterParser().get_vacancies_data(
                    search_keyword=self.search_keyword,
                    experience=self.experience,
                    schedule=self.schedule,
                    area=self.area
                )
            if self.api_service == "SuperJob":
                data = SuperJobParser().get_vacancies_data(
                    search_keyword=self.search_keyword,
                    experience=self.experience,
                    schedule=self.schedule,
                    area=self.area
                )
            json.dump(data, file, indent=2, ensure_ascii=False)

    def load_vacancies_from_file(self):
        pass

    def delete_vacancy_from_file(self):
        pass
