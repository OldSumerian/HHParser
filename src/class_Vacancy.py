
class Vacancy:
    """
    Класс для создания и валидации экземпляров вакансий
    """
    def __init__(self, name: str, salary: dict, employer: str, url: str):
        self.name = name
        self.__validate_salary(salary)
        self.employer = employer
        self.url = url

    def __validate_salary(self, salary: dict):
        if salary is None:
            self.salary_to = 0
            self.salary_from = 0
        else:
            self.salary_to = salary['to'] if salary['to'] else 0
            self.salary_from = salary['from'] if salary['from'] else 0



        # if self.salary_to and self.salary_from:
        #     salary_all = f'{self.salary_from} - {self.salary_to} рублей'
        # elif self.salary_to and not self.salary_from:
        #     salary_all = f'до {self.salary_to} рублей'
        # elif not self.salary_to and self.salary_from:
        #     salary_all = f'от {self.salary_from} рублей'
        # else:
        #     salary_all = 'размер не указан'

    def __lt__(self, other):
        return self.salary_to < other.salary_to


    def __str__(self):
        return (f'Наименование вакансии: {self.name}\n'
                f'Заработная плата: {self.salary_from} - {self.salary_to} \n'
                f'Работодатель: {self.employer}\n'
                f'Ссылка на вакансию: {self.url}')


