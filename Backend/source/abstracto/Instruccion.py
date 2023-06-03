from source.simbolo.TablaSimbolos import TablaSimbolos

class Instruccion:
    """
    interfaz para las instrucciones
    """

    def __init__(self, line:int, column:int):
        self.line = line
        self.column = column

    def ejecutar(self, ts: TablaSimbolos):
        raise NotImplementedError("Subclasses must implement this method")