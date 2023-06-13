
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, Tipo, TipoDato, TipoVariable
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
            return Retorno(self.valor, self.tipo, TipoVariable.NORMAL)
        if(self.tipo == TipoDato.NUMERO):
            return Retorno(self.valor, self.tipo, TipoVariable.NORMAL)
        if(self.tipo == TipoDato.BOOLEANO):
            if(self.valor == "true"):
                return Retorno(True, self.tipo, TipoVariable.NORMAL)
            if(self.valor == "false"):
                return Retorno(False, self.tipo, TipoVariable.NORMAL)
        if(self.tipo == TipoDato.NULL):
            return Retorno(None, self.tipo, TipoVariable.NORMAL)
        if(self.tipo == TipoDato.ANY):
            return Retorno(self.valor, self.tipo, TipoVariable.NORMAL)

        consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Tipo de dato no reconocido", self.line, self.column))
        return Retorno(0, Tipo.ERROR, TipoVariable.NORMAL)
    
    def graficarAst(self) -> str:
        nombre = f'node_{self.line}_{self.column}_'
        output = ""
        output+= f"{nombre};"
        output+= f"{nombre}[label=\"<Valor>\n\\\"{self.valor}\\\"\"];"
        
        return output