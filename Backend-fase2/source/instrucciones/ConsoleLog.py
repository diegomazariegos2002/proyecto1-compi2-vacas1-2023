
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
                        print(retorno.contenidoVector[0])
                        cadenaRetornoPrints += consola.genPrintC(91)  # [
                        cadenaRetornoExpresiones += retorno.codigoTraducido
                        for x in range(0, len(retorno.contenidoVector)):
                            if x== 0:
                                if retorno.contenidoVector[x].tipoVariable == TipoVariable.VECTOR:
                                    vecRetorno = self.agregarVectorConsolaC3D(retorno.contenidoVector[x])
                                    cadenaRetornoExpresiones += vecRetorno[0]
                                    cadenaRetornoPrints += vecRetorno[1]
                                else:
                                    if(retorno.contenidoVector[x].tipo == TipoDato.CADENA):
                                        t1 = consola.genNewTemp()
                                        t2 = consola.genNewTemp()

                                        l1 = consola.genNewEtq()
                                        l2 = consola.genNewEtq()
                                        cadenaRetornoPrints += consola.genAsignacion(t1, retorno.contenidoVector[x].valor)
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
                                        continue
                                    elif(retorno.contenidoVector[x].tipo == TipoDato.NUMERO):
                                        cadenaRetornoPrints += consola.genPrintF(retorno.contenidoVector[x].valor)
                                        continue
                                    elif(retorno.contenidoVector[x].tipo == TipoDato.BOOLEANO):
                                        l1 = consola.genNewEtq()
                                        l2 = consola.genNewEtq()
                                        cadenaRetornoPrints += consola.genIf(str(retorno.contenidoVector[x].valor)+"==1", consola.genGoto2(l1))
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
                                        continue
                                    elif(retorno.contenidoVector[x].tipo == TipoDato.NULL):
                                        cadenaRetornoPrints += consola.genPrintC(110)  # n
                                        cadenaRetornoPrints += consola.genPrintC(117)  # u
                                        cadenaRetornoPrints += consola.genPrintC(108)  # l
                                        cadenaRetornoPrints += consola.genPrintC(108)  # l
                                        continue
                            else:
                                cadenaRetornoPrints += consola.genPrintC(44)  # [
                                if retorno.contenidoVector[x].tipoVariable == TipoVariable.VECTOR:
                                    vecRetorno = self.agregarVectorConsolaC3D(retorno.contenidoVector[x])
                                    cadenaRetornoExpresiones += vecRetorno[0]
                                    cadenaRetornoPrints += vecRetorno[1]
                                else:
                                    if(retorno.contenidoVector[x].tipo == TipoDato.CADENA):
                                        t1 = consola.genNewTemp()
                                        t2 = consola.genNewTemp()

                                        l1 = consola.genNewEtq()
                                        l2 = consola.genNewEtq()
                                        cadenaRetornoPrints += consola.genAsignacion(t1, retorno.contenidoVector[x].valor)
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
                                        continue
                                    elif(retorno.contenidoVector[x].tipo == TipoDato.NUMERO):
                                        cadenaRetornoPrints += consola.genPrintF(retorno.contenidoVector[x].valor)
                                        continue
                                    elif(retorno.contenidoVector[x].tipo == TipoDato.BOOLEANO):
                                        l1 = consola.genNewEtq()
                                        l2 = consola.genNewEtq()
                                        cadenaRetornoPrints += consola.genIf(str(retorno.contenidoVector[x].valor)+"==1", consola.genGoto2(l1))
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
                                        continue
                                    elif(retorno.contenidoVector[x].tipo == TipoDato.NULL):
                                        cadenaRetornoPrints += consola.genPrintC(110)  # n
                                        cadenaRetornoPrints += consola.genPrintC(117)  # u
                                        cadenaRetornoPrints += consola.genPrintC(108)  # l
                                        cadenaRetornoPrints += consola.genPrintC(108)  # l
                                        continue
                                
                        cadenaRetornoPrints += consola.genPrintC(93)  # [
                            
                    cadenaRetornoExpresiones += consola.genPrintC(10)
            else:
                consola.set_Consola("Error en la ejecucion de la instruccion ConsoleLog, tipo no valido")
                return Excepcion()
        
        return (consola.genComment("console.log")+
                cadenaRetornoExpresiones + 
                cadenaRetornoPrints+
                consola.genPrintC(10))
        
    def agregarVectorConsolaC3D(self, vectorNuevo: RetornoTraduccion):
        consola = Consola()
        cadenaRetornoPrints = ""
        cadenaRetornoExpresiones = ""
        cadenaRetornoPrints += consola.genPrintC(91)  # [
        cadenaRetornoExpresiones += vectorNuevo.codigoTraducido
        for x in range(0, len(vectorNuevo.contenidoVector)):
            if x== 0:
                if vectorNuevo.contenidoVector[x].tipoVariable == TipoVariable.VECTOR:
                    vecRetorno = self.agregarVectorConsolaC3D(vectorNuevo.contenidoVector[x])
                    cadenaRetornoExpresiones += vecRetorno[0]
                    cadenaRetornoPrints += vecRetorno[1]
                else:
                    if(vectorNuevo.contenidoVector[x].tipo == TipoDato.CADENA):
                        t1 = consola.genNewTemp()
                        t2 = consola.genNewTemp()

                        l1 = consola.genNewEtq()
                        l2 = consola.genNewEtq()
                        cadenaRetornoPrints += consola.genAsignacion(t1, vectorNuevo.contenidoVector[x].valor)
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
                        continue
                    elif(vectorNuevo.contenidoVector[x].tipo == TipoDato.NUMERO):
                        print("VECTOR CONSOLA")
                        cadenaRetornoPrints += consola.genPrintF(vectorNuevo.contenidoVector[x].valor)
                        continue
                    elif(vectorNuevo.contenidoVector[x].tipo == TipoDato.BOOLEANO):
                        l1 = consola.genNewEtq()
                        l2 = consola.genNewEtq()
                        cadenaRetornoPrints += consola.genIf(str(vectorNuevo.contenidoVector[x].valor)+"==1", consola.genGoto2(l1))
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
                        continue
                    elif(vectorNuevo.contenidoVector[x].tipo == TipoDato.NULL):
                        cadenaRetornoPrints += consola.genPrintC(110)  # n
                        cadenaRetornoPrints += consola.genPrintC(117)  # u
                        cadenaRetornoPrints += consola.genPrintC(108)  # l
                        cadenaRetornoPrints += consola.genPrintC(108)  # l
                        continue
            else:
                cadenaRetornoPrints += consola.genPrintC(44)  # [
                if vectorNuevo.contenidoVector[x].tipoVariable == TipoVariable.VECTOR:
                    vecRetorno = self.agregarVectorConsolaC3D(vectorNuevo.contenidoVector[x])
                    cadenaRetornoExpresiones += vecRetorno[0]
                    cadenaRetornoPrints += vecRetorno[1]
                else:
                    if(vectorNuevo.contenidoVector[x].tipo == TipoDato.CADENA):
                        t1 = consola.genNewTemp()
                        t2 = consola.genNewTemp()

                        l1 = consola.genNewEtq()
                        l2 = consola.genNewEtq()
                        cadenaRetornoPrints += consola.genAsignacion(t1, vectorNuevo.contenidoVector[x].valor)
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
                        continue
                    elif(vectorNuevo.contenidoVector[x].tipo == TipoDato.NUMERO):
                        cadenaRetornoPrints += consola.genPrintF(vectorNuevo.contenidoVector[x].valor)
                        continue
                    elif(vectorNuevo.contenidoVector[x].tipo == TipoDato.BOOLEANO):
                        l1 = consola.genNewEtq()
                        l2 = consola.genNewEtq()
                        cadenaRetornoPrints += consola.genIf(str(vectorNuevo.contenidoVector[x].valor)+"==1", consola.genGoto2(l1))
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
                        continue
                    elif(vectorNuevo.contenidoVector[x].tipo == TipoDato.NULL):
                        cadenaRetornoPrints += consola.genPrintC(110)  # n
                        cadenaRetornoPrints += consola.genPrintC(117)  # u
                        cadenaRetornoPrints += consola.genPrintC(108)  # l
                        cadenaRetornoPrints += consola.genPrintC(108)  # l
                        continue
                
        cadenaRetornoPrints += consola.genPrintC(93)  # [
        return ([cadenaRetornoExpresiones, cadenaRetornoPrints])