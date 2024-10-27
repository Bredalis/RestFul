
from flask import Flask, request
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

# Base de datos temporal (en memoria)
todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        """
        Obtiene un todo por su ID
        
        Args:
            todo_id: Identificador del todo
            
        Returns:
            dict: Todo encontrado
        """
        if todo_id not in todos:
            abort(404, message = f"Todo {todo_id} not found")
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        """
        Actualiza o crea un todo
        
        Args:
            todo_id: Identificador del todo
            
        Returns:
            dict: Todo actualizado
        """
        if not request.json or "data" not in request.json:
            abort(400, message = "Missing 'data' in request")
            
        todos[todo_id] = request.json["data"]
        return {todo_id: todos[todo_id]}

# Configurar rutas
api.add_resource(TodoSimple, "/<string:todo_id>")

if __name__ == "__main__":
    app.run(debug = True)