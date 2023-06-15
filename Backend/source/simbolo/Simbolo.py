from enum import Enum
from source.abstracto.Retorno import Tipo, TipoDato, TipoVariable

class TiposSimbolos(Enum):
    """
    Enum de tipos de datos que se pueden manejar en el lenguaje (variables, constantes, funciones, etc)
    """
    VARIABLE = 1
    FUNCTION = 2
    INTERFACE = 3

def getTipoSimbolo(s):
    if(s == 1):
        return TiposSimbolos.VARIABLE

class Simbolo:
    def __init__(self, tipoSimbolo:TiposSimbolos, tipo: Tipo, tipoDato: TipoDato, id: str, valor,tipoVariable: TipoVariable ):
        self.valor = valor
        self.id : str = id
        self.tipo : Tipo = tipo
        self.tipoDato : TipoDato = tipoDato
        self.tipoSimbolo : TiposSimbolos = tipoSimbolo
        self.tipoVariable: TipoVariable = tipoVariable