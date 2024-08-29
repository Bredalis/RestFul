
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class TodoResource(Resource):
    def __init__(self):
        self.todos = {}  # Diccionario para almacenar los todos

        # Iniciar el parser de argumentos
        self.parse = reqparse.RequestParser()
        self.parse.add_argument("task", type = str, required = True, help = "Task cannot be blank")

    def get(self, todo_id):

        # Devuelve el todo con el id específico
        if todo_id in self.todos:
            return {todo_id: self.todos[todo_id]}
        else:
            return {"message": "Todo not found"}

    def post(self, todo_id):

        # Analizar los argumentos de la solicitud
        args = self.parse.parse_args()
        task = args["task"]
        self.todos[todo_id] = task
        
        return {todo_id: task}, 201  # Devuelve el todo creado y un código de estado 201

# Agregar ruta a la API con el parámetro `todo_id`
api.add_resource(TodoResource, "/todos/<string:todo_id>")

if __name__ == "__main__":
    app.run(debug = True)