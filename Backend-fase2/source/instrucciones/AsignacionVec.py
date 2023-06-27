from datetime import datetime
from source.abstracto.Expresion import Expresion
from source.abstracto.Instruccion import Instruccion
from source.abstracto.Retorno import Retorno, Tipo, TipoVariable, TipoDato, VectorAux, RetornoTraduccion
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.Simbolo import Simbolo, SimboloTraduccion
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
    
    def traducir(self, ts: TablaSimbolos):
        consolaGlobal = Consola()
        expresionRetorno : RetornoTraduccion = self.expresionAsignar.traducir(ts)
        indices = []
        i: Expresion = None
        cadena = ""
        for i in self.indices:
            indi:RetornoTraduccion = i.traducir(ts)
            if indi.tipo != TipoDato.NUMERO:
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "El indice para un vector debe ser numérico", self.line, self.column, datetime.now()))
                return
            cadena += indi.codigoTraducido
            indices.append(indi.valor)

        variable : SimboloTraduccion = ts.buscar(self.nombreVar)
        # validar que todo este bien antes de actualizar la variable
        if variable is None:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la asignacion, variable sin declarar", self.line, self.column, datetime.now()))
            return Excepcion()

        if variable.tipoVariable != TipoVariable.VECTOR:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "La variable a la que se quiere acceder no es un vector.", self.line, self.column, datetime.now()))
            return Excepcion()
        
        if len(indices) > variable.dimensiones:
            print("ASIGNACION VECTOR")
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "No se puede accesar a los indices del vector.", self.line, self.column, datetime.now()))
            cadena = consolaGlobal.genPrintC(66)
            cadena += consolaGlobal.genPrintC(111)
            cadena += consolaGlobal.genPrintC(117)
            cadena += consolaGlobal.genPrintC(110)
            cadena += consolaGlobal.genPrintC(100)
            cadena += consolaGlobal.genPrintC(115)
            cadena += consolaGlobal.genPrintC(32)
            cadena += consolaGlobal.genPrintC(69)
            cadena += consolaGlobal.genPrintC(114)
            cadena += consolaGlobal.genPrintC(114)
            cadena += consolaGlobal.genPrintC(111)
            cadena += consolaGlobal.genPrintC(114)
            return cadena
        
        cadP = ""
        valorInicio = variable.temporal
        
        valoresFinales = []
        cadenaFinal = ""
        tbandera = consolaGlobal.genNewTemp() # Genera nuevo tmp longitud
        cadP += consolaGlobal.genAsignacion(tbandera, 0)
        ban = True
        for i in range(0, variable.dimensiones):
            if ban == True:
                tlenTMP = consolaGlobal.genNewTemp() # Genera nuevo tmp longitud
                tinicioTMP = consolaGlobal.genNewTemp() # Nuevo temporal de inicio
                tauxTMP = consolaGlobal.genNewTemp() # Genera nuevo tmp auxiliar
                tpivoteTMP = consolaGlobal.genNewTemp() # Genera nuevo tmp pivote
                tsumaTMP = consolaGlobal.genNewTemp() # Genera nuevo tmp sumar
                l0TMP = consolaGlobal.genNewEtq() # Nuevo label 
                l1TMP = consolaGlobal.genNewEtq() # Nuevo label
                l2TMP = consolaGlobal.genNewEtq() # Nuevo label
                l3TMP = consolaGlobal.genNewEtq() # Nuevo label
                l4TMP = consolaGlobal.genNewEtq() # Nuevo label
                cadP += consolaGlobal.genAsignacion(tlenTMP,
                                            "HEAP[int({})]".format(valorInicio)) # Asigna longitud
                cadP += consolaGlobal.genAsignacion(tinicioTMP,
                                            "{} + {}".format(valorInicio, 1)) # Asigna longitud
                cadP += consolaGlobal.genAsignacion(tauxTMP, 0)
                cadP += "{}:\n".format(l0TMP) # Se inicia label 0

                cadP += consolaGlobal.genIf("{} > {}".format(tlenTMP,
                                    tauxTMP), consolaGlobal.genGoto2(l1TMP)) # If el auxiliar es menos que longitud ir a l1
                cadP += consolaGlobal.genGoto(l2TMP) # sino ir al l2
                cadP += "{}:\n".format(l1TMP) # definicion de label 1
                cadP += consolaGlobal.genIf("{} == {}".format(tauxTMP,
                                indices[i]), consolaGlobal.genGoto2(l3TMP))
                cadP += consolaGlobal.genGoto(l4TMP) # sino ir al l2
                if i == len(indices)-1:
                    cadP += "{}:\n".format(l3TMP) # Se inicia label 3 
                    cadP += consolaGlobal.genAsignacion(tsumaTMP,
                                            "{} + {}".format(tinicioTMP, tauxTMP)) # 
                    cadP += consolaGlobal.genAsignacion(tbandera, 1)
                    cadP += consolaGlobal.genAsignacion("HEAP[int({})]".format(tsumaTMP),
                                            expresionRetorno.valor)
                    cadP += consolaGlobal.genGoto(l2TMP) # sino ir al l2
                    ban = False
                else:
                    cadP += "{}:\n".format(l3TMP)
                    cadP += consolaGlobal.genAsignacion(tsumaTMP,
                                            "{} + {}".format(tinicioTMP, tauxTMP))  
                    cadP += consolaGlobal.genAsignacion(tpivoteTMP,
                                            "HEAP[int({})]".format(tsumaTMP))
                cadenaFinal += "{}:\n".format(l4TMP) # Se inicia label 4   
                cadenaFinal += consolaGlobal.genAsignacion(tsumaTMP,
                                            "{} + {}".format(tinicioTMP, tauxTMP))  
                cadenaFinal += consolaGlobal.genAsignacion(tpivoteTMP,
                                            "HEAP[int({})]".format(tsumaTMP))
                valorInicio = tpivoteTMP
                    
                cadenaFinal += consolaGlobal.genAsignacion(tauxTMP,
                                    "{} + 1".format(tauxTMP))
                cadenaFinal += consolaGlobal.genGoto(l0TMP)
                cadenaFinal += "{}:\n".format(l2TMP)
                valoresFinales.append(cadenaFinal)
                cadenaFinal = ""
        
        valoresFinales.reverse()
        for i in valoresFinales:
            cadenaFinal += i
        
        cadP += cadenaFinal
        
        label1 = consolaGlobal.genNewEtq() # Nuevo label
        label2 = consolaGlobal.genNewEtq() # Nuevo label
        cadP += consolaGlobal.genIf("{} == {}".format(tbandera,
                            0), consolaGlobal.genGoto2(label1))
        cadP += consolaGlobal.genGoto(label2)
        cadP += "{}:\n".format(label1) # Se inicia label 0
        cadP += consolaGlobal.genPrintC(66)
        cadP += consolaGlobal.genPrintC(111)
        cadP += consolaGlobal.genPrintC(117)
        cadP += consolaGlobal.genPrintC(110)
        cadP += consolaGlobal.genPrintC(100)
        cadP += consolaGlobal.genPrintC(115)
        cadP += consolaGlobal.genPrintC(32)
        cadP += consolaGlobal.genPrintC(69)
        cadP += consolaGlobal.genPrintC(114)
        cadP += consolaGlobal.genPrintC(114)
        cadP += consolaGlobal.genPrintC(111)
        cadP += consolaGlobal.genPrintC(114)
        cadP += "{}:\n".format(label2)
        return cadena + consolaGlobal.genComment("ASIGNACION EN VECTOR") + cadP
        