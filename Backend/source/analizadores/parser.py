# Librerías implementadas
from datetime import datetime
from ply import yacc
from source.consola_singleton.Consola import Consola

from source.errores.Excepcion import Excepcion
from source.expresiones.nativas.ToExponential import ToExponential
from source.expresiones.nativas.ToFixed import ToFixed
from source.expresiones.nativas.ToLowerCase import ToLowerCase
from source.expresiones.nativas.ToString import ToString
from source.expresiones.nativas.ToUpperCase import ToUpperCase
from .lexer import *
# Librerías propias
from source.abstracto.Retorno import Tipo, Tipo_OperadorAritmetico, TipoLogicas, TipoRelacionales, TipoDato
from source.expresiones.Primitivos import Primitivos
from source.expresiones.Aritmeticas import Arimeticas
from source.expresiones.Logicas import Logicas
from source.expresiones.Acceso import Acceso
from source.expresiones.Relacionales import Relacionales
from source.expresiones.vectores.Vector import Vector
from source.instrucciones.ConsoleLog import ConsoleLog
from source.instrucciones.Declaracion import Declaracion
from source.instrucciones.Asignacion import Asignacion
from source.AST.Ast import Ast



input: str = ''
# Método para calcular la columna en la que se encuentra el token
def calcularColumna(entrada, token):
    totalColumnasEnLinea = entrada.rfind('\n', 0, token.lexpos) + 1
    posicionActualToken = token.lexpos + 1
    return (posicionActualToken - totalColumnasEnLinea)

# arreglo para manejar la precedencia
# precedencia
precedence = (
    ('left', 'or'),
    ('left', 'and'),
    ('left', 'suma', 'resta'),
    ('nonassoc', 'menor', 'mayor', 'menorigual', 'mayorigual', 'igualacion', 'diferente'),
    ('left', 'multiplicacion', 'division', 'modulo'),
    ('left', 'potencia'),
    ('right', 'not'),
    ('left', 'uresta'),
)

#Definición de la gramática
def p_INICIO(p):
    """
    INICIO : ENTRADAS
    """
    p[0] = Ast(p[1])

def p_ENTRADAS_PARTE_1(p):
    """
    ENTRADAS : ENTRADAS ENTRADA
    """
    p[1].append(p[2])
    p[0] = p[1]

def p_ENTRADAS_PARTE_2(p):
    """
    ENTRADAS : ENTRADA
    """
    p[0] = [p[1]]

def p_ENTRADA(p):
    """
    ENTRADA : IMPRIMIR puntoYcoma
    """
    p[0] = p[1]

def p_error(p):
    """
    ENTRADA : error puntoYcoma
    """
    print(p)
    if p:
        Consola().set_Excepcion(Excepcion("ERROR SINTACTICO", "NO SE ESPERABA "+p.value, p.lineno, p.lexpos, datetime.now()))
        # este no se usa realmente
        listaErrores.append(
            Excepcion("ERROR SINTACTICO", "NO SE ESPERABA "+p.value, p.lineno, p.lexpos))
        
# ----------------- DECLARACION ----------------

def p_ENTRADA_Declaracion(p):
    """
    ENTRADA : DECLARACION puntoYcoma
    """
    p[0] = p[1]

def p_DECLARACION_NoTipada(p):
    """
    DECLARACION : let id igual EXPRESION
    """
    p[0] = Declaracion(p[2], None, p[4], p.lineno(1), calcularColumna(input, p.slice[1]))


def p_DECLARACION_Tipada(p):
    """
    DECLARACION : let id dosPuntos TIPO igual EXPRESION
    """
    p[0] = Declaracion(p[2], p[4], p[6], p.lineno(1), calcularColumna(input, p.slice[1]))

def p_DECLARACION_SinExpresion_SinTipado(p):
    """
    DECLARACION : let id 
    """
    p[0] = Declaracion(p[2], None, None, p.lineno(1), calcularColumna(input, p.slice[1]))

def p_DECLARACION_SinExpresion_Tipado(p):
    """
    DECLARACION : let id dosPuntos TIPO
    """
    p[0] = Declaracion(p[2], p[4], None, p.lineno(1), calcularColumna(input, p.slice[1]))
    
# ------------------ ASIGNACION ------------------
    
def p_ENTRADA_Asignacion(p):
    """
    ENTRADA : ASIGNACION puntoYcoma
    """
    p[0] = p[1]

def p_ASIGNACION(p):
    """
    ASIGNACION : id igual EXPRESION
    """
    p[0] = Asignacion(p[1], p[3], p.lineno(1), calcularColumna(input, p.slice[1]))  
    
def p_ASIGNACION_VEC(p):
    """
    ASIGNACION : id LISTAINDICES igual EXPRESION
    """
    p[0] = Asignacion(p[1], p[3], p.lineno(1), calcularColumna(input, p.slice[1]))  
    
# ------------------ IMPRIMIR ------------------
def p_IMPRIMIR_1(p):
    """
    IMPRIMIR : console punto log p_Abre LISTAEXPRESIONES p_Cierra
    """
    p[0] = ConsoleLog(p[5], p.lineno(1), calcularColumna(input, p.slice[1]))

