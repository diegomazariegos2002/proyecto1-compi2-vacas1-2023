
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, Tipo
from source.simbolo.TablaSimbolos import TablaSimbolos


class Primitivos(Expresion):

    def __init__(self, valor, tipo:Tipo, line: int, column: int):
        super().__init__(line, column)
        self.valor = valor
        self.tipo = tipo
    
    def ejecutar(self, ts: TablaSimbolos) -> Retorno:
        if(self.tipo == Tipo.STRING):
            return Retorno(self.valor, self.tipo)
        if(self.tipo == Tipo.NUMBER):
            return Retorno(self.valor, self.tipo)
        if(self.tipo == Tipo.BOOLEAN):
            return Retorno(self.valor, self.tipo)
        if(self.tipo == Tipo.NULL):
            return Retorno(None, self.tipo)
        if(self.tipo == Tipo.ANY):
            return Retorno(self.valor, self.tipo)

        
        return Retorno(0, Tipo.ERROR)