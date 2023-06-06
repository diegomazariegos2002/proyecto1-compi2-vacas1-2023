from flask import Flask, jsonify, request
from flask.wrappers import Request
from flask_cors import CORS
import json
#Librerías implementadas
from config import config
from source.AST.Ast import Ast
from source.consola_singleton.Consola import Consola
from source.analizadores.parser import parsear, getErrores
from source.simbolo.TablaSimbolos import TablaSimbolos


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
    
@app.route('/analizar', methods=['POST'])
def analizar():
    """
    Método handler para el endpoint '/analizar'.

    Este método maneja las solicitudes POST enviadas al endpoint '/analizar'.

    Args:
        - request (flask.Request): JSON.
            {
                "textoEntrada": "Texto a analizar"
            }
    Returns:
        - flask.Response: JSON.
            {
                "textoSalida": "Texto analizado"
            }
    Raises:
        - KeyError: Si la clave 'textoEntrada' no está presente en el JSON de la solicitud.
        - Exception: Si ocurre algún otro error en el procesamiento de la solicitud.

    """
    try:
        consolaGlobal: Consola = Consola()
        consolaGlobal.clean_Consola()
        textoEntrada = request.json['textoEntrada']
        ast: Ast = parsear(textoEntrada)

        if(ast != None):
            ts = TablaSimbolos(None, 'Global')
            ast.ejecutar(ts)
        
        listaExcepciones = consolaGlobal.get_Excepciones()
        if listaExcepciones != []:
                consolaGlobal.set_Consola("\nSe encontraron errores léxicos o sintácticos...\n")    

        salida = consolaGlobal.get_Consola()
        objeto = {
        'textoSalida': salida
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
