from datetime import datetime
from typing import Union
from source.abstracto.Retorno import Retorno, RetornoTraduccion, TipoDato, TipoVariable
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.abstracto.Expresion import Expresion
from source.abstracto.Instruccion import Instruccion
from source.instrucciones.sentencias_de_transferencia.Break import Break
from source.instrucciones.sentencias_de_transferencia.Continue import Continue
from source.instrucciones.sentencias_de_transferencia.Return import Return
from source.simbolo.TablaSimbolos import TablaSimbolos
from source.simbolo.Simbolo import Simbolo, TiposSimbolos


class If(Instruccion):

    def __init__(self, condicion:Expresion, insEntraIf:list[Instruccion], insEntraOpcionales:Union[list[Instruccion],Instruccion], line: int, column: int):
        super().__init__(line, column)
        self.condicion : Expresion = condicion
        self.insEntraIf : list[Instruccion] = insEntraIf
        self.insEntraOpcionales : list[Instruccion] = insEntraOpcionales
        # Fase 2
        self.retornoLlamada : RetornoTraduccion = None


    def ejecutar(self, ts: TablaSimbolos):
        """
        IF al ejecutar va a devolver un valor (return, break, continue)
        """
        consola = Consola()
        retornoExpresion:Retorno = self.condicion.ejecutar(ts)
        
        if retornoExpresion.tipo != TipoDato.BOOLEANO:
            # ERROR
            consola.set_Excepcion(Excepcion("Error Semantico", "Error la condicion en el if no es de tipo boolean", self.line, self.column, datetime.now()))
            # nota: no retorna nada entonces cuidado con los ciclos infinitos
            return Excepcion()

        # Si solo viene el if
        if self.insEntraOpcionales == None:
            newEnviroment = TablaSimbolos(ts, "IF-")
            if retornoExpresion.valor == True:
                for instruccion in self.insEntraIf:
                    resultIns:Instruccion = instruccion.ejecutar(newEnviroment)
                    # En algunos casos hay instrucciones que si retorna algo
                    if resultIns != None:
                        # Verificar si lo que devuelve son returns, continues, breaks.
                        if isinstance(resultIns, Excepcion):
                            return Excepcion()
                        if isinstance(resultIns, Return):
                            return resultIns
                        if isinstance(resultIns, Break):
                            return resultIns
                        if isinstance(resultIns, Continue):
                            return resultIns
        # si if viene con otra condición (else if, else)
        else:
            newEnviroment = TablaSimbolos(ts, "IF-")
            if retornoExpresion.valor == True:
                for instruccion in self.insEntraIf:
                    resultIns:Instruccion = instruccion.ejecutar(newEnviroment)
                    # En algunos casos hay instrucciones que si retorna algo
                    if resultIns != None:
                        # Verificar si lo que devuelve son returns, continues, breaks.
                        if isinstance(resultIns, Excepcion):
                            return Excepcion()
                        if isinstance(resultIns, Return):
                            return resultIns
                        if isinstance(resultIns, Break):
                            return resultIns
                        if isinstance(resultIns, Continue):
                            return resultIns
            else:
                # como no se cumplio el if, se ejecuta el else si hay
                # y si es un else if se ejecuta el else if
                # si insEntraOpcionales estamos hablando de un ELSE
                if isinstance(self.insEntraOpcionales, list):
                    newEnviroment2 = TablaSimbolos(ts, "ELSE-")
                    for instruccion in self.insEntraOpcionales:
                        resultIns:Instruccion = instruccion.ejecutar(newEnviroment2)
                        # En algunos casos hay instrucciones que si retorna algo
                        if resultIns != None:
                            # Verificar si lo que devuelve son returns, continues, breaks.
                            if isinstance(resultIns, Excepcion):
                                return Excepcion()
                            if isinstance(resultIns, Return):
                                return resultIns
                            if isinstance(resultIns, Break):
                                return resultIns
                            if isinstance(resultIns, Continue):
                                return resultIns
                # ELSE IF
                else:
                    newEnviroment2 = TablaSimbolos(ts, "ELSE IF-")
                    resultIns:Instruccion = self.insEntraOpcionales.ejecutar(newEnviroment2)
                    # En algunos casos hay instrucciones que si retorna algo
                    if resultIns != None:
                        # Verificar si lo que devuelve son returns, continues, breaks.
                        if isinstance(resultIns, Excepcion):
                            return Excepcion()
                        if isinstance(resultIns, Return):
                            return resultIns
                        if isinstance(resultIns, Break):
                            return resultIns
                        if isinstance(resultIns, Continue):
                            return resultIns
        return

    def graficarAst(self):
        consola = Consola()
        nombreNodo = f"instruccion_{self.line}_{self.column}_{str(id(self))}_"
        consola.set_AstGrafico(f"{nombreNodo}[label=\"\\<Instruccion\\>\\nIf\"];\n")
        nombreNodoCondicion = f"instruccion_{self.line}_{self.column}_{str(id(self))}_condicion"
        consola.set_AstGrafico(f"{nombreNodoCondicion}[label=\"\\<Instruccion\\>\\nCondicion\"];\n")
        nombreNodoBlkIns = f"instruccion_{self.line}_{self.column}_{str(id(self))}_blkInsIf"
        consola.set_AstGrafico(f"{nombreNodoBlkIns}[label=\"\\<Bloque\\>\\nInstrucciones If\"];\n")
        consola.set_AstGrafico(f"{nombreNodo}->{nombreNodoCondicion};\n")
        consola.set_AstGrafico(f"{nombreNodo}->{nombreNodoBlkIns};\n")
        consola.set_AstGrafico(f"{nombreNodoCondicion}->{self.condicion.graficarAst()};\n")
        cont = 0
        nombreNodoAnterior = ""

        for instruccion in self.insEntraIf:
            try:
                if cont == 0:
                    nombreNodoAnterior = instruccion.graficarAst()
                    consola.set_AstGrafico(f"{nombreNodoBlkIns}->{nombreNodoAnterior};\n")
                else:
                    nombreNodoNuevo = instruccion.graficarAst()
                    consola.set_AstGrafico(f"{nombreNodoAnterior}->{nombreNodoNuevo};\n")
                    nombreNodoAnterior = nombreNodoNuevo
                    
            except Exception as error:
                print("soy un error en el if ast." + error)
            cont += 1
        
        if self.insEntraOpcionales != None:
            #ELSE
            if isinstance(self.insEntraOpcionales, list):
                nombreNodoElse = f"instruccion_{self.line}_{self.column}_{str(id(self))}_else"
                consola.set_AstGrafico(f"{nombreNodoElse}[label=\"\\<Instruccion\\>\\nElse\"];\n")
                consola.set_AstGrafico(f"{nombreNodo}->{nombreNodoElse};\n")
                cont = 0
                nombreNodoAnterior = ""

                for instruccion in self.insEntraOpcionales:
                    try:
                        if cont == 0:
                            nombreNodoAnterior = instruccion.graficarAst()
                            consola.set_AstGrafico(f"{nombreNodoElse}->{nombreNodoAnterior};\n")
                        else:
                            nombreNodoNuevo = instruccion.graficarAst()
                            consola.set_AstGrafico(f"{nombreNodoAnterior}->{nombreNodoNuevo};\n")
                            nombreNodoAnterior = nombreNodoNuevo
                            
                    except Exception as error:
                        print("soy un error en el else ast." + error)
                    cont += 1
            
            #ELSE IF
            else:
                consola.set_AstGrafico(f"{nombreNodo}->{self.insEntraOpcionales.graficarAst()};\n")
                    
        return nombreNodo
        
    def traducir(self, ts: TablaSimbolos):
        consola: Consola = Consola()
        cadenaRetorno = ""
        retornoExpresion:RetornoTraduccion = self.condicion.traducir(ts)
        
        if retornoExpresion.tipo != TipoDato.BOOLEANO:
            # ERROR
            consola.set_Excepcion(Excepcion("Error Semantico", "Error la condicion en el if no es de tipo boolean", self.line, self.column, datetime.now()))
            # nota: no retorna nada entonces cuidado con los ciclos infinitos
            return Excepcion()
        
        cadenaRetorno += consola.genComment("INSTRUCCION IF")
        cadenaRetorno += consola.genComment("CONDICION IF")
        cadenaRetorno += retornoExpresion.codigoTraducido
        # Se valida si ya se creo la salida de la instrucción if, esto sirve para los else if/else.
        if self.etqSalida == None:
            self.etqSalida = consola.genNewEtq()
        
        # Si solo viene el if
        if self.insEntraOpcionales == None:
            newEnviroment = TablaSimbolos(ts, "IF-")
            lTrue = consola.genNewEtq()
            lFalse = consola.genNewEtq()

            cadenaRetorno += consola.genComment("VALIDACION IF")
            cadenaRetorno += consola.genIf(retornoExpresion.valor+"==1", consola.genGoto2(lTrue))
            cadenaRetorno += consola.genGoto(lFalse)
            cadenaRetorno += "{}: \n".format(lTrue)
            for ins in self.insEntraIf:
                ins.etqContinue = self.etqContinue
                ins.etqBreak = self.etqBreak
                ins.etqReturn = self.etqReturn
                resIns : Union[Excepcion, str] = ins.traducir(newEnviroment)
                if isinstance(resIns, Excepcion):
                    return Excepcion()
                
                if isinstance(resIns, RetornoTraduccion):
                    cadenaRetorno += resIns.codigoTraducido
                    continue
                
                cadenaRetorno += resIns
            cadenaRetorno += consola.genGoto(self.etqSalida)
            cadenaRetorno += "{}: \n".format(lFalse)
            cadenaRetorno += consola.genGoto(self.etqSalida)
            cadenaRetorno += "{}: \n".format(self.etqSalida)
            return cadenaRetorno
        # si if viene con otra condición (else if, else)
        else:
            # Primero validar el if principal y luego lo demás
            newEnviroment = TablaSimbolos(ts, "IF-")
            
            lTrue = consola.genNewEtq()
            lFalse = consola.genNewEtq()

            cadenaRetorno += consola.genComment("VALIDACION IF")
            cadenaRetorno += consola.genIf(retornoExpresion.valor+"==1", consola.genGoto2(lTrue))
            cadenaRetorno += consola.genGoto(lFalse)
            cadenaRetorno += "{}: \n".format(lTrue)
            for ins in self.insEntraIf:
                ins.etqContinue = self.etqContinue
                ins.etqBreak = self.etqBreak
                ins.etqReturn = self.etqReturn
                resIns : Union[Excepcion, str, RetornoTraduccion] = ins.traducir(newEnviroment)
                if isinstance(resIns, Excepcion):
                    return Excepcion()
                if isinstance(resIns, RetornoTraduccion):
                    cadenaRetorno += resIns.codigoTraducido
                    continue
                cadenaRetorno += resIns
            cadenaRetorno += consola.genGoto(self.etqSalida)
            cadenaRetorno += "{}: \n".format(lFalse)
            # ELSE IF
            if not isinstance(self.insEntraOpcionales, list):
                if isinstance(self.insEntraOpcionales, If):
                    cadenaRetorno += consola.genComment("ELSE IF")
                    self.insEntraOpcionales.etqBreak = self.etqBreak
                    self.insEntraOpcionales.etqContinue = self.etqContinue
                    self.insEntraOpcionales.etqSalida = self.etqSalida
                    self.insEntraOpcionales.etqReturn = self.etqReturn
                    resinsEntraOpcionales:str = self.insEntraOpcionales.traducir(newEnviroment)
                    if isinstance(resinsEntraOpcionales, Excepcion):
                        return Excepcion()
                    cadenaRetorno += resinsEntraOpcionales

                    return cadenaRetorno

            # ELSE
            else:
                newEnviroment2 = TablaSimbolos(ts, "ELSE-")
                cadenaRetorno += consola.genComment("ELSE")
                for ins in self.insEntraOpcionales:
                    ins.etqContinue = self.etqContinue
                    ins.etqBreak = self.etqBreak
                    ins.etqReturn = self.etqReturn
                    resElse : Union[str, Excepcion, RetornoTraduccion] = ins.traducir(newEnviroment2)
                    if isinstance(resElse, Excepcion):
                        return Excepcion()
                    if isinstance(resElse, RetornoTraduccion):
                        cadenaRetorno += resElse.codigoTraducido
                        continue
                    cadenaRetorno += resElse
                cadenaRetorno += consola.genGoto(self.etqSalida)
                cadenaRetorno += "{}: \n".format(self.etqSalida)
                return cadenaRetorno
        