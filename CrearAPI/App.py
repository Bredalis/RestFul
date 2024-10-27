
from flask import Flask
from flask_restful import Resource, Api

class HelloWorldResource(Resource):
    """Recurso para manejar el saludo inicial"""
    
    def get(self):
        """
        Maneja las solicitudes GET
        
        Returns:
            dict: Mensaje de saludo
        """
        return {
            "message": "Hello World",
            "status": "success"
        }

def create_app():
    """
    Crea y configura la aplicación Flask
    
    Returns:
        Flask: Aplicación configurada
    """
    app = Flask(__name__)
    api = Api(app)
    
    # Configurar rutas
    setup_routes(api)
    
    return app

def setup_routes(api):
    """
    Configura las rutas de la API
    
    Args:
        api: Instancia de Flask-RESTful API
    """
    api.add_resource(HelloWorldResource, "/")

def main():
    """Función principal para ejecutar la aplicación"""
    app = create_app()
    app.run(debug = True)

if __name__ == "__main__":
    main()