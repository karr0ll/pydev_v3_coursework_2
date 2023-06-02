from parsers.headhunter_parser import HeadHunterParser
from parsers.superjob_parser import SuperJobParser

def get_search_experience_id(experience_index_input, api_service_index):
    # получение словаря с id названий типа опыта
    experience_list = []
    hh_all_experience_dicts = HeadHunterParser().get_additional_dicts()["experience"]
    hh_experience_dict = hh_all_experience_dicts[experience_index_input]
    experience_list.append(hh_experience_dict["id"])

    sj_experience_dict = SuperJobParser().get_additional_data_dicts()["experience"]
    for key in sj_experience_dict.keys():
        if str(experience_index_input) == key:
            experience_list.append(int(key))

    if api_service_index == 1:
        return experience_list[0]

    if api_service_index == 2:
        return experience_list[1]

    if api_service_index == 3:
        return experience_list


def get_city_id(api_service_index, search_city):
    cities_list = []
    hh_areas_list: dict = HeadHunterParser().get_area_dicts()["areas"]
    for area in hh_areas_list:
        if search_city in area["name"]:  # проверка наличия города вне региона (напр. Москва)
            cities_list.append(str(area["id"]))
        else:
            for city in area["areas"]:  # спуск до городов внутри регионов
                if search_city in city["name"]:
                    cities_list.append(str(city["id"]))
    sj_towns_list: list = SuperJobParser().get_towns_dict()["objects"]
    for item in sj_towns_list:
        if search_city == item["title"]:
            cities_list.append(item["id"])

    if api_service_index == 1:
        return cities_list[0]

    if api_service_index == 2:
        return cities_list[1]

    if api_service_index == 3:
        return cities_list
