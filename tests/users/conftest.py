from random import randrange

import pytest
import requests

from config import SERVICE_URL


@pytest.fixture(autouse=True)
def say_hello():
    # print('hello')
    return 14


@pytest.fixture()
def get_users():
    return requests.get(SERVICE_URL)


def _calculate(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b



@pytest.fixture()
def calculate():
    return _calculate


@pytest.fixture()
def make_number():
    # print(' I\'m getting number')
    number = randrange(1, 1000, 5)
    yield number
    # print(f' Number at home {number}')
