from abc import ABC, abstractmethod


class BaseApiParser(ABC):
    """
    Базовый класс получения данных по API
    """

    @abstractmethod
    def get_vacancies_data(self, **kwargs):
        """
        Абстрактный метод получения данных по API
        :param kwargs: именованные аргументы для параметризации запроса к API
        :return: данные вакансий от из API
        :rtype: dict[list], list
        """
        pass