def p_LISTAEXPRESIONES_1(p):
    """
    LISTAEXPRESIONES :  LISTAEXPRESIONES coma EXPRESION
    """
    p[1].append(p[3])
    p[0] = p[1]


def p_LISTAEXPRESIONES_2(p):
    """
    LISTAEXPRESIONES : EXPRESION
    """
    p[0] = [p[1]]
    
def p_LISTAEXPRESIONES_Indices(p):
    """
    LISTAINDICES :  LISTAINDICES c_Abre EXPRESION c_Cierra
    """
    p[1].append(p[3])
    p[0] = p[1]

def p_LISTAEXPRESIONES_2(p):
    """
    LISTAINDICES : c_Abre EXPRESION c_Cierra
    """
    p[0] = [p[2]]

# ------------------ LISTA DE EXPRESIONES ARITMETICAS ------------------

def p_EXPRESION_suma(p):
    """
    EXPRESION : EXPRESION suma EXPRESION
    """
    p[0] = Arimeticas(Tipo_OperadorAritmetico.SUMA, p[1], p[3],  p.lineno(1),
                calcularColumna(input, p.slice[2]))
        
def p_EXPRESION_resta(p):
    """
    EXPRESION : EXPRESION resta EXPRESION
    """
    p[0] = Arimeticas(Tipo_OperadorAritmetico.RESTA, p[1], p[3],  p.lineno(1),
            calcularColumna(input, p.slice[2]))

def p_EXPRESION_multiplicacion(p):
    """
    EXPRESION : EXPRESION multiplicacion EXPRESION
    """
    p[0] = Arimeticas(Tipo_OperadorAritmetico.MULTIPLICACION, p[1], p[3],  p.lineno(1),
            calcularColumna(input, p.slice[2]))
    
def p_EXPRESION_division(p):
    """
    EXPRESION : EXPRESION division EXPRESION
    """
    p[0] = Arimeticas(Tipo_OperadorAritmetico.DIVISION, p[1], p[3],  p.lineno(1),
            calcularColumna(input, p.slice[2]))
    
def p_EXPRESION_potencia(p):
    """
    EXPRESION : EXPRESION potencia EXPRESION
    """
    p[0] = Arimeticas(Tipo_OperadorAritmetico.POTENCIA, p[1], p[3],  p.lineno(1),
            calcularColumna(input, p.slice[2]))
    
def p_EXPRESION_modulo(p):
    """
    EXPRESION : EXPRESION modulo EXPRESION
    """
    p[0] = Arimeticas(Tipo_OperadorAritmetico.MODULO, p[1], p[3],  p.lineno(1),
            calcularColumna(input, p.slice[2]))
    
def p_EXPRESION_negativo(p):
    """
    EXPRESION : resta EXPRESION %prec uresta
    """
    p[0] = Arimeticas(Tipo_OperadorAritmetico.NEGATIVO, p[2], None,  p.lineno(1),
            calcularColumna(input, p.slice[1]))

# ------------------ LISTA DE EXPRESIONES LOGICAS ------------------

def p_EXPRESION_and(p):
    """
    EXPRESION : EXPRESION and EXPRESION
    """
    p[0] = Logicas(TipoLogicas.AND, p[1], p[3],  p.lineno(1),
            calcularColumna(input, p.slice[2]))

def p_EXPRESION_or(p):
    """
    EXPRESION : EXPRESION or EXPRESION
    """
    p[0] = Logicas(TipoLogicas.OR, p[1], p[3],  p.lineno(1),
            calcularColumna(input, p.slice[2]))

def p_EXPRESION_not(p):
    """
    EXPRESION : not EXPRESION
    """
    p[0] = Logicas(TipoLogicas.NOT, p[2], None,  p.lineno(1),
            calcularColumna(input, p.slice[1]))
    
# ------------------ LISTA DE EXPRESIONES RELACIONALES ------------------

def p_EXPRESION_mayor(p):
    """
    EXPRESION : EXPRESION mayor EXPRESION
    """
    p[0] = Relacionales(TipoRelacionales.MAYORQUE, p[1], p[3],  p.lineno(1),
            calcularColumna(input, p.slice[2]))

def p_EXPRESION_mayorigual(p):
    """
    EXPRESION : EXPRESION mayorigual EXPRESION
    """
    p[0] = Relacionales(TipoRelacionales.MAYORIGUAL, p[1], p[3],  p.lineno(1),
            calcularColumna(input, p.slice[2]))

def p_EXPRESION_menor(p):
    """
    EXPRESION : EXPRESION menor EXPRESION
    """
    p[0] = Relacionales(TipoRelacionales.MENORQUE, p[1], p[3],  p.lineno(1),
            calcularColumna(input, p.slice[2]))

def p_EXPRESION_menorigual(p):
    """
    EXPRESION : EXPRESION menorigual EXPRESION
    """
    p[0] = Relacionales(TipoRelacionales.MENORIGUAL, p[1], p[3],  p.lineno(1),
            calcularColumna(input, p.slice[2]))

