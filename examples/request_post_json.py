import requests

URL = "http://jsonplaceholder.typicode.com/posts"

HEADERS = {
    "Content-type": "application/json; charset=UTF-8"
}

DATA = {
    "some": "this is some",
    "wall": "this is wall",
}

response = requests.post(
    URL,
    HEADERS,
    DATA
)

print(response.json())