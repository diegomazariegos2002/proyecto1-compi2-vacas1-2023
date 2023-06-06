from enum import Enum

class Tipo(Enum):
    """
    Enum de tipos de datos que se pueden manejar en el lenguaje
    """

    NULL = 1
    NUMBER = 2
    BOOLEAN = 3
    STRING = 4
    ANY = 5
    ARRAY = 6
    INTERFACE = 7
    ERROR = 10

class Tipo_OperadorAritmetico(Enum):
    """
    Enum de operadores aritmeticos
    """
    SUMA = 1
    RESTA = 2
    MULTIPLICACION = 3
    DIVISION = 4
    POTENCIA = 5
    MODULO = 7
    NEGATIVO = 8

class TipoLogicas(Enum):
    """
    Enum de operadores logicos
    """
    AND = 1
    OR = 2
    NOT = 3


def getTipo(s: str):
    if s == "NULL":
        return Tipo.NULL
    if s == "NUMBER":
        return Tipo.NUMBER
    if s == "BOOLEAN":
        return Tipo.BOOLEAN
    if s == "STRING":
        return Tipo.STRING
    if s == "ANY":
        return Tipo.ANY
    if s == "ARRAY":
        return Tipo.ARRAY
    if s == "INTERFACE":
        return Tipo.INTERFACE
    return Tipo.ERROR

class Retorno: 
    """
    Retorno de una expresion
    """

    def __init__(self, valor:None, tipo:Tipo) -> None:
        self.valor = valor
        self.tipo = tipo

