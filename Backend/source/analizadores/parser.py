# Librerías implementadas
from ply import yacc
from .lexer import *
# Librerías propias
from source.abstracto.Retorno import Tipo, Tipo_OperadorAritmetico, TipoLogicas, TipoRelacionales
from source.expresiones.Primitivos import Primitivos
from source.expresiones.Aritmeticas import Arimeticas
from source.expresiones.Logicas import Logicas
from source.expresiones.Relacionales import Relacionales
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
