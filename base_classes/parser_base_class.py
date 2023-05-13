from abc import ABC, abstractmethod


class BaseApiParser(ABC):
    @abstractmethod
    def get_vacancies_data(self):
        pass



