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

@app.route('/proyectoolc2/errores', methods=['GET'])
def repErrores():
    consolaGlobal: Consola = Consola()
    excepciones = consolaGlobal.get_Excepciones()
    objeto = {
        'repoerrores': excepciones
    }
    return (jsonify(objeto))

@app.route('/proyectoolc2/simbolos', methods=['GET'])
def repSimbolos():
    consolaGlobal: Consola = Consola()
    simbolos = consolaGlobal.obtenerSimbolos()
    objeto = {
        'reposimbolos': simbolos
    }
    return (jsonify(objeto))

@app.route('/proyectoolc2/ast', methods=['GET'])
def repAst():
    consolaGlobal: Consola = Consola()
    ast = consolaGlobal.get_AstGrafico()
    objeto = {
        'repoast': ast
    }
    return (jsonify(objeto))
    
    
@app.route('/proyectoolc2/analizar', methods=['POST'])
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
        entradaConsola = request.json['textoEntrada']
        listaExcepciones = []
        salidaConsola = ""
        salidaGrafico = ""
        # Realizar análisis léxico y sintáctico
        ast: Ast = parsear(entradaConsola)

        # Realizar análisis semántico
        # Incluyendo pasadas para funciones, Interfaces y luego instrucciones.
        if(ast != None):
            ts = TablaSimbolos(None, 'GLOBAL-')
            ast.ejecutar(ts)
        
        listaExcepciones = consolaGlobal.obtenerErrores()
        
        # Generar gráfico AST
        if listaExcepciones == []:
           ast.generarGrafico()
           salidaGrafico = consolaGlobal.get_AstGrafico()
        
        if listaExcepciones != []:
            consolaGlobal.set_Consola("\nSe encontraron errores léxicos, sintácticos o semánticos...\n")   
            
        for x in listaExcepciones:
            print(x.descripcion)

        salidaConsola = consolaGlobal.get_Consola()
        objeto = {
        'textoSalida': salidaConsola
        }
        return (jsonify(objeto)) # Se devuelve un json para mejor facilidad en javascript
    except Exception as error:
        salidaConsola={"Mensaje": error}
        return (jsonify(salidaConsola))



def pagina_no_encontrada(error):
    return "<h1>La página que intentas buscar no existe...</h1>"

if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
