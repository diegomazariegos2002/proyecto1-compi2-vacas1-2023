from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, Tipo
from source.simbolo.TablaSimbolos import TablaSimbolos

class Arimeticas(Expresion):
    def __init__(self, operador, izq, der, line, column):
        super().__init__(line, column)
        self.operador = operador
        self.izq : Expresion = izq
        self.der : Expresion = der
        self.unico : Expresion = None
        if self.der == None:
            self.unico = self.izq
        

    def ejecutar(self, ts: TablaSimbolos) -> Retorno:
        valorIzq : Retorno = None
        valorDer : Retorno = None
        valorUnico : Retorno = None
        if self.unico != None:
            valorUnico = self.unico.ejecutar(ts)
            if valorUnico.tipo == Tipo.ERROR:
                return 



        return Retorno(0, Tipo.ERROR)