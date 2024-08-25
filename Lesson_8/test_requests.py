import pytest
import requests

from Lesson_8.employee import Company

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
