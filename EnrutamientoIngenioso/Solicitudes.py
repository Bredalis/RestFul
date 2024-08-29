
from requests import put, get

# ACtualizar la bbdd
print(put("http://localhost:5000/todo1", data = {"data": "Remember the milk"}).json())
print(get("http://localhost:5000/todo1").json())

print(put("http://localhost:5000/todo2", data = {"data": "Change my brakepads"}).json())
print(get("http://localhost:5000/todo2").json())