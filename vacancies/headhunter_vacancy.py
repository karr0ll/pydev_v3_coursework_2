from file_processors.headhunter_file_processors import HeadHunterFileProcessor


class HeadHunterVacancy:
    """
    Класс вакансий с HeadHunter, инициализируется любым из именованных аргументов
    """
    all = []
    text: str = None
    experience: str = None
    area: str = None
    salary: int = None

    def __init__(self, text=None, experience=None, area=None, salary=None) -> None:
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
        self.text = text
        self.experience = experience
        self.area = area
        self.salary = salary

        vacancy_data = self.__get_vacancy_data()
        for item in vacancy_data:
            try:
                self.employer_name: str = item["employer"]["name"]
                self.vacancy_name: str = item["name"]
                self.salary_from: int = item["salary"]["from"]
                self.salary_to: int = item["salary"]["to"]
                self.requirement: str = item["snippet"]["requirement"]
                self.description: str = item["snippet"]["responsibility"]
                self.employment: str = item["employment"]["name"]
                self.url: str = item["alternate_url"]
                self.all.append(self)

            except TypeError:
                for key, value in self.__dict__.items():
                    if value is None:
                        self.__dict__[key] = "не указано"

    def __str__(self) -> str:
        """
        Возвращает строковое представление экземпляра класса
        :return: строка с представлением экземпляра класса
        :rtype: str
        """
        return f"Компания: {self.employer_name}\nПозиция: {self.vacancy_name}, г.{self.area}\n" \
               f"Зарпалата: {self.salary_from} - {self.salary_to} руб\n" \
               f"Требования к соискателю:\n{self.requirement}\n" \
               f"Опыт работы: {self.experience}\n" \
               f"Обязанности: {self.description}\n" \
               f"Тип занятости: {self.employment}\nСсылка на вакансию: {self.url} "

    def __repr__(self) -> str:
        """
        Возвращает строковое представление экземпляра класса
        :return: строка с представлением экземпляра класса
        :rtype: str
        """
        return f"Компания: {self.employer_name}\nПозиция: {self.vacancy_name}, г.{self.area}\n" \
               f"Зарпалата: {self.salary_from} - {self.salary_to} руб.\n" \
               f"Требования к соискателю:\n{self.requirement}\n" \
               f"Опыт работы: {self.experience}\n" \
               f"Обязанности: {self.description}\n" \
               f"Тип занятости: {self.employment}\nСсылка на вакансию: {self.url} "

    def __get_vacancy_data(self) -> list[dict]:
        """
        Метод получения данных из файла вакансий
        :return: данные из файла вакансий
        :rtype: list[dict]
        """
        HeadHunterFileProcessor().save_vacancies_to_file(
            text=self.text,
            experience=self.experience,
            area=self.area,
            salary=self.salary
        )
        vacancy_data: list[dict] = HeadHunterFileProcessor().load_vacancies_from_file()
        return vacancy_data




