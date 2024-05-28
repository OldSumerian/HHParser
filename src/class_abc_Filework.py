from abc import ABC, abstractmethod


class Filework(ABC):
    """
    Абстрактный класс обязывающий создать методы по обработке информации о вакансиях в файле
    (добавление в файл, получение из файла, удаление из файла)
    """
    @abstractmethod
    def add_vacancies_to_file(self, vacancies):
        pass

    @abstractmethod
    def get_vacancies_from_file(self):
        pass

    @abstractmethod
    def delete_vacancies_from_file(self):
        pass