def p_EXPRESION_igualacion(p):
    """
    EXPRESION : EXPRESION igualacion EXPRESION
    """
    p[0] = Relacionales(TipoRelacionales.IGUALACION, p[1], p[3],  p.lineno(1),
            calcularColumna(input, p.slice[2]))

def p_EXPRESION_diferente(p):
    """
    EXPRESION : EXPRESION diferente EXPRESION
    """
    p[0] = Relacionales(TipoRelacionales.DIFERENTE, p[1], p[3],  p.lineno(1),
            calcularColumna(input, p.slice[2]))

# ------------------ LISTA DE FUNCIONES NATIVAS ------------------

def p_EXPRESION_funcionesnativas(p):
    """
    EXPRESION : FUNCION_TOFIXED
            | FUNCION_TOEXPONENTIAL
            | FUNCION_TOSTRING
            | FUNCION_TOLOWERCASE
            | FUNCION_TOUPPERCASE
            | FUNCION_SPLIT
    """
    p[0] = p[1]

def p_FUNCION_TOFIXED(p):
    """
    FUNCION_TOFIXED : id punto toFixed p_Abre EXPRESION p_Cierra
    """
    # semantico
    p[0] = ToFixed(p[1], p[5], p.lineno(1), calcularColumna(input, p.slice[1]))

def p_FUNCION_TOEXPONENTIAL(p):
    """
    FUNCION_TOEXPONENTIAL : id punto toExponential p_Abre EXPRESION p_Cierra
    """
    # semantico
    p[0] = ToExponential(p[1], p[5], p.lineno(1), calcularColumna(input, p.slice[1]))

def p_FUNCION_TOSTRING(p):
    """
    FUNCION_TOSTRING : id punto toString p_Abre p_Cierra
    """
    # semantico
    p[0] = ToString(p[1], p.lineno(1), calcularColumna(input, p.slice[1]))

def p_FUNCION_TOLOWERCASE(p):
    """
    FUNCION_TOLOWERCASE : id punto toLowerCase p_Abre p_Cierra
    """
    # semantico
    p[0] = ToLowerCase(p[1], p.lineno(1), calcularColumna(input, p.slice[1]))

def p_FUNCION_TOUPPERCASE(p):
    """
    FUNCION_TOUPPERCASE : id punto toUpperCase p_Abre p_Cierra
    """
    # semantico
    p[0] = ToUpperCase(p[1], p.lineno(1), calcularColumna(input, p.slice[1]))

def p_FUNCION_SPLIT(p):
    """
    FUNCION_SPLIT : id punto split p_Abre cadena p_Cierra
    """
    # semantico

#   Queda pendiente CONCAT pues utiliza arrays.

# ------------------ LISTA DE EXPRESIONES PRIMITIVAS ------------------
def p_EXPRESION_cadena(p):
    """
    EXPRESION : cadena
    """
    p[0] = Primitivos(p[1], TipoDato.CADENA, p.lineno(1),
                  calcularColumna(input, p.slice[1]))
    
def p_EXPRESION_numero(p):
    """
    EXPRESION : numero
    """
    p[0] = Primitivos(p[1], TipoDato.NUMERO, p.lineno(1),
                  calcularColumna(input, p.slice[1]))

def p_EXPRESION_booleano(p):
    """
    EXPRESION : true
                | false
    """
    p[0] = Primitivos(p[1], TipoDato.BOOLEANO, p.lineno(1),
                  calcularColumna(input, p.slice[1]))
    
def p_EXPRESION_null(p):
    """
    EXPRESION : null
    """
    p[0] = Primitivos(p[1], TipoDato.NULL, p.lineno(1),
                  calcularColumna(input, p.slice[1]))
    
def p_EXPRESION_Acceso(p):
    """
    EXPRESION : id
    """
    p[0] = Acceso(p[1], p.lineno(1),
                  calcularColumna(input, p.slice[1]))
    
def p_EXPRESION_Vector(p):
    """
    EXPRESION : c_Abre LISTAEXPRESIONES c_Cierra
    """
    p[0] = Vector(p[2], p.lineno(1),
                  calcularColumna(input, p.slice[1]))


def p_TIPO_NUMBER(p):
    """
    TIPO : number
    """
    p[0] = Tipo.NUMBER

def p_TIPO_STRING(p):
    """
    TIPO : string
    """
    p[0] = Tipo.STRING

def p_TIPO_BOOLEAN(p):
    """
    TIPO : boolean
    """
    p[0] = Tipo.BOOLEAN

def p_TIPO_ANY(p):
    """
    TIPO : any
    """
    p[0] = Tipo.ANY


# Crea el analizador sintáctico
parser = yacc.yacc()

def parsear(inp):
    try:
        listaErrores.clear()
        generateLexer()
        parser = yacc.yacc()
        global input
        result = parser.parse(inp)
        return result
    except Exception as error:
        return None

def getErrores():
    listaAux = listaErrores
    return listaAux
