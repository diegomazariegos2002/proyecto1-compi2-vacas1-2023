#Recordar que lo mejor para importar estas librerías es tener el archivo de PLY en el mismo lugar que la gramatica.py
from source.abstracto.Retorno import Tipo
from source.expresiones.Literal import Literal
from source.instrucciones.Println import Println
import source.analizadores.ply.lex as lex

#Parte del analizador léxico

"""
Notas Importantes:
1. Todos los tokens definidos por funciones se agregan en el mismo orden en que aparecen en el archivo lexer.
2. Los tokens definidos por cadenas se agregan a continuación clasificándolos en orden decreciente de longitud de expresión regular (las expresiones más largas se agregan primero).
"""

#Declaración de tokens
reservadas = {
    'println': 'println'
}


tokens = [
        'cadena', 
        'p_Abre',
        'p_Cierre',
        'puntoYcoma'
        ] + list(reservadas.values())

#La r al principio de la cadena es para dar a entender que es una expresión regular
#Primera forma para definir tokens mediante funciones:

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value)    # Check for reserved words
     return t

def t_cadena(t):
    r'\".*?\"'
    t.value = t.value[1:-1] #devolvemos el valor del token sin las comillas dobles
    return t

#Segunda forma para definir tokens mediante asignacion:
t_p_Abre = r'\('
t_p_Cierre = r'\)'
t_puntoYcoma = r';'

#En caso de errores
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

analizadorLexico = lex.lex()

#Comienzo yacc o sea el analizador sintactico
import source.analizadores.ply.yacc as yacc

#Importaciones generales
from source.AST.Ast import Ast

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
    p[0] = p[1].append(p[2])

def p_ENTRADAS_PARTE_2(p):
    """
    ENTRADAS : ENTRADA
    """
    p[0] = [p[1]]

#Recordar que esto no es así, ya que no pueden venir instrucciones directamente en la entrada
#se necesita un método main. pero lo dejo así para pruebas rápidas.
def p_ENTRADA(p):
    """
    ENTRADA : INSTRUCCION
    """
    p[0] = p[1]

def p_INSTRUCCION_PRINTLN(p):
    """
    INSTRUCCION : PRINTLN
    """
    p[0] = p[1]


def p_PRINTLN(p):
    """
    PRINTLN : println p_Abre EXPRESION p_Cierre puntoYcoma
    """
    p[0] = Println(p[3], p.lineno(1), 0)

def p_EXPRESION(p):
    """
    EXPRESION : cadena
    """
    p[0] = Literal(p[1], Tipo.STRING, p.lineno(1), 0)

def p_error(p):
    if not p:
        print("Error sin recuperación")
        return

    # Read ahead looking for a closing ';'
    while True:
        tok = analizadorParser.token()             # Get the next token
        if not tok or tok.type == 'puntoYcoma': #Que se recupere al encontrar este token
            break
        print(f"Error sintactico {tok.type}")
    analizadorParser.restart() #Se reinicia el analizador si encuentra puntoYcoma

analizadorParser = yacc.yacc()

def parse(input):
    return analizadorParser.parse(input)