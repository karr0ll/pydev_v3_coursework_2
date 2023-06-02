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

    if api_service_index == 1:
        #  получение id опыта работы по введенному индексу
        search_experience = get_search_experience_id(experience_index_input, api_service_index)

        #  получение id города из ввода пользователя
        city_id = get_city_id(api_service_index, search_city)
        vacancies = HeadHunterVacancy(
            text=search_keyword,
            experience=search_experience,
            area=city_id,
            salary=search_salary
        )

    if api_service_index == 2:
        #  получение id опыта работы по введенному индексу
        search_experience = get_search_experience_id(experience_index_input, api_service_index)

        #  получение id города из ввода пользователя
        city_id = get_city_id(api_service_index, search_city)

        vacancies = SuperJobVacancy(
            keyword=search_keyword,
            experience=search_experience,
            town=city_id,
            payment_from=search_salary)

    if api_service_index == 3:
        search_experience_list = get_search_experience_id(experience_index_input, api_service_index)
        search_experience_hh = search_experience_list[0]
        city_data_list = get_city_id(api_service_index, search_city)
        city_id_hh = city_data_list[0]
        vacancies = HeadHunterVacancy(
            text=search_keyword,
            experience=search_experience_hh,
            area=city_id_hh,
            salary=search_salary
        )
        search_experience_sj = search_experience_list[1]
        city_id_sj = city_data_list[1]

        vacancies = SuperJobVacancy(
            keyword=search_keyword,
            experience=search_experience_sj,
            town=city_id_sj,
            payment_from=search_salary)

        all_vacancies = AllVacancies()


if __name__ == "__main__":
    interact_with_user()
