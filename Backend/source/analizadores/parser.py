# Librerías implementadas
from ply import yacc
from .lexer import *
# Librerías propias
from source.abstracto.Retorno import Tipo
from source.expresiones.Primitivos import Primitivos
from source.instrucciones.ConsoleLog import ConsoleLog
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
    ('left', 'suma', 'resta'),
    ('left', 'multiplicacion', 'division', 'modulo'),
    ('nonassoc', 'potencia')
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

# ------------------ LISTA DE EXPRESIONES ARITMETICAS ------------------


# ------------------ LISTA DE EXPRESIONES PRIMITIVAS ------------------
def p_EXPRESION_cadena(p):
    """
    EXPRESION : cadena
    """
    p[0] = Primitivos(p[1], Tipo.STRING, p.lineno(1),
                  calcularColumna(input, p.slice[1]))
    
def p_EXPRESION_numero(p):
    """
    EXPRESION : numero
    """
    p[0] = Primitivos(p[1], Tipo.NUMBER, p.lineno(1),
                  calcularColumna(input, p.slice[1]))

def p_EXPRESION_booleano(p):
    """
    EXPRESION : true
                | false
    """
    p[0] = Primitivos(p[1], Tipo.BOOLEAN, p.lineno(1),
                  calcularColumna(input, p.slice[1]))
    
def p_EXPRESION_null(p):
    """
    EXPRESION : null
    """
    p[0] = Primitivos(p[1], Tipo.NULL, p.lineno(1),
                  calcularColumna(input, p.slice[1]))
    
def p_EXPRESION_any(p):
    """
    EXPRESION : any
    """
    p[0] = Primitivos(p[1], Tipo.ANY, p.lineno(1),
                  calcularColumna(input, p.slice[1]))
    
def p_error(p):
    print("Error sintactico '%s'" % p.value)
    print("El token \""+ str(p.value) + "\" no se esperaba.")
    print(p.lexer.lineno)
    print(calcularColumna(input, p.slice[1]))
    p.lexer.skip(1)


# Crea el analizador sintáctico
parser = yacc.yacc()

def parsear(inp):
    generateLexer()
    parser = yacc.yacc()
    global input
    result = parser.parse(inp)
    return result
