from source.simbolo.TablaSimbolos import TablaSimbolos

class Instruccion:
    """
    interfaz para las instrucciones
    """

    def __init__(self, line:int, column:int):
        self.line = line
        self.column = column

    def ejecutar(self, ts: TablaSimbolos):
        """
        ejecutar puede retornar none o un valor (Instruccion, Expresion, Errores, etc)
        """
        raise NotImplementedError("Subclasses must implement this method")
    
    def graficarAst(self) -> None:
        """
        Metodo para graficar con graphviz
        """
        raise NotImplementedError("Subclasses must implement this method")