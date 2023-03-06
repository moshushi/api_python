import requests

r = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(type(r))
print(r.status_code)
print(r.text)
print(r.json())

# for key, value in r.headers.items():
#     print(key, ' ====> ', value)