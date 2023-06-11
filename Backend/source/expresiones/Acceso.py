
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, Tipo, TipoDato, TipoVariable
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.TablaSimbolos import TablaSimbolos
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