from typing import Union
from source.errores.Excepcion import Excepcion
from source.simbolo.TablaSimbolos import TablaSimbolos

class Instruccion:
    """
    interfaz para las instrucciones
    """

    def __init__(self, line:int, column:int):
        self.line = line
        self.column = column
        # fase 2
        # etiquetas para el control de flujo en los entornos
        self.etqSalida = None
        self.etqContinue = None
        self.etqBreak = None
        self.etqReturn = None

    def ejecutar(self, ts: TablaSimbolos):
        """
        ejecutar puede retornar none o un valor (Instruccion, Expresion, Errores, etc)
        """
        raise NotImplementedError("Subclasses must implement this method")
    
    def graficarAst(self) -> str:
        """
        Metodo para graficar con graphviz
        """
        raise NotImplementedError("Subclasses must implement this method")
    
    def traducir(self, ts) -> Union[str, Excepcion]:
        """
        Metodo para generar el código de la expresion
        """
        raise NotImplementedError("Subclasses must implement this method")