from abc import ABC, abstractmethod


class FileInterfaceBaseClass(ABC):
    """
    Базовый класс для работы с файлами вакансий
    """

    @abstractmethod
    def save_vacancies_to_file(self, **kwargs):
        """
        Абстрактный метод сохранения информации в файл
        :param kwargs: именованные аргументы для параметризации запроса к API
        :type kwargs: int, str, array
        :return: None
        :rtype: None
        """
        pass

    @abstractmethod
    def load_vacancies_from_file(self):
        """
        Абстрактный метод загрузки информации из файла
        :return: None
        :rtype: None
        """
        pass

    @abstractmethod
    def delete_vacancy_from_file(self, vacancy_id):
        """
        Абстрактный метод удаления информации из файла по id вакансии
        :param vacancy_id: id вакансии для удаления из файла
        :type vacancy_id: int, str
        :return: None
        :rtype: None
        """
        pass
