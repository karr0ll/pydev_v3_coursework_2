from file_processors.headhunter_file_processors import HeadHunterFileProcessor


class HeadHunterVacancy:
    """
    Класс вакансий с HeadHunter, инициализируется любым из именованных аргументов
    """
    all = []

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
        if not isinstance(text, str):
            raise TypeError("Ключевое слово для поиска должно быть строкой")
        else:
            self.text = text

        if experience is not None:
            if not isinstance(experience, str):
                raise TypeError("Опыт работы для поиска долже быть строкой")
        else:
            self.experience = experience

        if not isinstance(area, str):
            raise TypeError("ID города для поиска долже быть строкой")
        else:
            self.area = area

        if not isinstance(salary, int):
            raise TypeError("Зарплата для поиска должны быть целым числом")
        else:
            self.salary = salary

        vacancy_data = self.__get_vacancy_data()
        for item in vacancy_data:
            self.employer_name: str = item["employer"]["name"]
            self.area: str = item["area"]["name"]
            self.vacancy_name: str = item["name"]
            self.salary_from: int = item["salary"]["from"]
            self.salary_to: int = item["salary"]["to"]
            self.requirement: str = item["snippet"]["requirement"]
            self.experience: str = item["experience"]["name"]
            self.description: str = item["snippet"]["responsibility"]
            self.employment: str = item["employment"]["name"]
            self.url: str = item["alternate_url"]

            self.all.append(self)

    # def __repr__(self) -> str:
    #     """
    #     Возвращает строковое представление экземпляра класса
    #     :return: строка с представлением экземпляра класса
    #     :rtype: str
    #     """
    #     return f"Компания: {self.employer_name}\nПозиция: {self.vacancy_name}, г.{self.area}\n" \
    #            f"Зарпалата: от {self.salary_from} до {self.salary_to} руб\n" \
    #            f"Требования к соискателю:\n{self.requirement}\n" \
    #            f"Опыт работы: {self.experience}\n" \
    #            f"Обязанности: {self.description}\n" \
    #            f"Тип занятости: {self.employment}\nСсылка на вакансию: {self.url}\n"

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
        HeadHunterFileProcessor().save_vacancies_to_file(
            text=self.text,
            experience=self.experience,
            area=self.area,
            salary=self.salary
        )
        vacancy_data: list[dict] = HeadHunterFileProcessor().load_vacancies_from_file()
        return vacancy_data





data = HeadHunterVacancy(text="python", salary=100_000, area="1")

print(data.all)
