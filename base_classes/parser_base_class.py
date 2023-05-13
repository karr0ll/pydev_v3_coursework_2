from abc import ABC, abstractmethod


class BaseApiParser(ABC):

    @abstractmethod
    def query_params(self):
        pass

    @abstractmethod
    def get_vacancies_data(self):
        pass



