from enum import Enum
from source.abstracto.Retorno import Tipo, TipoDato

class TiposSimbolos(Enum):
    """
    Enum de tipos de datos que se pueden manejar en el lenguaje (variables, constantes, funciones, etc)
    """
    VARIABLE = 1

def getTipoSimbolo(s):
    if(s == 1):
        return TiposSimbolos.VARIABLE

class Simbolo:
    def __init__(self, tipoSimbolo:int, tipo: Tipo, tipoDato: TipoDato, id: str, valor):
        self.valor = valor
        self.id : str = id
        self.tipo : Tipo = tipo
        self.tipoDato : TipoDato = tipoDato
        self.tipoSimbolo : TiposSimbolos = getTipoSimbolo(tipoSimbolo)