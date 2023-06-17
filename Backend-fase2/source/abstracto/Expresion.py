from typing import Union
from source.abstracto.Retorno import Retorno, RetornoTraduccion
from source.errores.Excepcion import Excepcion
from source.simbolo.TablaSimbolos import TablaSimbolos

class Expresion:
    """
    Interfaz para las expresiones
    """

    def __init__(self, line:int, column:int):
        self.line = line
        self.column = column

    def ejecutar(self, ts: TablaSimbolos) -> Retorno:
        """
        Metodo para ejecutar la expresion y obtener su retorno
        """
        raise NotImplementedError("Subclasses must implement this method")
    
    def graficarAst(self) -> str:
        """
        Metodo para graficar con graphviz
        """
        raise NotImplementedError("Subclasses must implement this method")
    
    def traducir(self, ts) -> Union[RetornoTraduccion, Excepcion]:
        """
        Metodo para generar el código de la expresion
        """
        raise NotImplementedError("Subclasses must implement this method")