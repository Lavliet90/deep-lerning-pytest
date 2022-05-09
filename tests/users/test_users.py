import pytest
import requests
from config import STATS_BASKER, SERVICE_URL
from src.baseclasses.response import Response
from src.pydantic_schemas.user import User
# from src.schemes.post import POST_SCHEMA
from src.pydantic_schemas.post import Post


# def test_getting_posts():
#     response = Response(requests.get(url=STATS_BASKET))
#
#     response.assert_status_code(200).validate(Post)  #or POST_SCHEMA


# resp = requests.get(SERVICE_URL)
# print(resp.json())


def test_getting_users_list(get_users, calculate):
    test_object = Response(get_users)
    test_object.assert_status_code(200).validate(User)
    # print(calculate)
    # print(calculate(1, 20))


@pytest.mark.production
# @pytest.mark.skip('Skip this test')  # skip test
def test_another(make_number):
    assert 1 == 1
    # print(make_number)


@pytest.mark.development
@pytest.mark.parametrize('a, b, c', [(1, 2, 3),
                                     (1, -2, -1),
                                     (-1, -2, -3),
                                     ('b', -2, None),
                                     ('v', 's', None)])
def calculator(a, b, c, calculate):
    assert calculate(a, b) == c
