from datetime import datetime
from source.abstracto.Expresion import Expresion
from source.abstracto.Instruccion import Instruccion
from source.abstracto.Retorno import Retorno, Tipo, TipoVariable, TipoDato, VectorAux
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
            if indi.tipo != TipoDato.NUMERO:
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "El indice para un vector debe ser numérico", self.line, self.column, datetime.now()))
                return
            indices.append(round(indi.valor))

        variable : Simbolo = ts.buscar(self.nombreVar)
        # validar que todo este bien antes de actualizar la variable
        if variable is None:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la asignacion, variable sin declarar", self.line, self.column, datetime.now()))
            return

        if variable.tipoVariable != TipoVariable.VECTOR:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "La variable a la que se quiere acceder no es un vector.", self.line, self.column, datetime.now()))
            return

        varVal = variable.valor
        vectorAux = []

        for x in range(0, len(indices)):
            if x == len(indices)-1:
                if isinstance(varVal, Retorno):
                    if(indices[x] < len(varVal.valor)):
                        if  varVal.valor[indices[x]].tipo == expresionRetorno.tipo or varVal.valor.tipo == TipoDato.ANY:
                                varVal.valor[indices[x]] = expresionRetorno
                                vectorAux.append(VectorAux(varVal, indices[x]))
                            
                        else:
                            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Los tipo de datos de las variables no coinciden.", self.line, self.column, datetime.now()))
                            return Excepcion()
                    else:
                            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "No existe el indice al que se desea acceder en el vector.", self.line, self.column, datetime.now()))
                            return Excepcion()
                else:
                    if(indices[x] < len(varVal)):
                        if  varVal[indices[x]].tipo == expresionRetorno.tipo or varVal.tipo == TipoDato.ANY:
                                varVal[indices[x]] = expresionRetorno
                                vectorAux.append(VectorAux(varVal, indices[x]))
                            
                        else:
                            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Los tipo de datos de las variables no coinciden.", self.line, self.column, datetime.now()))
                            return Excepcion()
                    else:
                            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "No existe el indice al que se desea acceder en el vector.", self.line, self.column, datetime.now()))
                            return Excepcion()
            else:
                if  varVal[indices[x]].tipoVariable == TipoVariable.VECTOR:
                    vectorAux.append(VectorAux(varVal, indices[x]))
                    varVal = varVal[indices[x]].valor
                else:
                    consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "No existe el indice al que se desea acceder en el vector.", self.line, self.column, datetime.now()))
                    return Excepcion()

        # si todo esta bien, se actualiza la variable    
        ts.actualizarVariable(self.nombreVar, vectorAux[0].vectortmp)