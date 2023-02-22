import requests

URL_INFO = "http://my-api-example.herokuapp.com/api/info/about"
r = requests.request("PUT", URL_INFO)

print(r.headers)
