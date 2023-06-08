from datetime import datetime
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, TipoVariable, Tipo_OperadorAritmetico, TipoDato
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.Simbolo import Simbolo
from source.simbolo.TablaSimbolos import TablaSimbolos

class ToExponential(Expresion):
    def __init__(self, nombreVar:str, expresionEntrada:Expresion, line, column):
        super().__init__(line, column)
        self.expresionEntrada : Expresion = expresionEntrada
        self.nombreVar : str = nombreVar
        

    def ejecutar(self, ts: TablaSimbolos) -> Retorno:
        consolaGlobal = Consola()
        """igual que con toString() no se valida funcion.toExponential()"""
        idSimbolo : Simbolo = None
        if self.nombreVar != None:
            idSimbolo = ts.buscar(self.nombreVar)

            if idSimbolo == None:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error la variable no existe en llamada a toExponential(), no se puede operar expresion con ERROR", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)

            if idSimbolo.tipoDato == TipoDato.ERROR:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en toExponential(), no se puede operar expresion con ERROR", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
            # si no hay error, se puede operar
            # se verifica el valor primitivo        
            if idSimbolo.tipoDato == TipoDato.NUMERO:
                # se verifica que la expresion de entrada sea un numero
                retornoExpresionEntrada : Retorno = self.expresionEntrada.ejecutar(ts)
                if retornoExpresionEntrada.tipo == TipoDato.ERROR:
                    # ERROR
                    consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en toExponential(), no se puede operar expresion con ERROR", self.line, self.column, datetime.now()))
                    return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
                
                # se verifica que la expresion de entrada sea un numero
                if retornoExpresionEntrada.tipo != TipoDato.NUMERO:
                    # ERROR
                    consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en toExponential(), no se puede operar con valores diferentes de Number", self.line, self.column, datetime.now()))
                    return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
                
                # la expresion de entrada es un numero, se puede operar
                formatted_number = "{:.{}e}".format(idSimbolo.valor, retornoExpresionEntrada.valor)
                
                return Retorno(str(formatted_number), TipoDato.CADENA, TipoVariable.NORMAL)
        
        # ERROR
        consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error algo salio mal en la funcion nativa toExponential(), revisar parametros de la funcion", self.line, self.column, datetime.now()))
        return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL, TipoVariable.NORMAL)