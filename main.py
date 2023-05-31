from parsers.headhunter_parser import HeadHunterParser
from vacancies.headhunter_vacancy import HeadHunterVacancy
from vacancies.superjob_vacancy import SuperJobVacancy


def interact_with_user():
    try:
        api_service = int(input("Здравствуйте, вводом номера выберите сервис поиска вакансий:\n"
                                "1. HeadHunter 2.SuperJob 3.Оба сервиса\n"))
    except ValueError:
        print("Необходимо ввести номер опции (1/2/3)")
    else:
        print("Введите параметры поиска (ключевое слово для поиска, опыт работы, зарплату, город):")
        search_keyword = input("Ключевое слово: ")

        experience_dict = HeadHunterParser().get_additional_dicts()["experience"]
        experience_hint = ""
        index = 0
        experience_list = []
        for item in experience_dict:
            index += 1
            experience_hint += str(index) + ". " + item['name'] + " / "
            experience_list.append(item["name"])
        try:
            experience_index = int(input(f"Опыт работы ({experience_hint}): "))
            while experience_index <= 0 or experience_index > index:
                print("Необходимо ввести номер опции")
                experience_index = int(input())
        except ValueError:
            print("Необходимо ввести номер опции")
        else:

            search_salary = int(input("Зарплата: "))
            search_city = input("Город: ").capitalize()

            if api_service == 1:

                #  получение id опыта работы по введенному индексу
                for dict_item in experience_dict:
                    if experience_list[experience_index - 1] in dict_item.values():
                        search_experience = dict_item["id"]

                #  получение id города из ввода пользователя
                areas_list = HeadHunterParser().get_area_dicts()["areas"]
                for area in areas_list:
                    if search_city in area["name"]:  # проверка наличия города вне региона (напр. Москва)
                        city_id = str(area["id"])
                    else:
                        for city in area["areas"]:  # спуск до городов внутри регионов
                            if search_city in city["name"]:
                                city_id = str(city["id"])


                vacancies = HeadHunterVacancy(
                            text=search_keyword,
                            experience=search_experience,
                            salary=search_salary,
                            area=city_id
                        )

        if api_service == 2:
            SuperJobVacancy(search_keyword, search_experience, search_salary, search_city)
        else:
            HeadHunterVacancy(search_keyword, search_experience, search_salary, search_city)
            SuperJobVacancy(search_keyword, search_experience, search_salary, search_city)


interact_with_user()





