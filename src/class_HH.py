import requests
from src.class_abc_Parser import Parser


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 10}
        self.vacancies = []

    def load_vacancies(self, keyword: str, salary_range, page):
        self.params['text'] = keyword
        if salary_range != 0:
            self.params['salary'] = salary_range
            self.params['only_with_salary'] = True
        while self.params.get('page') != page:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
