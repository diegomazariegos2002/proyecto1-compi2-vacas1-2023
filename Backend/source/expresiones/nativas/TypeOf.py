from datetime import datetime
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, TipoVariable, Tipo_OperadorAritmetico, TipoDato
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.Simbolo import Simbolo
from source.simbolo.TablaSimbolos import TablaSimbolos

class TypeOf(Expresion):
    def __init__(self, expresion, line, column):
        super().__init__(line, column)
        self.expresion = expresion
        
    def ejecutar(self, ts: TablaSimbolos) -> Retorno:
        consolaGlobal = Consola()
        expresionEjecutada:Retorno = self.expresion.ejecutar(ts)

        if expresionEjecutada.tipo == TipoDato.ERROR:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Ocurrio un error ejecutando la expresion.", self.line, self.column, datetime.now()))
            return Retorno(0, TipoDato.ERROR, TipoVariable.NORMAL)
        
        if expresionEjecutada.tipoVariable == TipoVariable.VECTOR:
            return Retorno("Vector", TipoDato.CADENA, TipoVariable.NORMAL)
        elif expresionEjecutada.tipoVariable == TipoVariable.NORMAL:
            if expresionEjecutada.tipo == TipoDato.BOOLEANO:
                return Retorno("boolean", TipoDato.CADENA, TipoVariable.NORMAL)
            elif expresionEjecutada.tipo == TipoDato.CADENA:
                return Retorno("string", TipoDato.CADENA, TipoVariable.NORMAL)
            elif expresionEjecutada.tipo == TipoDato.NUMERO:
                return Retorno("number", TipoDato.CADENA, TipoVariable.NORMAL)
            elif expresionEjecutada.tipo == TipoDato.NULL:
                return Retorno("null", TipoDato.CADENA, TipoVariable.NORMAL)
            
        # ERROR
        consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error algo salio mal en la funcion nativa TypeOf(), revisar parametros de la funcion", self.line, self.column, datetime.now()))
        return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)