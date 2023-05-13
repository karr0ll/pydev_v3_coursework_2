from base_classes.parser_base_class import BaseApiParser
class Vacancy:
    employer_name = None
    vacancy_name = None
    city = None
    salary = None
    currency = None
    url = None
    schedule = None

    def __init__(self, employer_name, vacancy_name, city, salary_from, currency, url, schedule):
        vacancy_data = BaseApiParser.get_vacancies_data()
        self.employer_name = BaseApiParser.get_vacancies_data()
        self.vacancy_name = vacancy_name
        self.city = city
        self.salary_from = salary_from
        self.currency = currency
        self.url = url
        self.schedule = schedule

    def __gt__(self, other):
        return self.salary_from > other.salary_from





