from abc import ABC, abstractmethod


class Filework(ABC):
    """
    Абстрактный класс обязывающий создать методы по обработке информации о вакансиях в файле
    (добавление в файл, получение из файла, удаление из файла)
    """
    @abstractmethod
    def add_vacancies_to_file(self, vacancies):
        """
        Функция добавления вакансий в файл
        :param vacancies:
        :return:
        """
        pass

    @abstractmethod
    def get_vacancies_from_file(self):
        """
        Функция получения данных о вакансиях из файла
        :return:
        """
        pass

    @abstractmethod
    def delete_vacancies_from_file(self):
        """
        Функция по удалению вакансий из файла
        :return:
        """
        pass
