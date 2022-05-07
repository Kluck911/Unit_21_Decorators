import pytest
from datetime import datetime


@pytest.fixture()
def some_data():
    return 42


def test_some_data(some_data):
    assert some_data == 42


@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print(f'\nТест шел: {end_time - start_time}')
