from datetime import datetime
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, TipoVariable, Tipo_OperadorAritmetico, TipoDato, Tipo
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.TablaSimbolos import TablaSimbolos

class Split(Expresion):
    def __init__(self, id, separador, line, column):
        super().__init__(line, column)
        self.id = id
        self.separador : Expresion = separador
        

    def ejecutar(self, ts: TablaSimbolos) -> Retorno:
        consolaGlobal = Consola()
        
        variable = ts.buscar(self.id)

        if(variable == None):
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre '"+ self.id +"' no existe.", self.line, self.column, datetime.now()))
            return Retorno(0, TipoDato.ERROR, TipoVariable.NORMAL)
        
        if variable.tipoDato != TipoDato.CADENA:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "La variable para la función nativa split debe ser de tipo string.", self.line, self.column, datetime.now()))
            return Retorno(0, TipoDato.ERROR, TipoVariable.NORMAL)
        
        separadorSplit : Retorno = self.separador.ejecutar(ts)
        
        if separadorSplit.tipo != TipoDato.CADENA:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "El separador para la funcion nativa split debe ser dentro de una cadena.", self.line, self.column, datetime.now()))
            return Retorno(0, TipoDato.ERROR, TipoVariable.NORMAL)
        
        separadorSeco = separadorSplit.valor[1:-1]
        
        splitHecho = variable.valor.split(separadorSplit.valor)
        
        vectorRetorno = []
        
        for s in splitHecho:
            vectorRetorno.append(Retorno(s, TipoDato.CADENA, TipoVariable.NORMAL))
        
        return Retorno(vectorRetorno, TipoDato.CADENA, TipoVariable.VECTOR)