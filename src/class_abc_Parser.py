from abc import ABC, abstractmethod


class Parser(ABC):
    """
    Абстрактный класс для парсера
    """
    @abstractmethod
    def load_vacancies(self, keyword, salary_range, page):
        pass
