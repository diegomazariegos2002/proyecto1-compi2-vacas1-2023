
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, Tipo, TipoDato, TipoVariable
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.TablaSimbolos import TablaSimbolos
from datetime import datetime

class AccesoVector(Expresion):
    def __init__(self, id, indices, line: int, column: int):
        super().__init__(line, column)
        self.id = id
        self.indices = indices
    
    def ejecutar(self, ts: TablaSimbolos) -> Retorno:
        consolaGlobal = Consola()
        variable = ts.buscar(self.id)
        
        indices = []
        i: Expresion = None
        for i in self.indices:
            indi:Retorno = i.ejecutar(ts)
            if indi.tipo != TipoDato.NUMERO:
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "El indice para un vector debe ser numérico", self.line, self.column, datetime.now()))
                return
            indices.append(round(indi.valor))


        if(variable == None):
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" no existe.", self.line, self.column, datetime.now()))
            return Retorno(0, Tipo.ERROR)
        
        if variable.tipoVariable != TipoVariable.VECTOR:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "La variable a la que se quiere acceder no es un vector.", self.line, self.column, datetime.now()))
            return
        
        varVal = variable.valor
        
        for x in range(0, len(indices)):
            if x == len(indices)-1:
                if isinstance(varVal, Retorno):
                    if(indices[x] < len(varVal.valor)):
                        varVal = varVal.valor[indices[x]]
                    else:
                            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "No existe el indice al que se desea acceder en el vector.", self.line, self.column, datetime.now()))
                            return
                else:
                    if(indices[x] < len(varVal)):
                        varVal = varVal[indices[x]]
                    else:
                            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "No existe el indice al que se desea acceder en el vector.", self.line, self.column, datetime.now()))
                            return 
            else:
                print("------------------------")
                print(varVal)
                if  varVal[indices[x]].tipoVariable == TipoVariable.VECTOR:
                    varVal = varVal[indices[x]].valor
                else:
                    consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "No existe el indice al que se desea acceder en el vector.", self.line, self.column, datetime.now()))
                    return
        
        return Retorno(varVal.valor, varVal.tipo, varVal.tipoVariable)