
from flask import Flask, request
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

# Base de datos en memoria
todos = {
    1: {"task": "Learn Flask"},
    2: {"task": "Build an API"},
    3: {"task": "???"}
}

class TodoSimple(Resource):
    """Maneja operaciones CRUD para tareas individuales"""
    
    def get(self, todo_id):
        """
        Obtiene una tarea por su ID
        
        Args:
            todo_id (int): ID de la tarea
            
        Returns:
            dict: Tarea encontrada
        """
        if todo_id not in todos:
            abort(404, message = f"Todo {todo_id} not found")
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        """
        Actualiza una tarea existente
        
        Args:
            todo_id (int): ID de la tarea
            
        Returns:
            dict: Tarea actualizada
        """
        if not request.json or "task" not in request.json:
            abort(400, message = "Missing 'task' in request")
        
        todos[todo_id] = {"task": request.json["task"]}
        return {todo_id: todos[todo_id]}

    def delete(self, todo_id):
        """
        Elimina una tarea
        
        Args:
            todo_id (int): ID de la tarea
            
        Returns:
            tuple: Respuesta vacía con código 204
        """
        if todo_id not in todos:
            abort(404, message = f"Todo {todo_id} not found")
            
        del todos[todo_id]
        return "", 204

class TodoList(Resource):
    """Maneja operaciones para la lista completa de tareas"""
    
    def get(self):
        """
        Obtiene todas las tareas
        
        Returns:
            dict: Lista de todas las tareas
        """
        return todos

    def post(self):
        """
        Crea una nueva tarea
        
        Returns:
            tuple: Nueva tarea creada y código 201
        """
        if not request.json or "task" not in request.json:
            abort(400, message = "Missing 'task' in request")
            
        try:
            new_id = max(todos.keys()) + 1
        except ValueError:
            new_id = 1
            
        todos[new_id] = {"task": request.json["task"]}
        return {new_id: todos[new_id]}, 201

# Configuración de rutas
api.add_resource(TodoSimple, "/todos/<int:todo_id>")
api.add_resource(TodoList, "/todos")

if __name__ == "__main__":
    app.run(debug = True)