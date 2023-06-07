
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, Tipo, TipoDato
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.TablaSimbolos import TablaSimbolos


class Primitivos(Expresion):

    def __init__(self, valor, tipo:Tipo, line: int, column: int):
        super().__init__(line, column)
        self.valor = valor
        self.tipo = tipo
    
    def ejecutar(self, ts: TablaSimbolos) -> Retorno:
        consolaGlobal = Consola()
        if(self.tipo == TipoDato.CADENA):
            return Retorno(self.valor, self.tipo)
        if(self.tipo == TipoDato.NUMERO):
            return Retorno(self.valor, self.tipo)
        if(self.tipo == TipoDato.BOOLEANO):
            if(self.valor == "true"):
                return Retorno(True, self.tipo)
            if(self.valor == "false"):
                return Retorno(False, self.tipo)
        if(self.tipo == TipoDato.NULL):
            return Retorno(None, self.tipo)
        if(self.tipo == TipoDato.ANY):
            return Retorno(self.valor, self.tipo)

        consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Tipo de dato no reconocido", self.line, self.column))
        return Retorno(0, Tipo.ERROR)