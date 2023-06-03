from enum import Enum

class Tipo(Enum):
    """
    Enum de tipos de datos que se pueden manejar en el lenguaje
    """

    INT64 = 1
    FLOAT64 = 2
    STRING = 3
    ERROR = 10


def getTipo(s: str):
    if s == "INT64":
        return Tipo.INT64
    if s == "FLOAT64":
        return Tipo.FLOAT64
    if s == "STRING":
        return Tipo.STRING


def definirTipo(value):
    if type(value) == float:
        return Tipo.FLOAT64
    elif type(value) == int:
        return Tipo.INT64
    elif type(value) == str:
        return Tipo.STRING
    else:
        return None
    
class Retorno: 
    """
    Retorno de una expresion
    """

    def __init__(self, valor:None, tipo:Tipo) -> None:
        self.valor = valor
        self.tipo = tipo

