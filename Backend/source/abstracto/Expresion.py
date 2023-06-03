from source.abstracto.Retorno import Retorno
from source.simbolo.TablaSimbolos import TablaSimbolos

class Expresion:
    """
    Interfaz para las expresiones
    """

    def __init__(self, line:int, column:int):
        self.line = line
        self.column = column

    def ejecutar(self, ts: TablaSimbolos) -> Retorno:
        raise NotImplementedError("Subclasses must implement this method")