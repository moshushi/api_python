import inspect
import requests

r = requests.get('https://jsonplaceholder.typicode.com/posts/1')

print(type(r))
print(dir(r))
# print(filter(lambda x: not x.startswitch('_'), dir(r)))
print(r.status_code)
# print(inspect.getsource(dir(r)))

# for i in dir(r):
#     if not i.startswith('_'):
#         print(i)