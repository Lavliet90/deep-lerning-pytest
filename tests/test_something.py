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


def test_getting_users_list(say_hello):
    response = requests.get(SERVICE_URL)
    test_object = Response(response)
    test_object.assert_status_code(200).validate(User)
    print(say_hello)
