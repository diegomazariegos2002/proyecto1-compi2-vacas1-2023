from datetime import datetime
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, TipoVariable, Tipo_OperadorAritmetico, TipoDato
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.Simbolo import Simbolo
from source.simbolo.TablaSimbolos import TablaSimbolos

class Length(Expresion):
    def __init__(self, nombreVar : str, line, column):
        super().__init__(line, column)
        self.nombreVar : str = nombreVar
        
    def ejecutar(self, ts: TablaSimbolos) -> Retorno:
        """
        la funcion nativa ToString() recibe un id de una variable y retorna el valor de la variable en string
        recordar que al menos aquí no he tomado en cuenta
        el retorno de las funciones. [funcion.toString()]
        """
        consolaGlobal = Consola()
        idSimbolo : Simbolo = None
        if self.nombreVar != None:
            idSimbolo = ts.buscar(self.nombreVar)

            if idSimbolo == None:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error la variable no existe en llamada a Length(), no se puede operar expresion con ERROR", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)

            if idSimbolo.tipoDato == TipoDato.ERROR:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en Length(), no se puede operar expresion con ERROR", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
            # si no hay error, se puede operar
            # se verifica el valor primitivo            
            if idSimbolo.tipoVariable == TipoVariable.VECTOR:
                return Retorno(len(idSimbolo.valor), TipoDato.NUMERO, TipoVariable.NORMAL)
            elif idSimbolo.tipoDato == TipoDato.CADENA:
                return Retorno(len(idSimbolo.valor), TipoDato. NUMERO, TipoVariable.NORMAL)
            
        # ERROR
        consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error algo salio mal en la funcion nativa Length(), revisar parametros de la funcion", self.line, self.column, datetime.now()))
        return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
    
    def graficarAst(self):
        consola = Consola()
        nombreNodo = f"instruccion_{self.line}_{self.column}_{str(id(self))}_"
        consola.set_AstGrafico(f"{nombreNodo}[label=\"\\<Expresion\\>\\ntoString\"];\n")
        nombreNodoId = f"instruccion_{self.line}_{self.column}_{str(id(self))}_id_"
        consola.set_AstGrafico(f"{nombreNodoId}[label=\"\\<Identificador\\>\\n{self.nombreVar}\"];\n")
        consola.set_AstGrafico(f"{nombreNodo}->{nombreNodoId};\n")
        return nombreNodo