from source.abstracto.Instruccion import Instruccion
from source.instrucciones.funcion.Function import Function


class Ast:
    """
    Mi clase AST que básicamente voy a utilizar como la clase para almacenar todas mis instrucciones
    que me devuelva la gramática y posteriormente ejecutar en el main (de ahí que tenga dos métodos).
    """

    def __init__(self, instrucciones=None):
        if instrucciones is None:
            instrucciones = []

        self.instrucciones = instrucciones

    def ejecutar(self, ts):
        # Primera pasada (Funciones)
        for instruccion in self.instrucciones:
            if isinstance(instruccion, Instruccion):
                if isinstance(instruccion, Function):
                    instruccion.ejecutar(ts)
                    
        # Segunda pasada (Instrucciones)
        for instruccion in self.instrucciones:
            if isinstance(instruccion, Instruccion):
                if not isinstance(instruccion, Function):
                    instruccion.ejecutar(ts)