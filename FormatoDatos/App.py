
from flask import Flask, request
from flask_restful import Api, Resource, abort
import json

app = Flask(__name__)
api = Api(app)

class FormatoDeDatos(Resource):
    def __init__(self):
        # Datos de ejemplo
        self.datos = {
            "name": "Alice",
            "age": 30,
            "city": "Wonderland"
        }
        # Formatos válidos
        self.formatos_validos = ["json", "text"]

    def to_json(self):
        """
        Convierte los datos a formato JSON
        
        Returns:
            str: Datos formateados en JSON
            
        Raises:
            TypeError: Si hay error en la conversión
            OverflowError: Si hay desbordamiento
        """
        try:
            return json.dumps(self.datos, indent = 4)
        except (TypeError, OverflowError) as e:
            abort(500, message = f"Error al convertir a JSON: {str(e)}")

    def to_string(self):
        """
        Convierte los datos a una cadena de texto formateada
        
        Returns:
            str: Datos formateados como texto
        """
        try:
            return " ".join(f"{key}: {value}" for key, value in self.datos.items())
        except Exception as e:
            abort(500, message = f"Error al convertir a texto: {str(e)}")

    def get(self):
        """
        Devuelve los datos en formato JSON o string según el parámetro 'format'
        
        Returns:
            str: Datos formateados según el formato solicitado
            
        Raises:
            400: Si el formato solicitado no es válido
        """
        tipo_formato = request.args.get("format", "json").lower()

        if tipo_formato not in self.formatos_validos:
            abort(400, message = f"Formato no válido. Use: {", ".join(self.formatos_validos)}")

        return self.to_string() if tipo_formato == "text" else self.to_json()

# Configuración de rutas
api.add_resource(FormatoDeDatos, "/datos")

if __name__ == "__main__":
    app.run(debug = True)