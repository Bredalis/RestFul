
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class TodoResource(Resource):
    def __init__(self):
        self.todos = {}
        self._setup_parser()

    def _setup_parser(self):
        """Configura el parser de argumentos"""
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            "task",
            type = str,
            required = True,
            help = "Task cannot be blank"
        )

    def get(self, todo_id):
        """
        Obtiene una tarea por su ID
        
        Args:
            todo_id: Identificador único de la tarea
            
        Returns:
            dict: Tarea encontrada o mensaje de error
        """
        return (
            {todo_id: self.todos[todo_id]}
            if todo_id in self.todos
            else {"message": "Todo not found"}
        )

    def post(self, todo_id):
        """
        Crea una nueva tarea
        
        Args:
            todo_id: Identificador único para la nueva tarea
            
        Returns:
            tuple: Tarea creada y código de estado HTTP
        """
        args = self.parser.parse_args()
        task = args["task"]
        self.todos[todo_id] = task
        
        return {todo_id: task}, 201

def setup_routes(api):
    """Configura las rutas de la API"""
    api.add_resource(TodoResource, "/todos/<string:todo_id>")

def create_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__)
    api = Api(app)
    setup_routes(api)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug = True)