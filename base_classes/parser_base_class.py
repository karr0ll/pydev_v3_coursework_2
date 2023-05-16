from abc import ABC, abstractmethod


class BaseApiParser(ABC):

    @abstractmethod
    def get_vacancies_data(self, search_keyword, experience=None, schedule=None, area=None) -> dict:
        pass



