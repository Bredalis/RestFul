
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Crear la primera API
class HolaMundo(Resource):
	def get(self):
		return {"Hola": "Mundo"}

# Datos ubicados en la ruta principal
api.add_resource(HolaMundo, "/")

if __name__ == "__main__":
	app.run(debug = True)