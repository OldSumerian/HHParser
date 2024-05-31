import json
from src.class_Vacancy import Vacancy
from src.class_abc_Filework import Filework


class FileworkJSON(Filework):
    """
    Класс для работы с данными по вакансиям в JSON-формате
    """
    def __init__(self, filename='vacancies.json'):
        self.__filename = f'data/{filename}'

    def add_vacancies_to_file(self, vacancies):
        """
        Функция для добавления вакансий в файл
        :param vacancies:
        :return:
        """
        with open(self.__filename, 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def get_vacancies_from_file(self):
        """
        Функция для получения вакансий из файла
        :return:
        """
        with open(self.__filename, encoding='utf-8') as f:
            vacancies_data = json.load(f)
        vacancies = []
        for vacancy in vacancies_data:
            vacancies.append(Vacancy(name=vacancy['name'], salary=vacancy['salary'], employer=vacancy['employer']['name'], url=vacancy['alternate_url']))
        return vacancies

    def delete_vacancies_from_file(self):
        """
        Функция удаления вакансий из файла
        :return:
        """
        open(self.__filename, 'w').close()

