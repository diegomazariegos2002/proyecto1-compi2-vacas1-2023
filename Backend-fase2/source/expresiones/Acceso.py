
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, Tipo, TipoDato, TipoVariable, RetornoTraduccion
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.TablaSimbolos import TablaSimbolos
from source.simbolo.Simbolo import SimboloTraduccion
from datetime import datetime

class Acceso(Expresion):
    def __init__(self, id, line: int, column: int):
        super().__init__(line, column)
        self.id = id
    
    def ejecutar(self, ts: TablaSimbolos) -> Retorno:
        consolaGlobal = Consola()
        variable = ts.buscar(self.id)

        if(variable == None):
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre '"+ self.id +"' no existe.", self.line, self.column, datetime.now()))
            return Retorno(0, TipoDato.ERROR, TipoVariable.NORMAL)
        
        return Retorno(variable.valor, variable.tipoDato, variable.tipoVariable)
    
    def graficarAst(self):
        consola = Consola()
        nombreNodo = f"instruccion_{self.line}_{self.column}_{str(id(self))}_"
        consola.set_AstGrafico(f"{nombreNodo}[label=\"\\<Identificador\\>\\n{self.id}\"];\n")
        return nombreNodo
    
    def traducir(self, ts):
        consolaGlobal = Consola()
        variable:SimboloTraduccion = ts.buscar(self.id)

        if(variable == None):
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre '"+ self.id +"' no existe.", self.line, self.column, datetime.now()))
            return RetornoTraduccion(valor=0,
                                 tipo=TipoDato.ERROR,
                                 tipoVariable=TipoVariable.NORMAL,
                                 codigoTraducido=consolaGlobal.genComment("La variable con el nombre '"+ self.id +"' no existe."))
        t0 = consolaGlobal.genNewTemp()
        cad = consolaGlobal.genAsignacion(t0, "SP + {}".format(variable.direccion))
        cad += consolaGlobal.genAsignacion(variable.temporal, "STACK[int({})]".format(t0))
        
        return RetornoTraduccion(valor=variable.temporal,
                                tipo=variable.tipoDato,
                                tipoVariable=variable.tipoVariable,
                                codigoTraducido= consolaGlobal.genComment("Acceso Variable {}".format(self.id))+cad)