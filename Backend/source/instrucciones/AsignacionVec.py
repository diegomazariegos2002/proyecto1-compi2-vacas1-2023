from datetime import datetime
from source.abstracto.Expresion import Expresion
from source.abstracto.Instruccion import Instruccion
from source.abstracto.Retorno import Retorno, Tipo, TipoVariable, TipoDato
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.Simbolo import Simbolo
from source.simbolo.TablaSimbolos import TablaSimbolos


class AsignacionVec(Instruccion):

    def __init__(self, nombreVar:str, indices, expresionAsignar:Expresion, line: int, column: int):
        super().__init__(line, column)
        self.nombreVar = nombreVar
        self.expresionAsignar = expresionAsignar
        self.indices = indices

    def ejecutar(self, ts: TablaSimbolos):
        consolaGlobal = Consola()
        expresionRetorno : Retorno = self.expresionAsignar.ejecutar(ts)
        indices = []
        i: Expresion = None
        for i in self.indices:
            indi:Retorno = i.ejecutar(ts)
            if indi.tipo != Tipo.NUMBER:
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "El indice para un vector debe ser numérico", self.line, self.column, datetime.now()))
                return
            indices.append(indi)

        variable : Simbolo = ts.buscar(self.nombreVar)
        # validar que todo este bien antes de actualizar la variable
        if variable is None:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la asignacion, variable sin declarar", self.line, self.column, datetime.now()))
            return

        if variable.tipoVariable != TipoVariable.VECTOR:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "La variable a la que se quiere acceder no es un vector.", self.line, self.column, datetime.now()))
            return

        varVal:Retorno = variable.valor

        for x in range(0, len(indices)):
            if x == len(indices)-1:
                varVal = varVal[indices[x]]
                if  varVal.tipo == expresionRetorno.tipo or varVal.tipo == TipoDato.ANY:
                    varVal = expresionRetorno
                else:
                    consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Los tipo de datos de las variables no coinciden", self.line, self.column, datetime.now()))
                    return
            else:
                if  varVal.tipoVariable == TipoVariable.VECTOR:
                    varVal = varVal[indices[x]]
                else:
                    consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "No existe el indice al que se desea acceder en el vector.", self.line, self.column, datetime.now()))
                    return

        if variable.tipo != consolaGlobal.relacionarTipos(expresionRetorno.tipo): # validar que los tipos sean iguales
            if variable.tipo == Tipo.ANY: # si la variable es de tipo ANY, se le asigna el tipo de la expresion
                # Actualizando el tipoDato de la variable ANY
                variable.tipoDato = expresionRetorno.tipo
            else:   # si no, se lanza un error
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", f"Asignacion incorrecta, la variable con nombre '{self.nombreVar}' es de tipo [{variable.tipo}] y se le esta tratando de asignar un tipo [{consolaGlobal.relacionarTipos(expresionRetorno.tipo)}]", self.line, self.column, datetime.now()))                
                return

        # si todo esta bien, se actualiza la variable    
        ts.actualizarVariable(self.nombreVar, expresionRetorno.valor)
        ts.recorrerTablaSimbolos()