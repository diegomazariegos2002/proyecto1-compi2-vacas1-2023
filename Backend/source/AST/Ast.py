from source.abstracto.Instruccion import Instruccion


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
        for instruccion in self.instrucciones:
            if isinstance(instruccion, Instruccion):
                print(type(instruccion))
                instruccion.ejecutar(ts)