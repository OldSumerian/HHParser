from src.class_HH import HeadHunterAPI
from src.class_Filework_JSON import FileworkJSON


def user_interaction():
    """
    Функция по взаимодействию с пользователем через интерфейс
    :return:
    """
    platforms = ["headhunter", 'хедхантер', "хэдхантер"]

    search_query = input("Введите наименование платформы по поиску вакансий:\n")
    if search_query.lower() in platforms:
        filter_words = input("Введите ключевое слово для фильтрации вакансий: ")
        salary_range = input("Введите размер желаемой зарплаты: ")
        top_n = int(input("Введите количество вакансий для вывода (кратно 10)"))
        page = top_n // 10

        # Создание экземпляра класса для работы с API сайтов с вакансиями
        hh_api = HeadHunterAPI()

        # Получение вакансий с hh.ru в формате JSON по заданным параметрам
        hh_api.load_vacancies(filter_words, int(salary_range), page)

        # Создание экземпляра класса для работы с сохраненным файлом и его обработка
        json_saver = FileworkJSON()
        json_saver.add_vacancies_to_file(hh_api.vacancies)

        #  Формирование и вывод в консоль списка вакансий по параметрам пользователя
        vacancies_list = json_saver.get_vacancies_from_file()
        for vacancy in vacancies_list:
            print(vacancy)
            print()
    else:
        print('В данный момент поиск по данной платформе не поддерживается, но мы работаем над этим.')


if __name__ == "__main__":
    user_interaction()
