from datetime import datetime
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, TipoVariable, Tipo_OperadorAritmetico, TipoDato
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.TablaSimbolos import TablaSimbolos

class Concat(Expresion):
    def __init__(self, id, vectorExtra, line, column):
        super().__init__(line, column)
        self.id = id
        self.vectorExtra = vectorExtra
        

    def ejecutar(self, ts: TablaSimbolos) -> Retorno:
        consolaGlobal = Consola()
        
        variable = ts.buscar(self.id)

        if(variable == None):
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre '"+ self.id +"' no existe.", self.line, self.column, datetime.now()))
            return Retorno(0, TipoDato.ERROR, TipoVariable.NORMAL)
        
        if variable.tipoVariable != TipoVariable.VECTOR:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Para usar la función nativa concat se necesita que se realice con vectores.", self.line, self.column, datetime.now()))
            return Retorno(0, TipoDato.ERROR, TipoVariable.NORMAL)
        
        vectorRetorno = variable.valor
        vectorTipoDato = variable.tipoDato
        
        for vec in self.vectorExtra:
            vecAux : Retorno = vec.ejecutar(ts)
            if vecAux.tipoVariable != TipoVariable.VECTOR:
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Para usar la función nativa concat se necesita que se realice con vectores.", self.line, self.column, datetime.now()))
                return Retorno(0, TipoDato.ERROR, TipoVariable.NORMAL)
            
            vectorRetorno =  vectorRetorno + vecAux.valor
            if (vecAux.tipo != vectorTipoDato):
                vectorTipoDato = TipoDato.ANY
                
        print(vectorRetorno)
        
        return Retorno(vectorRetorno, vectorTipoDato, TipoVariable.VECTOR)