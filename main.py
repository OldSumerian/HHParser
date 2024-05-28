from src.class_HH import HeadHunterAPI
from src.class_Filework_JSON import FileworkJSON






# # Преобразование набора данных из JSON в список объектов
# vacancies = Vacancy.cast_to_object_list(hh_vacancies)
#
# # Пример работы контструктора класса с одной вакансией
# vacancy = Vacancy("Python Developer", "", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
#
# # Сохранение информации о вакансиях в файл
#

# json_saver.delete_vacancy(vacancy)



# Функция для взаимодействия с пользователем
def user_interaction():
    platforms = ["headhunter", 'хедхантер', "хэдхантер"]

    search_query = input("Введите наименование платформы по поиску вакансий:\n")
    if search_query.lower() in platforms:
        filter_words = input("Введите ключевое слово для фильтрации вакансий: ")
        salary_range = input("Введите размер желаемой зарплаты: ")
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))

        # Создание экземпляра класса для работы с API сайтов с вакансиями
        hh_api = HeadHunterAPI()

        # Получение вакансий с hh.ru в формате JSON
        hh_api.load_vacancies(filter_words)
        json_saver = FileworkJSON()
        json_saver.add_vacancies_to_file(hh_api.vacancies)
        vacancies_list = json_saver.get_vacancies_from_file()
        for vacancy in vacancies_list:
            print(vacancy)
            print()
    else:
        print('В данный момент поиск по данной платформе не поддерживается, но мы работаем над этим.')







#     filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
#
#     ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
#
#     sorted_vacancies = sort_vacancies(ranged_vacancies)
#     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
#     print_vacancies(top_vacancies)
#
#
if __name__ == "__main__":
    user_interaction()