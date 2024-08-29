
from flask import Flask, request
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)

class FormatoDeDatos(Resource):
	def __init__(self):
		self.datos = {
			"name": "Alice",
			"age": 30,
			"city": "Wonderland"
		}

	def to_json(self):
		"""
		Conviente los datos a formato JSON
		"""

		try:
			return json.dumps(self.datos, indent = 4)
		
		except (TypeError, OverflowError) as e:
			return f"Error al convertir los datos a JSON: {e}"

	def to_string(self):
		"""
		Convierte los datos a una cadena 
		de texto formateada
		"""
		cadena_formateada = ""

		for key, value in self.datos.items():
			cadena_formateada += f" {key}: {value} "

		return cadena_formateada

	def get(self):
		"""
		Devuelve los datos como en formato JSON 
		o como un string
		"""

		tipo_formato = request.args.get("format", "json")

		if tipo_formato == "text":
			return self.to_string()

		else:
			return self.to_json()

# Agregar la ruta a la API
api.add_resource(FormatoDeDatos, "/datos")

if __name__ == "__main__":
	app.run(debug = True)