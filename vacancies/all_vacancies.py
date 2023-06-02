from file_processors.all_vacancies_file_processor import CombinationFileProcessor


class AllVacancies:
    """
    Класс вакансий с HeadHunter, инициализируется любым из именованных аргументов
    """
    all = []

    def __init__(self, *args, **kwargs) -> None:
        """
        Конструктор класса, инициализируется одним из переданных именованных аргументов,
        дополнительные атрибуты заполняются данными из файла вакансий
        :param text: ключевое слово для поиска вакансий
        :type text: str
        :param experience: требуемый опыт для поиска вакансий
        :type experience: str
        :param area: город для поиска вакансий
        :type area: str
        :param salary: зарплата
        :type salary: int
        """
        vacancy_data = self.__get_vacancy_data(**kwargs)
        for item in vacancy_data:
            self.employer_name: str = item["employer"]
            self.area: str = item["city"]["name"]
            self.vacancy_name: str = item["name"]
            self.salary_from: int = item["salary_from"]
            self.salary_to: int = item["salary_to"]
            self.requirement: str = item["requirement"]
            self.experience: str = item["experience"]["name"]
            self.description: str = item["responsibility"]
            self.employment: str = item["employment"]["name"]
            self.url: str = item["url"]

            self.all.append(self)

    def __repr__(self) -> str:
        """
        Возвращает строковое представление экземпляра класса
        :return: строка с представлением экземпляра класса
        :rtype: str
        """
        return f"Компания: {self.employer_name}\nПозиция: {self.vacancy_name}, г.{self.area}\n" \
               f"Зарпалата: от {self.salary_from} до {self.salary_to} руб\n" \
               f"Требования к соискателю:\n{self.requirement}\n" \
               f"Опыт работы: {self.experience}\n" \
               f"Обязанности: {self.description}\n" \
               f"Тип занятости: {self.employment}\nСсылка на вакансию: {self.url}\n"

    def __str__(self) -> str:
        """
        Возвращает строковое представление экземпляра класса
        :return: строка с представлением экземпляра класса
        :rtype: str
        """
        return f"Компания: {self.employer_name}\nПозиция: {self.vacancy_name}, г.{self.area}\n" \
               f"Зарпалата: от {self.salary_from} до {self.salary_to} руб\n" \
               f"Требования к соискателю:\n{self.requirement}\n" \
               f"Опыт работы: {self.experience}\n" \
               f"Обязанности: {self.description}\n" \
               f"Тип занятости: {self.employment}\nСсылка на вакансию: {self.url}\n"

    def __ge__(self, other):
        return self.salary_from > other.salary_from

    def __get_vacancy_data(self) -> list[dict]:
        """
        Метод получения данных из файла вакансий
        :return: данные из файла вакансий
        :rtype: list[dict]
        """
        CombinationFileProcessor().save_vacancies_to_file()
        vacancy_data: list[dict] = CombinationFileProcessor().load_vacancies_from_file()
        return vacancy_data
