
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, Tipo, TipoDato, TipoVariable, RetornoTraduccion
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.TablaSimbolos import TablaSimbolos
from source.simbolo.Simbolo import Simbolo, SimboloTraduccion
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
                return Retorno(0, Tipo.ERROR, TipoVariable.NORMAL)
            indices.append(round(indi.valor))


        if(variable == None):
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" no existe.", self.line, self.column, datetime.now()))
            return Retorno(0, Tipo.ERROR, TipoVariable.NORMAL)
        
        if variable.tipoVariable != TipoVariable.VECTOR:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "La variable a la que se quiere acceder no es un vector.", self.line, self.column, datetime.now()))
            return Retorno(0, Tipo.ERROR, TipoVariable.NORMAL)
        
        varVal = variable.valor
        
        for x in range(0, len(indices)):
            if x == len(indices)-1:
                if isinstance(varVal, Retorno):
                    if(indices[x] < len(varVal.valor)):
                        varVal = varVal.valor[indices[x]]
                    else:
                            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "No existe el indice al que se desea acceder en el vector.", self.line, self.column, datetime.now()))
                            return Retorno(0, Tipo.ERROR, TipoVariable.NORMAL)
                else:
                    if(indices[x] < len(varVal)):
                        varVal = varVal[indices[x]]
                    else:
                            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "No existe el indice al que se desea acceder en el vector.", self.line, self.column, datetime.now()))
                            return Retorno(0, Tipo.ERROR, TipoVariable.NORMAL)
            else:
                if  varVal[indices[x]].tipoVariable == TipoVariable.VECTOR:
                    varVal = varVal[indices[x]].valor
                else:
                    consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "No existe el indice al que se desea acceder en el vector.", self.line, self.column, datetime.now()))
                    return Retorno(0, Tipo.ERROR, TipoVariable.NORMAL)
        
        return Retorno(varVal.valor, varVal.tipo, varVal.tipoVariable)
    
    def traducir(self, ts:TablaSimbolos):
        consolaGlobal = Consola()
        variable : SimboloTraduccion = ts.buscar(self.id)
        cadena = ""
        indices = []
        i: Expresion = None
        for i in self.indices:
            indi:RetornoTraduccion = i.traducir(ts)
            if indi.tipo != TipoDato.NUMERO:
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "El indice para un vector debe ser numérico", self.line, self.column, datetime.now()))
                return RetornoTraduccion(valor=0,
                                 tipo=TipoDato.ERROR,
                                 tipoVariable=TipoVariable.NORMAL,
                                 codigoTraducido="")
            cadena += indi.codigoTraducido
            indices.append(indi.valor)


        if(variable == None):
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" no existe.", self.line, self.column, datetime.now()))
            return RetornoTraduccion(valor=0,
                                tipo=TipoDato.ERROR,
                                tipoVariable=TipoVariable.NORMAL,
                                codigoTraducido="")
        
        if variable.tipoVariable != TipoVariable.VECTOR:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "La variable a la que se quiere acceder no es un vector.", self.line, self.column, datetime.now()))
            return RetornoTraduccion(valor=0,
                                tipo=TipoDato.ERROR,
                                tipoVariable=TipoVariable.NORMAL,
                                codigoTraducido="")
        
        if len(indices) > variable.dimensiones:
            print("ACCESO VECTOR")
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
            return RetornoTraduccion(valor=0,
                                tipo=TipoDato.ERROR,
                                tipoVariable=TipoVariable.NORMAL,
                                codigoTraducido=cadena)
        
        cadP = ""
        valorInicio = variable.temporal
        
        valoresFinales = []
        cadenaFinal = ""
        tvalor = consolaGlobal.genNewTemp() # Genera nuevo tmp longitud
        tipoVar: TipoVariable = TipoVariable.NORMAL
        tbandera = consolaGlobal.genNewTemp() # Genera nuevo tmp longitud
        cadP += consolaGlobal.genAsignacion(tbandera, 0)
        ban = True
        contDim = 0
        print(len(indices))
        for i in range(0, variable.dimensiones):
            if ban == True:
                if i == variable.dimensiones - 1:
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
                        cadP += consolaGlobal.genAsignacion(tvalor,
                                                "HEAP[int({})]".format(tsumaTMP))
                        tipoVar = TipoVariable.NORMAL
                        ban = False
                        contDim = variable.dimensiones - len(indices)
                        cadP += consolaGlobal.genGoto(l2TMP) # sino ir al l2
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
                else:
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
                        cadP += consolaGlobal.genAsignacion(tvalor,
                                                "HEAP[int({})]".format(tsumaTMP))
                        tipoVar = TipoVariable.VECTOR
                        cadP += consolaGlobal.genGoto(l2TMP) # sino ir al l2
                        contDim = variable.dimensiones - len(indices)
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
        
        return RetornoTraduccion(valor=tvalor,
                                     tipo=variable.tipoDato,
                                     tipoVariable=tipoVar,
                                     codigoTraducido=cadena + consolaGlobal.genComment("ACCESO A VECTOR") + cadP,
                                     dimensiones=contDim)