import pytest
import requests
from datetime import datetime


@pytest.fixture(scope="class")
def get_key(request):
    # переменные email и password нужно заменить своими учетными данными
    response = requests.post(url='https://petfriends1.herokuapp.com/login',
                             data={"email": 'afvaegffewafgwe@gmail.com', "pass": 'afwwfwaffaw'})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
    print("\nreturn auth_key")
    return response.request.headers.get('Cookie')


@pytest.fixture(autouse=True)
def request_fixture(request):
    if 'Pets' in request.function.__name__:
        print(f"\nЗапущен тест из сьюта Дом Питомца: {request.function.__name__}")


class TestClassPets:

    def test_getAllPets2(self, get_key):
        response = requests.get(url='https://petfriends1.herokuapp.com/api/pets',
                                headers={"Cookie": get_key})
        assert response.status_code == 200, 'Запрос выполнен неуспешно'
        assert len(response.json().get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'

    def test_getMyPets2(self, get_key):
        response = requests.get(url='https://petfriends1.herokuapp.com/my_pets',
                                headers={"Cookie": get_key})
        assert response.status_code == 200, 'Запрос выполнен неуспешно'
        assert response.headers.get('Content-Type') == 'text/html; charset=utf-8'

    def test_anotherTest(self):
        pass


@pytest.fixture()
def time_delta():
    start_time = datetime.now()
    yield
    stop_time = datetime.now()
    print(f'Время теста: {stop_time - start_time}')
