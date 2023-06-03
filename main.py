from file_processors.all_vacancies_file_processor import AllVacanciesFileProcessor
from file_processors.headhunter_file_processor import HeadHunterFileProcessor
from file_processors.superjob_file_processor import SuperJobFileProcessor
from utils import get_search_experience_id, get_city_id
from vacancies.all_vacancies import AllVacancies
from vacancies.headhunter_vacancy import HeadHunterVacancy
from vacancies.superjob_vacancy import SuperJobVacancy


def interact_with_user():
    # этап выбора сервиса поиска работы
    api_service_index = int(
        input(
            "Здравствуйте, вводом номера выберите сервис поиска вакансий:\n "
            "1. HeadHunter 2.SuperJob 3.Оба сервиса\n"
        )
    )
    while api_service_index not in range(1, 4) or not isinstance(api_service_index, int):
        print("Необходимо ввести номер опции (1/2/3)")
        api_service_index = int(input())

    print("Введите параметры поиска (ключевое слово для поиска, опыт работы, зарплату, город):")
    search_keyword = input("Ключевое слово: ")
    search_salary = int(input("Зарплата: "))

    # этап выбора искомого опыта работы

    experience_index_input = int(input("1. Нет опыта / 2. От 1 года до 3 лет / 3. От 3 до 6 лет / 4. Более 6 лет\n"))
    while experience_index_input not in range(1, 5) or not isinstance(experience_index_input, int):
        print("Необходимо ввести номер опции")
        experience_index_input = int(input())

    search_city = input("Город: ").capitalize()
    top_chart_size = int(input("Введите количество вакансий в топе для отображения:\n"))

    #  получение списка id опыта работы по введенному индексу
    search_experience_list: list = get_search_experience_id(experience_index_input)

    #  получение id города из ввода пользователя
    city_data_list: list = get_city_id(search_city)

    if api_service_index == 1:
        HeadHunterFileProcessor().save_vacancies_to_file(
            filename="vacancies_hh.json",
            text=search_keyword,
            experience=search_experience_list[0],
            area=city_data_list[0],
            salary=search_salary
        )
        vacancies: list[dict] = HeadHunterFileProcessor().load_vacancies_from_file(filename="vacancies_hh.json")

        all_hh_vacancies: list[HeadHunterVacancy] = [
            HeadHunterVacancy(
                employer_name=item["employer"],
                area=item["city"]["name"],
                vacancy_name=item["name"],
                salary_from=item["salary_from"],
                salary_to=item["salary_to"],
                requirement=item["requirement"],
                experience=item["experience"]["name"],
                description=item["responsibility"],
                employment=item["employment"]["name"],
                url=item["url"]
            ) for item in vacancies]

        sorted_vacancies: list[HeadHunterVacancy] = sorted(
            all_hh_vacancies,
            key=lambda cls_object: cls_object.salary_from,
            reverse=True
        )

    elif api_service_index == 2:
        SuperJobFileProcessor().save_vacancies_to_file(
            filename="vacancies_sj.json",
            keyword=search_keyword,
            experience=search_experience_list[1],
            town=city_data_list[1],
            payment_from=search_salary
        )

        vacancies: list[dict] = SuperJobFileProcessor().load_vacancies_from_file(filename="vacancies_sj.json")
        all_sj_vacancies: list[SuperJobVacancy] = [
            SuperJobVacancy(
                employer_name=item["employer"],
                area=item["city"]["name"],
                vacancy_name=item["name"],
                salary_from=item["salary_from"],
                salary_to=item["salary_to"],
                requirement=item["requirement"],
                experience=item["experience"]["name"],
                description=item["responsibility"],
                employment=item["employment"]["name"],
                url=item["url"]
            ) for item in vacancies
        ]

        sorted_vacancies: list[SuperJobVacancy] = sorted(
            all_sj_vacancies,
            key=lambda cls_object: cls_object.salary_from,
            reverse=True
        )

    else:
        search_experience_hh = search_experience_list[0]
        city_id_hh = city_data_list[0]

        HeadHunterFileProcessor().save_vacancies_to_file(
            filename="vacancies_hh.json",
            text=search_keyword,
            experience=search_experience_hh,
            area=city_id_hh,
            salary=search_salary
        )

        search_experience_sj = search_experience_list[1]
        city_id_sj = city_data_list[1]

        SuperJobFileProcessor().save_vacancies_to_file(
            filename="vacancies_sj.json",
            keyword=search_keyword,
            experience=search_experience_sj,
            town=city_id_sj,
            payment_from=search_salary
        )

        AllVacanciesFileProcessor().save_vacancies_to_file(
            filename="vacancies_all.json",
            hh_filename="vacancies_hh.json",
            sj_filename="vacancies_sj.json"
        )
        vacancies: list[dict] = AllVacanciesFileProcessor().load_vacancies_from_file(
            filename="vacancies_all.json"
        )

        all_vacancies: list[AllVacancies] = [
            AllVacancies(
                service=item["service"],
                employer_name=item["employer"],
                area=item["city"]["name"],
                vacancy_name=item["name"],
                salary_from=item["salary_from"],
                salary_to=item["salary_to"],
                requirement=item["requirement"],
                experience=item["experience"]["name"],
                description=item["responsibility"],
                employment=item["employment"]["name"],
                url=item["url"]
            ) for item in vacancies
        ]
        sorted_vacancies: list[AllVacancies] = sorted(
            all_vacancies,
            key=lambda cls_object: cls_object.salary_from,
            reverse=True
        )
    print(f"Топ-{top_chart_size} вакансий по начальной зарплате:\n")
    for vacancy in sorted_vacancies[0:top_chart_size]:
        print(vacancy)


if __name__ == "__main__":
    interact_with_user()
