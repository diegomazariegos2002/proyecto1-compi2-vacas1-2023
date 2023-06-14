from datetime import datetime
from typing import Union
from source.abstracto.Retorno import Retorno, TipoDato, TipoVariable
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
        consola.set_AstGrafico(f"{nombreNodo}[label=\"\\<Instruccion\\>\\nCondicion\"];\n")
        consola.set_AstGrafico(f"{nombreNodoCondicion}->{self.condicion.graficarAst()};\n")
        cont = 0
        nombreNodoAnterior = ""

        for instruccion in self.insEntraIf:
            try:
                if cont == 0:
                    nombreNodoAnterior = instruccion.graficarAst()
                    consola.set_AstGrafico(f"{nombreNodo}->{nombreNodoAnterior};\n")
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
        
        