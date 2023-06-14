from datetime import datetime
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, TipoVariable, Tipo_OperadorAritmetico, TipoDato
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.Simbolo import Simbolo
from source.simbolo.TablaSimbolos import TablaSimbolos

class ToFixed(Expresion):
    def __init__(self, nombreVar:str, expresionEntrada:Expresion, line, column):
        super().__init__(line, column)
        self.expresionEntrada : Expresion = expresionEntrada
        self.nombreVar : str = nombreVar
        

    def ejecutar(self, ts: TablaSimbolos) -> Retorno:
        consolaGlobal = Consola()
        """igual que con toString() no se valida funcion.toFixed()"""
        idSimbolo : Simbolo = None
        if self.nombreVar != None:
            idSimbolo = ts.buscar(self.nombreVar)

            if idSimbolo == None:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error la variable no existe en llamada a toFixed(), no se puede operar expresion con ERROR", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)

            if idSimbolo.tipoDato == TipoDato.ERROR:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en toFixed(), no se puede operar expresion con ERROR", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
            # si no hay error, se puede operar
            # se verifica el valor primitivo        
            if idSimbolo.tipoDato == TipoDato.NUMERO:
                # se verifica que la expresion de entrada sea un numero
                retornoExpresionEntrada : Retorno = self.expresionEntrada.ejecutar(ts)
                if retornoExpresionEntrada.tipo == TipoDato.ERROR:
                    # ERROR
                    consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en toFixed(), no se puede operar expresion con ERROR", self.line, self.column, datetime.now()))
                    return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
                
                # se verifica que la expresion de entrada sea un numero
                if retornoExpresionEntrada.tipo != TipoDato.NUMERO:
                    # ERROR
                    consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en toFixed(), no se puede operar con valores diferentes de Number", self.line, self.column, datetime.now()))
                    return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
                
                # la expresion de entrada es un numero, se puede operar
                formatted_number = "{:.{}f}".format(idSimbolo.valor, retornoExpresionEntrada.valor)
                return Retorno(str(formatted_number), TipoDato.CADENA, TipoVariable.NORMAL)
        
        # ERROR
        consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error algo salio mal en la funcion nativa toFixed(), revisar parametros de la funcion", self.line, self.column, datetime.now()))
        return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL, TipoVariable.NORMAL)
    
    def graficarAst(self):
        consola = Consola()
        nombreNodo = f"instruccion_{self.line}_{self.column}_{str(id(self))}_"
        consola.set_AstGrafico(f"{nombreNodo}[label=\"\\<Expresion\\>\\ntoFixed\"];\n")
        nombreNodoId = f"instruccion_{self.line}_{self.column}_{str(id(self))}_id_"
        consola.set_AstGrafico(f"{nombreNodoId}[label=\"\\<Identificador\\>\\n{self.nombreVar}\"];\n")
        consola.set_AstGrafico(f"{nombreNodo}->{nombreNodoId};\n")
        consola.set_AstGrafico(f"{nombreNodo}->{self.expresionEntrada.graficarAst()};\n")
        return nombreNodo