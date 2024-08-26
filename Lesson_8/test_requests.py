import pytest
import requests

from Lesson_8.employee import Company, Employee

URL = "https://x-clients-be.onrender.com"
@pytest.fixture()
def get_token(username= 'raphael', password= 'cool-but-crude'):
    log_pass = {'username': username, 'password': password}
    resp_token = requests.post(URL + '/auth/login', json=log_pass)
    token = resp_token.json()['userToken']
    return token


def test_create_employee(get_token):
    company = Company(URL)
    body = {
  "name": "ООО Ромашка",
  "description": "Выращивание и продажа цветов"
}
    id = company.create_company(str(get_token), body)
    assert id is not None

    body_employer = {
        'id': 0,
        'firstName': 'Ivan',
        'lastName': 'Petrov',
        'middleName': 'string',
        'companyId': id,
        'email': 'test@mail.ru',
        'url': 'string',
        'phone': 'string',
        'birthdate': '2024-05-16T11:02:45.622Z',
        'isActive': 'true',
    }
    employer = Employee(URL)
    new_employer_id = (employer.add_new(str(get_token), body_employer))['id']
    """Удостоверяемся, что ID не пустой"""
    assert new_employer_id is not None


def test_change_employer_info(get_token):
    company = Company(URL)
    body = {
        "name": "ООО Ромашка",
        "description": "Выращивание и продажа цветов"
    }
    id = company.create_company(str(get_token), body)
    assert id is not None
    body_employer = {
        'id': 0,
        'firstName': 'Ivan',
        'lastName': 'Petrov',
        'middleName': 'string',
        'companyId': id,
        'email': 'test@mail.ru',
        'url': 'string',
        'phone': 'string',
        'birthdate': '2024-05-16T11:02:45.622Z',
        'isActive': 'true',
    }
    employer = Employee(URL)
    just_employer = employer.add_new(str(get_token), body_employer)
    id = just_employer['id']
    body_change_employer = {
        'lastName': 'Ivanov',
        'email': 'test1@mail.ru',
        'url': 'string',
        'phone': 'string',
        'isActive': 'true',
    }
    employer_changed = employer.change_employee_info(str(get_token), id, body_change_employer)
    assert employer_changed.status_code == 200

    """Проверка что ID соответствует ID при создании сотрудника"""
    assert id == employer_changed.json()["id"]
    """Проверка изменения почты"""
    assert (employer_changed.json()["email"]
            ) == body_change_employer.get("email")

def test_get_employer(get_token):
        company = Company(URL)
        body = {
            "name": "ООО Ромашка",
            "description": "Выращивание и продажа цветов"
        }
        id = company.create_company(str(get_token), body)
        assert id is not None
        """Список работников компании"""
        employer = Employee(URL)
        list_employers = employer.get_employees(id)
        """Проверка наличия списка"""
        assert isinstance(list_employers, list)