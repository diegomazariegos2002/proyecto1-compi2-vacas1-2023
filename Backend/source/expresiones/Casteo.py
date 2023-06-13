from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, Tipo, TipoDato, TipoVariable
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.TablaSimbolos import TablaSimbolos
from datetime import datetime

class Casteo(Expresion):
    def __init__(self, tipo:Tipo, expresion: Expresion, line: int, column: int):
        super().__init__(line, column)
        self.tipo = tipo
        self.expresion = expresion
    
    def ejecutar(self, ts: TablaSimbolos) -> Retorno:
        consolaGlobal = Consola()
        
        expresionEjecutada:Retorno = self.expresion.ejecutar(ts)
        
        if expresionEjecutada.tipo == TipoDato.ERROR:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Ocurrio un error ejecutando la expresion.", self.line, self.column, datetime.now()))
            return Retorno(0, TipoDato.ERROR, TipoVariable.NORMAL)
        
        if expresionEjecutada.tipoVariable == TipoVariable.VECTOR:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "No se puede castear un vector directamente.", self.line, self.column, datetime.now()))
            return Retorno(0, TipoDato.ERROR, TipoVariable.NORMAL)
        
        if self.tipo == Tipo.ANY:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Para usar un casteo se necesita un tipo de dato definido, no any.", self.line, self.column, datetime.now()))
            return Retorno(0, TipoDato.ERROR, TipoVariable.NORMAL)
           
        if self.tipo == Tipo.STRING:
            if expresionEjecutada.tipo == TipoDato.BOOLEANO:
                if expresionEjecutada.valor == True:
                    return Retorno("true", TipoDato.CADENA, TipoVariable.NORMAL)
                elif expresionEjecutada.valor == False:
                    return Retorno("false", TipoDato.CADENA, TipoVariable.NORMAL)
            elif expresionEjecutada.tipo == TipoDato.NUMERO:
                return Retorno(str(expresionEjecutada.valor), TipoDato.CADENA, TipoVariable.NORMAL)
            elif expresionEjecutada.tipo == TipoDato.NULL:
                return Retorno("null", TipoDato.CADENA, TipoVariable.NORMAL)
            elif expresionEjecutada.tipo == TipoDato.CADENA:
                return Retorno(expresionEjecutada.valor, TipoDato.CADENA, TipoVariable.NORMAL)
            else:
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "No se pudo realizar el casteo a String.", self.line, self.column, datetime.now()))
                return Retorno(0, TipoDato.ERROR, TipoVariable.NORMAL)
        elif self.tipo == Tipo.NUMBER:
            if expresionEjecutada.tipo == TipoDato.CADENA:
                if self.isNumeric(expresionEjecutada.valor)  == True:
                    return Retorno(float(expresionEjecutada.valor), TipoDato.NUMERO, TipoVariable.NORMAL)
            elif expresionEjecutada.tipo == TipoDato.NUMERO:
                return Retorno(expresionEjecutada.valor, TipoDato.NUMERO, TipoVariable.NORMAL)
            else:
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "No se pudo realizar el casteo a Number.", self.line, self.column, datetime.now()))
                return Retorno(0, TipoDato.ERROR, TipoVariable.NORMAL)
        elif self.tipo == Tipo.BOOLEAN:
            if expresionEjecutada.tipo != TipoDato.BOOLEANO:
                if expresionEjecutada.tipo == TipoDato.CADENA:
                    if expresionEjecutada.valor  == "true":
                        return Retorno(True, TipoDato.CADENA, TipoVariable.NORMAL)
                    elif expresionEjecutada.valor == "false":
                        return Retorno(False, TipoDato.CADENA, TipoVariable.NORMAL)
                else:
                    consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "No se pudo realizar el casteo a Number.", self.line, self.column, datetime.now()))
                    return Retorno(0, TipoDato.ERROR, TipoVariable.NORMAL)
            else:
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "No se puede castear la expresion a un Boolean.", self.line, self.column, datetime.now()))
                return Retorno(0, TipoDato.ERROR, TipoVariable.NORMAL)
        
    
    def isNumeric(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False