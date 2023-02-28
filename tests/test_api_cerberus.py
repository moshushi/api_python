"""Проверяем полученный json на корректность"""
import cerberus
import requests

# base_url = 'https://jsonplaceholder.typicode.com/'


def test_api_json_schema(base_url):
    """Проверка структуры ответа на запрос"""
    res = requests.get(base_url + "todos/1")

    schema = {
        "id": {"type": "number"},
        "userId": {"type": "number"},
        "title": {"type": "string"},
        "completed": {"type": "boolean"},
        # "www": {"type": "boolean"},
    }

    v = cerberus.Validator()
    assert v.validate(res.json(), schema)
