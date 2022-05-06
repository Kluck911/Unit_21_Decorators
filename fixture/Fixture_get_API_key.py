import pytest
import requests


@pytest.fixture()
def get_key():
    # переменные email и password нужно заменить своими учетными данными
    response = requests.post(url='https://petfriends1.herokuapp.com/login',
                             data={"email": 'afvaegffewafgwe@gmail.com', "pass": 'afwwfwaffaw'})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
    return response.request.headers.get('Cookie')


def test_getAllPets(get_key):
    response = requests.get(url='https://petfriends1.herokuapp.com/api/pets',
                            headers={"Cookie": get_key})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert len(response.json().get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'