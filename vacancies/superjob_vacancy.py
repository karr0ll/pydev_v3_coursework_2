from file_processors.superjob_file_processor import SuperJobFileProcessor
from vacancies.headhunter_vacancy import HeadHunterVacancy


class SuperJobVacancy(HeadHunterVacancy):
    """
    Класс вакансии SuperJob, инициализируется любым из именованных аргументов
    """

    def __init__(self,
                 keyword: str = None,
                 experience: str = None,
                 town: int = None,
                 payment_from: int = None
                 ) -> None:
        """
        Конструктор класса, инициализируется одним из переданных именованных аргументов,
        дополнительные атрибуты заполняются данными из файла вакансий
        :param keyword: ключевое слово для поиска вакансий
        :type keyword: str
        :param experience: требуемый опыт для поиска вакансий
        :type experience: str
        :param town: город для поиска вакансий
        :type town: int
        :param payment_from: нижняя граница зарплаты
        :type payment_from: int
        """
        super().__init__()
        self.keyword = keyword
        self.experience = experience
        self.town = town
        self.payment_from = payment_from

        vacancy_data = self.__get_vacancy_data()
        for item in vacancy_data:
            try:
                self.employer_name: str = item["objects"]["client"]["title"]
                self.vacancy_name: str = item["objects"]["profession"]
                self.salary_from: int = item["objects"]["payment_from"]
                self.salary_to: int = item["objects"]["payment_to"]
                self.description: str = item["objects"]["candidat"]
                self.employment: str = item["objects"]["type_of_work"]["title"]
                self.url: str = item["objects"]["link"]
                self.all.append(self)

            except TypeError:
                for key, value in self.__dict__.items():
                    if value is None:
                        self.__dict__[key] = "не указано"

    def __get_vacancy_data(self) -> dict:
        """
        Метод получения данных из файла вакансий
        :return: данные из файла вакансий
        :rtype: dict
        """
        SuperJobFileProcessor().save_vacancies_to_file(
            text=self.text,
            experience=self.experience,
            area=self.area,
            salary=self.salary
        )
        vacancy_data: dict = SuperJobFileProcessor().load_vacancies_from_file()
        return vacancy_data


