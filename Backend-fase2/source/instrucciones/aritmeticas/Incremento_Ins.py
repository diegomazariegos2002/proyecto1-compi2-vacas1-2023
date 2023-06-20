from datetime import datetime
from source.abstracto.Expresion import Expresion
from source.abstracto.Instruccion import Instruccion
from source.abstracto.Retorno import Retorno, RetornoTraduccion, Tipo, TipoVariable, TipoDato
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.Simbolo import Simbolo, SimboloTraduccion
from source.simbolo.TablaSimbolos import TablaSimbolos


class Incremento_Ins(Instruccion):

    def __init__(self, nombreVar:str, line: int, column: int):
        super().__init__(line, column)
        self.nombreVar = nombreVar

    def ejecutar(self, ts: TablaSimbolos):
        consolaGlobal = Consola()

        variable : Simbolo = ts.buscar(self.nombreVar)
        # validar que todo este bien antes de actualizar la variable
        if variable is None:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la asignacion, variable sin declarar", self.line, self.column, datetime.now()))
            return Excepcion()
        if variable.tipoVariable != TipoVariable.NORMAL:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "No se puede incrementar un vector", self.line, self.column, datetime.now()))
            return Excepcion()
        
        if variable.tipoDato != TipoDato.NUMERO: # validar que la variable sea de tipo numerico
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", f"Asignacion incorrecta, la variable con nombre '{self.nombreVar}' es de tipo [{variable.tipo}] y se le esta tratando de incrementar como si fuera numerica.", self.line, self.column, datetime.now()))                
                return Excepcion()
        
        # si todo esta bien, se actualiza la variable    
        ts.actualizarVariable(self.nombreVar, variable.valor + 1)
        
    def graficarAst(self):
        consola = Consola()
        nombreNodo = f"instruccion_{self.line}_{self.column}_{str(id(self))}_"
        nombreNodoId = f"instruccion_{self.line}_{self.column}_{str(id(self))}_id"
        consola.set_AstGrafico(f"{nombreNodo}[label=\"\\<Instruccion\\>\\nIncremento (++)\"];\n")
        consola.set_AstGrafico(f"{nombreNodoId}[label=\"\\<Identificador\\>\\n{self.nombreVar}\"];\n")
        consola.set_AstGrafico(f"{nombreNodo} -> {nombreNodoId};\n")
        return nombreNodo
    
    def traducir(self, ts: TablaSimbolos):
        consolaGlobal: Consola = Consola()
        cadenaRetorno = ""
        variable : SimboloTraduccion = ts.buscar(self.nombreVar)
        # validar que todo este bien antes de actualizar la variable
        if variable is None:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la asignacion, variable sin declarar", self.line, self.column, datetime.now()))
            return Excepcion()
        if variable.tipoVariable != TipoVariable.NORMAL or variable.tipo != Tipo.NUMBER:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "No se puede aumentar nada que no sea una variable numerica", self.line, self.column, datetime.now()))
            return Excepcion()
        
        # obtener el valor de la variable
        t0 = consolaGlobal.genNewTemp()
        t1 = consolaGlobal.genNewTemp()
        cadenaRetorno += consolaGlobal.genComment("INSTRUCCION INCREMENTO")
        cadenaRetorno += consolaGlobal.genAsignacion(t0, "SP + {}".format(variable.direccion))
        cadenaRetorno += consolaGlobal.genAsignacion(t1, "STACK[int({})]".format(t0))
        
        # si todo esta bien, se actualiza la variable 
        cadenaRetorno += consolaGlobal.genComment("Asignacion Variable {}".format(self.nombreVar))
        t2 = consolaGlobal.genNewTemp()
        cadenaRetorno += consolaGlobal.genAsignacion(t2, t1 +"+1")
        cadenaRetorno += consolaGlobal.genAsignacion("STACK[int({})]".format(t0), t2)
        ts.actualizarVariable(self.nombreVar, t0)
        return cadenaRetorno
        
