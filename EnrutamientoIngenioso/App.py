
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# BBDD temporal
todos = {}

class TodoSimple(Resource):
	def get(self, todo_id):
		return {todo_id: todos[todo_id]}

	# Actualizar la bddd
	def put(self, todo_id):
		todos[todo_id] = request.json["data"]
		return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, "/<string:todo_id>")

if __name__ == "__main__":
	app.run(debug = True)