
from requests import put, get

def main():
    # Crear y obtener todos
    print(put("http://localhost:5000/todo1", json={"data": "Remember the milk"}).json())
    print(get("http://localhost:5000/todo1").json())

    print(put("http://localhost:5000/todo2", json={"data": "Change my brakepads"}).json())
    print(get("http://localhost:5000/todo2").json())

if __name__ == "__main__":
    main()