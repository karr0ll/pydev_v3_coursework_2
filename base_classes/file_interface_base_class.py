from abc import ABC, abstractmethod


class FileInterfaceBaseClass(ABC):
    """
    Базовый класс для работы с файлами вакансий
    """

    @abstractmethod
    def save_vacancies_to_file(self):
        """
        Абстрактный метод сохранения информации в файл
        Returns: None

        """
        pass

    @abstractmethod
    def load_vacancies_from_file(self):
        """
        Абстрактный метод загрузки информации из файла
        Returns: None

        """
        pass

    @abstractmethod
    def delete_vacancy_from_file(self, vacancy_id):
        """
        Абстрактный метод удаления информации из файла по id вакансии
        Params: id вакансии
        Returns: None

        """
        pass
