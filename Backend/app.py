from flask import Flask, jsonify, request
from flask.wrappers import Request
from flask_cors import CORS
import json
#Librerías implementadas
from config import config

app = Flask(__name__)
CORS(app)

# Método Handler para ver que todo va bien :D
@app.route('/', methods=['GET'])
def prueba():
    try:
        textoSalida = "Estoy corriendo :D"
        objeto = {
        'textoSalida': textoSalida
        }
        return (jsonify(objeto)) # Se devuelve un json para mejor facilidad en javascript
    except Exception as error:
        salida={"Mensaje":"Error"}
        return (jsonify(error))
    
# Método POST para analizar la entrada
@app.route('/analizar', methods=['POST'])
def analizar():
    try:
        textoEntrada = request.json['textoEntrada']
        
        objeto = {
        'textoSalida': textoEntrada + " prueba"
        }
        return (jsonify(objeto)) # Se devuelve un json para mejor facilidad en javascript
    except Exception as error:
        salida={"Mensaje": error}
        return (jsonify(salida))

def pagina_no_encontrada(error):
    return "<h1>La página que intentas buscar no existe...</h1>"

if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
