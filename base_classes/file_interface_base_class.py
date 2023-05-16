from abc import ABC, abstractmethod


class FileInterfaceBaseClass(ABC):

    @abstractmethod
    def save_vacancies_to_file(self):
        pass

    @abstractmethod
    def load_vacancies_from_file(self, api_service):
        pass

    @abstractmethod
    def delete_vacancy_from_file(self, api_service):
        pass
