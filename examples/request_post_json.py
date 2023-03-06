import requests

URL = "http://jsonplaceholder.typicode.com/posts"
# URL2 = "http://my-api-example.herokuapp.com/api/info/about"

HEADERS = {
    "Content-type": "application/json; charset=UTF-8"
}

DATA = {
    "some": "this is some",
    "wall": "this is wall",
}

response = requests.post(
    URL,
    headers=HEADERS,
    json=DATA
)

print(response.json())
