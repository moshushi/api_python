import requests
from jsonschema import validate


def test_api_json_schema(base_url):
    res = requests.get(base_url + "/todos/1")

    schema = {
        "type": "object",
        "properties": {
            "id": {"tupe": "number"},
            # "userId": {"tupe": "number"},
            "title": {"type": "string"},
            "completed": {"type", "boolean"}
        },
        "required": ["id", "userId", "completed"]
    }

    validate(instance=res.json(), schema=schema)