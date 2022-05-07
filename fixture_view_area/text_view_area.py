import pytest


def session_fixture():
    print("\nclass fixture starts")


@pytest.fixture(scope="function", autouse=True)
def function_fixture():
    print("\nfunction fixture starts")


class TestClass23:
    def test_first(self):
        pass

    def test_second(self):
        pass
