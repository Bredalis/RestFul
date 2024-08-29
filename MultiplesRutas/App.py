
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Datos
todos = {
	1: {"task": "Learn Flask"},
	2: {"task": "Build an API"},
	3: {"task": "???"},
}

# Ruta para manejar recursos individuales
class TodoSimple(Resource):
	def get(self, todo_id):
		return {todo_id: todos[todo_id]}

	def put(self, todo_id):
		todos[todo_id] = {"task": request.json["task"]}
		return {todo_id: todos[todo_id]}

	def delete(self, todo_id):
		del todos[todo_id]
		return "", 204

# Ruta para manejar la lista de recursos
class TodoList(Resource):
	def get(self):
		return todos

	def post(self):
		new_id = max(todos.keys()) + 1
		todos[new_id] = {"task": request.json["task"]}
		return {new_id: todos[new_id]}, 201 

# Agregar las rutas a la API
api.add_resource(TodoSimple, "/todos/<int:todo_id>")
api.add_resource(TodoList, "/todos")

if __name__ == "__main__":
	app.run(debug = True)