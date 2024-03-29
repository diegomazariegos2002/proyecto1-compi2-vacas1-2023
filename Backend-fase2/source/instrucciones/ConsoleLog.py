
from source.abstracto.Retorno import Retorno, RetornoTraduccion, Tipo, TipoDato, TipoVariable
from source.consola_singleton.Consola import Consola
from source.abstracto.Expresion import Expresion
from source.abstracto.Instruccion import Instruccion
from source.errores.Excepcion import Excepcion
from source.simbolo.TablaSimbolos import TablaSimbolos


class ConsoleLog(Instruccion):

    def __init__(self, valor:list[Expresion], line: int, column: int):
        super().__init__(line, column)
        self.valor : list[Expresion] = valor

    def ejecutar(self, ts: TablaSimbolos):
        consola = Consola()
        for expresion in self.valor:
            retorno:Retorno = expresion.ejecutar(ts)
            if(retorno.tipo != TipoDato.ERROR):
                if(retorno != None):
                    if retorno.tipoVariable == TipoVariable.NORMAL:
                        if(retorno.tipo == TipoDato.CADENA):
                            consola.set_Consola(retorno.valor)
                            continue
                        if(retorno.tipo == TipoDato.NUMERO):
                            consola.set_Consola(str(retorno.valor))
                            continue
                        if(retorno.tipo == TipoDato.BOOLEANO):
                            if(retorno.valor == True):
                                consola.set_Consola("true")
                            elif(retorno.valor == False):
                                consola.set_Consola("false")
                            continue
                        if(retorno.tipo == TipoDato.NULL):
                            consola.set_Consola("null")
                            continue
                        continue
                    elif retorno.tipoVariable == TipoVariable.VECTOR:
                        consola.set_Consola("[")
                        for x in range(0, len(retorno.valor)):
                            if x== 0:
                                if retorno.valor[x].tipoVariable == TipoVariable.VECTOR:
                                    self.agregarVectorConsola(retorno.valor[x])
                                else:
                                    if(retorno.valor[x].tipo == TipoDato.CADENA):
                                        consola.set_Consola(retorno.valor[x].valor)
                                    elif(retorno.valor[x].tipo == TipoDato.NUMERO):
                                        consola.set_Consola(str(retorno.valor[x].valor))
                                    elif(retorno.valor[x].tipo == TipoDato.BOOLEANO):
                                        if(retorno.valor[x].valor == True):
                                            consola.set_Consola("true")
                                        elif(retorno.valor[x].valor == False):
                                            consola.set_Consola("false")
                                    elif(retorno.valor[x].tipo == TipoDato.NULL):
                                        consola.set_Consola("null")
                            else:
                                consola.set_Consola(", ")
                                if retorno.valor[x].tipoVariable == TipoVariable.VECTOR:
                                    self.agregarVectorConsola(retorno.valor[x])
                                else:
                                    if(retorno.valor[x].tipo == TipoDato.CADENA):
                                        consola.set_Consola(retorno.valor[x].valor)
                                    elif(retorno.valor[x].tipo == TipoDato.NUMERO):
                                        consola.set_Consola(str(retorno.valor[x].valor))
                                    elif(retorno.valor[x].tipo == TipoDato.BOOLEANO):
                                        if(retorno.valor[x].valor == True):
                                            consola.set_Consola("true")
                                        elif(retorno.valor[x].valor == False):
                                            consola.set_Consola("false")
                                    elif(retorno.valor[x].tipo == TipoDato.NULL):
                                        consola.set_Consola("null")
                                
                        consola.set_Consola("]")
                continue
            else:
                consola.set_Consola("Error en la ejecucion de la instruccion ConsoleLog, tipo no valido")
                return Excepcion()
        consola.set_Consola("\n")
        return
    
    def graficarAst(self):
        consola = Consola()
        nombreNodo = f"instruccion_{self.line}_{self.column}_{str(id(self))}_"
        consola.set_AstGrafico(f"{nombreNodo}[label=\"\\<Instruccion\\>\\nconsole.log\"];\n")
        if self.valor != None or self.valor != []:        
            cont = 0
            nombreNodoAnterior = ""
            for expresion in self.valor:
                if cont == 0:
                    nombreNodoAnterior = expresion.graficarAst()
                    consola.set_AstGrafico(f"{nombreNodo} -> {nombreNodoAnterior};\n")
                else: 
                    nombreNodoNuevo = expresion.graficarAst()
                    consola.set_AstGrafico(f"{nombreNodoAnterior}-> {nombreNodoNuevo};\n")
                    nombreNodoAnterior = nombreNodoNuevo
                cont+=1 
        return nombreNodo
                 
    def agregarVectorConsola(self, vectorNuevo: Retorno):
        consola = Consola()
        consola.set_Consola("[")
        for x in range(0, len(vectorNuevo.valor)):
            if x== 0:
                if vectorNuevo.valor[x].tipoVariable == TipoVariable.VECTOR:
                    self.agregarVectorConsola(vectorNuevo.valor[x])
                else:
                    if(vectorNuevo.valor[x].tipo == TipoDato.CADENA):
                        consola.set_Consola(vectorNuevo.valor[x].valor)
                    elif(vectorNuevo.valor[x].tipo == TipoDato.NUMERO):
                        consola.set_Consola(str(vectorNuevo.valor[x].valor))
                    elif(vectorNuevo.valor[x].tipo == TipoDato.BOOLEANO):
                        if(vectorNuevo.valor[x].valor == True):
                            consola.set_Consola("true")
                        elif(vectorNuevo.valor[x].valor == False):
                            consola.set_Consola("false")
                    elif(vectorNuevo.valor[x].tipo == TipoDato.NULL):
                        consola.set_Consola("null")
            else:
                consola.set_Consola(", ")
                if vectorNuevo.valor[x].tipoVariable == TipoVariable.VECTOR:
                    self.agregarVectorConsola(vectorNuevo.valor[x])
                else:
                    if(vectorNuevo.valor[x].tipo == TipoDato.CADENA):
                        consola.set_Consola(vectorNuevo.valor[x].valor)
                    elif(vectorNuevo.valor[x].tipo == TipoDato.NUMERO):
                        consola.set_Consola(str(vectorNuevo.valor[x].valor))
                    elif(vectorNuevo.valor[x].tipo == TipoDato.BOOLEANO):
                        if(vectorNuevo.valor[x].valor == True):
                            consola.set_Consola("true")
                        elif(vectorNuevo.valor[x].valor == False):
                            consola.set_Consola("false")
                    elif(vectorNuevo.valor[x].tipo == TipoDato.NULL):
                        consola.set_Consola("null")
                
        consola.set_Consola("]")
        
    def traducir(self, ts: TablaSimbolos):
        consola: Consola = Consola()
        cadenaRetornoPrints = ""
        cadenaRetornoExpresiones = ""
        for expresion in self.valor:
            retorno:RetornoTraduccion = expresion.traducir(ts)
            if(retorno.tipo != TipoDato.ERROR):
                if(retorno != None):
                    if retorno.tipoVariable == TipoVariable.NORMAL:
                        if(retorno.tipo == TipoDato.CADENA):
                            t1 = consola.genNewTemp()
                            t2 = consola.genNewTemp()

                            l1 = consola.genNewEtq()
                            l2 = consola.genNewEtq()
                            cadenaRetornoPrints += consola.genAsignacion(t1, retorno.valor)
                            cadenaRetornoPrints += "{}:\n".format(l1)
                            cadenaRetornoPrints += consola.genAsignacion(t2,
                                                        "HEAP[int({})]".format(t1))
                            cadenaRetornoPrints += consola.genIf("{} == -1".format(t2),
                                                consola.genGoto2(l2))
                            cadenaRetornoPrints += consola.genPrintC(
                                "{}".format(t2))
                            cadenaRetornoPrints += consola.genAsignacion(t1, "{} + 1".format(t1))
                            cadenaRetornoPrints += consola.genGoto(l1)
                            cadenaRetornoPrints += "{}:\n".format(l2)
                            cadenaRetornoExpresiones += retorno.codigoTraducido
                            continue
                        elif(retorno.tipo == TipoDato.NUMERO):
                            cadenaRetornoPrints += consola.genPrintF(retorno.valor)
                            cadenaRetornoExpresiones += retorno.codigoTraducido
                            continue
                        elif(retorno.tipo == TipoDato.BOOLEANO):
                            l1 = consola.genNewEtq()
                            l2 = consola.genNewEtq()
                            cadenaRetornoPrints += consola.genIf(str(retorno.valor)+"==1", consola.genGoto2(l1))
                            cadenaRetornoPrints += consola.genPrintC(102)  # f
                            cadenaRetornoPrints += consola.genPrintC(97)   # a
                            cadenaRetornoPrints += consola.genPrintC(108)  # l
                            cadenaRetornoPrints += consola.genPrintC(115)  # s
                            cadenaRetornoPrints += consola.genPrintC(101)  # e
                            cadenaRetornoPrints += consola.genGoto(l2)
                            cadenaRetornoPrints += "{}:\n".format(l1)
                            cadenaRetornoPrints += consola.genPrintC(116)  # t
                            cadenaRetornoPrints += consola.genPrintC(114)  # r
                            cadenaRetornoPrints += consola.genPrintC(117)  # u
                            cadenaRetornoPrints += consola.genPrintC(101)  # e
                            cadenaRetornoPrints += "{}:\n".format(l2)
                            cadenaRetornoExpresiones += retorno.codigoTraducido
                            continue
                        elif(retorno.tipo == TipoDato.NULL):
                            cadenaRetornoPrints += consola.genPrintC(110)  # n
                            cadenaRetornoPrints += consola.genPrintC(117)  # u
                            cadenaRetornoPrints += consola.genPrintC(108)  # l
                            cadenaRetornoPrints += consola.genPrintC(108)  # l
                            cadenaRetornoExpresiones += retorno.codigoTraducido
                            continue
                        else:
                            consola.set_Consola("Error en la ejecucion de la instruccion ConsoleLog, tipo no valido")
                            return Excepcion()
                    elif retorno.tipoVariable == TipoVariable.VECTOR:
                        cadP = ""
                        valorInicio = retorno.valor
                        
                        valoresFinales = []
                        cadenaFinal = ""
                        
                        cadenaRetornoExpresiones += retorno.codigoTraducido
                        for i in range(0, retorno.dimensiones):
                            if i == retorno.dimensiones - 1:
                                tlenTMP = consola.genNewTemp() # Genera nuevo tmp longitud
                                tinicioTMP = consola.genNewTemp() # Nuevo temporal de inicio
                                tauxTMP = consola.genNewTemp() # Genera nuevo tmp auxiliar
                                tpivoteTMP = consola.genNewTemp() # Genera nuevo tmp pivote
                                tsumaTMP = consola.genNewTemp() # Genera nuevo tmp sumar
                                l0TMP = consola.genNewEtq() # Nuevo label 
                                l1TMP = consola.genNewEtq() # Nuevo label
                                l2TMP = consola.genNewEtq() # Nuevo label
                                cadP += consola.genPrintC("91") # Imprime [
                                cadP += consola.genPrintC("32") # Imprime espacio
                                cadP += consola.genAsignacion(tlenTMP,
                                                            "HEAP[int({})]".format(valorInicio)) # Asigna longitud
                                cadP += consola.genAsignacion(tinicioTMP,
                                                            "{} + {}".format(valorInicio, 1)) # Asigna longitud
                                cadP += consola.genAsignacion(tauxTMP, 0)
                                cadP += "{}:\n".format(l0TMP) # Se inicia label 0

                                cadP += consola.genIf("{} > {}".format(tlenTMP,
                                                    tauxTMP), consola.genGoto2(l1TMP)) # If el auxiliar es menos que longitud ir a l1
                                cadP += consola.genGoto(l2TMP) # sino ir al l2
                                cadP += "{}:\n".format(l1TMP) # definicion de label 1
                                cadP += consola.genAsignacion(tsumaTMP,
                                                            "{} + {}".format(tinicioTMP, tauxTMP)) # 
                                cadP += consola.genAsignacion(tpivoteTMP,
                                                            "HEAP[int ({})]".format(tsumaTMP))
                                valorInicio = tpivoteTMP
                                
                                if(retorno.tipo == TipoDato.CADENA):
                                    t1 = consola.genNewTemp()
                                    t2 = consola.genNewTemp()

                                    l1 = consola.genNewEtq()
                                    l2 = consola.genNewEtq()
                                    cadP += consola.genAsignacion(t1, valorInicio)
                                    cadP += "{}:\n".format(l1)
                                    cadP += consola.genAsignacion(t2,
                                                                "HEAP[int({})]".format(t1))
                                    cadP += consola.genIf("{} == -1".format(t2),
                                                        consola.genGoto2(l2))
                                    cadP += consola.genPrintC(
                                        "{}".format(t2))
                                    cadP += consola.genAsignacion(t1, "{} + 1".format(t1))
                                    cadP += consola.genGoto(l1)
                                    cadP += "{}:\n".format(l2)
                                elif(retorno.tipo == TipoDato.NUMERO):
                                    cadP += consola.genPrintF(valorInicio)
                                elif(retorno.tipo == TipoDato.BOOLEANO):
                                    l1 = consola.genNewEtq()
                                    l2 = consola.genNewEtq()
                                    cadP += consola.genIf(str(valorInicio)+"==1", consola.genGoto2(l1))
                                    cadP += consola.genPrintC(102)  # f
                                    cadP += consola.genPrintC(97)   # a
                                    cadP += consola.genPrintC(108)  # l
                                    cadP += consola.genPrintC(115)  # s
                                    cadP += consola.genPrintC(101)  # e
                                    cadP += consola.genGoto(l2)
                                    cadP += "{}:\n".format(l1)
                                    cadP += consola.genPrintC(116)  # t
                                    cadP += consola.genPrintC(114)  # r
                                    cadP += consola.genPrintC(117)  # u
                                    cadP += consola.genPrintC(101)  # e
                                    cadP += "{}:\n".format(l2)
                                
                                cadenaFinal += consola.genAsignacion(tauxTMP,
                                                    "{} + 1".format(tauxTMP))
                                cadenaFinal += consola.genPrintC("32")
                                cadenaFinal += consola.genGoto(l0TMP)
                                cadenaFinal += "{}:\n".format(l2TMP)

                                cadenaFinal += consola.genPrintC("93")
                                valoresFinales.append(cadenaFinal)
                                cadenaFinal = ""
                            else:
                                tlenTMP = consola.genNewTemp() # Genera nuevo tmp longitud
                                tinicioTMP = consola.genNewTemp() # Nuevo temporal de inicio
                                tauxTMP = consola.genNewTemp() # Genera nuevo tmp auxiliar
                                tpivoteTMP = consola.genNewTemp() # Genera nuevo tmp pivote
                                tsumaTMP = consola.genNewTemp() # Genera nuevo tmp sumar
                                l0TMP = consola.genNewEtq() # Nuevo label 
                                l1TMP = consola.genNewEtq() # Nuevo label
                                l2TMP = consola.genNewEtq() # Nuevo label
                                cadP += consola.genPrintC("91") # Imprime [
                                cadP += consola.genPrintC("32") # Imprime espacio
                                cadP += consola.genAsignacion(tlenTMP,
                                                            "HEAP[int({})]".format(valorInicio)) # Asigna longitud
                                cadP += consola.genAsignacion(tinicioTMP,
                                                            "{} + {}".format(valorInicio, 1)) # Asigna longitud
                                cadP += consola.genAsignacion(tauxTMP, 0)
                                cadP += "{}:\n".format(l0TMP) # Se inicia label 0

                                cadP += consola.genIf("{} > {}".format(tlenTMP,
                                                    tauxTMP), consola.genGoto2(l1TMP)) # If el auxiliar es menos que longitud ir a l1
                                cadP += consola.genGoto(l2TMP) # sino ir al l2
                                cadP += "{}:\n".format(l1TMP) # definicion de label 1
                                cadP += consola.genAsignacion(tsumaTMP,
                                                            "{} + {}".format(tinicioTMP, tauxTMP)) # 
                                cadP += consola.genAsignacion(tpivoteTMP,
                                                            "HEAP[int({})]".format(tsumaTMP))
                                valorInicio = tpivoteTMP
                                
                                cadenaFinal += consola.genAsignacion(tauxTMP,
                                                    "{} + 1".format(tauxTMP))
                                cadenaFinal += consola.genPrintC("32")
                                cadenaFinal += consola.genGoto(l0TMP)
                                cadenaFinal += "{}:\n".format(l2TMP)

                                cadenaFinal += consola.genPrintC("93")
                                valoresFinales.append(cadenaFinal)
                                cadenaFinal = ""
                        
                        valoresFinales.reverse()
                        for i in valoresFinales:
                            cadenaFinal += i
                            
                        cadenaRetornoPrints += cadP + cadenaFinal
                            
                    cadenaRetornoPrints += consola.genPrintC(10)
            else:
                consola.set_Consola("Error en la ejecucion de la instruccion ConsoleLog, tipo no valido")
                return Excepcion()
        
        return (consola.genComment("console.log")+
                cadenaRetornoExpresiones + 
                cadenaRetornoPrints+
                consola.genPrintC(10))
        