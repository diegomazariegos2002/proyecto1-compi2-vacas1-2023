from ply import lex
from source.consola_singleton.Consola import Consola

from source.errores.Excepcion import Excepcion

#Parte del analizador léxico

"""
Notas Importantes:
1. Todos los tokens definidos por funciones se agregan en el mismo orden en que aparecen en el archivo lexer.
2. Los tokens definidos por cadenas se agregan a continuación clasificándolos en orden decreciente de longitud de expresión regular (las expresiones más largas se agregan primero).
"""

listaErrores = []

#Declaración de tokens
reservadas = {
    'console': 'console',
    'log': 'log',
    'true': 'true',
    'false': 'false',
    'null': 'null',
    'any': 'any'
}


tokens = [
        'cadena', 
        'p_Abre',
        'p_Cierra',
        'igual',
        'puntoYcoma',
        'punto',
        'suma',
        'resta',
        'multiplicacion',
        'division',
        'modulo',
        'potencia',
        'numero',
        'coma',
        'id',
        'and',
        'or',
        'not',
        'igualacion',
        'diferente',
        'mayor',
        'menor',
        'mayorigual',
        'menorigual'
        ] + list(reservadas.values())

#La r al principio de la cadena es para dar a entender que es una expresión regular
#Primera forma para definir tokens mediante funciones:

def t_id(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value)    # Check for reserved words
    if t.type == None:
        Consola().set_Excepcion(Excepcion("ERROR LEXICO", "EL TOKEN " + t.value+" NO SE RECONOCE EN LAS RESERVADAS", t.lexer.lineno, t.lexer.lexpos))
    return t

def t_cadena(t):
    r'[\"]((\\\")|[^\"\n])*[\"]'
    t.value = t.value[1:-1]
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace('\\r', '\r')
    t.value = t.value.replace('\\\\', '\\')
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace("\\'", '\'')
    return t

def t_numero(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

#Segunda forma para definir tokens mediante asignacion:
t_p_Abre = r'\('
t_p_Cierra = r'\)'
t_igual = r'='
t_puntoYcoma = r';'
t_punto = r'\.'
t_suma = r'\+'
t_resta = r'-'
t_multiplicacion = r'\*'
t_division = r'/'
t_modulo = r'%'
t_potencia = r'\^'
t_coma = r'\,'
t_and = r'\&\&'
t_or = r'\|\|'
t_not = r'\!'
t_menor = r'<'
t_mayor = r'>'
t_menorigual = r'<='
t_mayorigual = r'>='
t_igualacion = r'==='
t_diferente = r'\!=='
t_ignore = ' \t'
t_ignore_COMENTARIOS = r'(\/\/.*[^\n])'
t_ignore_MULTCOMENTARIOS = r'(\/\*([^*/]|[^*]\/|\*[^/])*\*\/)'


def t_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#En caso de errores
def t_error(t):
    Consola().set_Excepcion(Excepcion("ERROR LEXICO", "EL TOKEN " +
                        t.value[0]+" NO SE RECONOCE", t.lexer.lineno, t.lexer.lexpos))
    listaErrores.append(Excepcion("ERROR LEXICO", "EL TOKEN " +
                        t.value[0]+" NO SE RECONOCE", t.lexer.lineno, t.lexer.lexpos))
    t.lexer.skip(1)

analizadorLexico = lex.lex()

# Construir el lexer
def generateLexer():
    global lexer
    lexer = lex.lex()