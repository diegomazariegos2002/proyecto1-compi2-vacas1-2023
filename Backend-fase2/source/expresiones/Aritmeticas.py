from datetime import datetime
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, RetornoTraduccion, Tipo, Tipo_OperadorAritmetico, TipoDato, TipoVariable
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.TablaSimbolos import TablaSimbolos

class Arimeticas(Expresion):
    def __init__(self, operador, izq, der, line, column):
        super().__init__(line, column)
        self.operador = operador
        self.izq : Expresion = izq
        self.der : Expresion = der
        self.unico : Expresion = None
        if self.der == None:
            self.unico = self.izq
        

    def ejecutar(self, ts: TablaSimbolos) -> Retorno:
        consolaGlobal = Consola()
        valorIzq : Retorno = None
        valorDer : Retorno = None
        valorUnico : Retorno = None
        if self.unico != None:
            valorUnico = self.unico.ejecutar(ts)
            if valorUnico.tipo == TipoDato.ERROR:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)

        valorIzq = self.izq.ejecutar(ts)
        if(self.der != None):
            valorDer = self.der.ejecutar(ts)

        if(self.operador == Tipo_OperadorAritmetico.SUMA):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                return Retorno(valorIzq.valor + valorDer.valor, TipoDato.NUMERO, TipoVariable.NORMAL)
            elif valorIzq.tipo == TipoDato.CADENA and valorDer.tipo == TipoDato.CADENA:
                return Retorno(str(valorIzq.valor) + str(valorDer.valor), TipoDato.CADENA, TipoVariable.NORMAL)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
        elif(self.operador == Tipo_OperadorAritmetico.RESTA):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                return Retorno(valorIzq.valor-valorDer.valor, TipoDato.NUMERO, TipoVariable.NORMAL)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
        elif(self.operador == Tipo_OperadorAritmetico.MULTIPLICACION):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                return Retorno(valorIzq.valor*valorDer.valor, TipoDato.NUMERO, TipoVariable.NORMAL)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
        elif(self.operador == Tipo_OperadorAritmetico.DIVISION):
            if(valorDer.valor != 0):
                if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                    return Retorno(valorIzq.valor/valorDer.valor, TipoDato.NUMERO, TipoVariable.NORMAL)
                else:
                    # ERROR
                    consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                    return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "division por cero imposible de realizar", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
        elif(self.operador == Tipo_OperadorAritmetico.POTENCIA):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                return Retorno(valorIzq.valor ** valorDer.valor, TipoDato.NUMERO, TipoVariable.NORMAL)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
        elif(self.operador == Tipo_OperadorAritmetico.MODULO):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                return Retorno(valorIzq.valor % valorDer.valor, TipoDato.NUMERO, TipoVariable.NORMAL)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR)
        elif(self.operador == Tipo_OperadorAritmetico.NEGATIVO):
            if valorUnico.tipo == TipoDato.NUMERO:
                return Retorno(valorUnico.valor * (-1), TipoDato.NUMERO, TipoVariable.NORMAL)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
        else:
            # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
        
    def graficarAst(self) -> str:
        consola = Consola()
        nombreOperacion = f'instruccion_{self.line}_{self.column}_{str(id(self))}_'
        output = ""
        
        if(self.operador == Tipo_OperadorAritmetico.SUMA):
            output += f"{nombreOperacion}[label=\"<Expresion>\nSuma (+)\"];"
            output += f"{nombreOperacion}->{self.izq.graficarAst()};"
            output += f"{nombreOperacion}->{self.der.graficarAst()};"
            
        elif(self.operador == Tipo_OperadorAritmetico.RESTA):
            output += f"{nombreOperacion}[label=\"<Expresion>\nResta (-)\"];"
            output += f"{nombreOperacion}->{self.izq.graficarAst()};"
            output += f"{nombreOperacion}->{self.der.graficarAst()};"
            
        elif(self.operador == Tipo_OperadorAritmetico.MULTIPLICACION):
            output += f"{nombreOperacion}[label=\"<Expresion>\nMultiplicacion (*)\"];"
            output += f"{nombreOperacion}->{self.izq.graficarAst()};"
            output += f"{nombreOperacion}->{self.der.graficarAst()};"
            
        elif(self.operador == Tipo_OperadorAritmetico.DIVISION):
            output += f"{nombreOperacion}[label=\"<Expresion>\nDivison (/)\"];"
            output += f"{nombreOperacion}->{self.izq.graficarAst()};"
            output += f"{nombreOperacion}->{self.der.graficarAst()};"
            
        elif(self.operador == Tipo_OperadorAritmetico.POTENCIA):
            output += f"{nombreOperacion}[label=\"<Expresion>\nPotencia (^)\"];"
            output += f"{nombreOperacion}->{self.izq.graficarAst()};"
            output += f"{nombreOperacion}->{self.der.graficarAst()};"
            
        elif(self.operador == Tipo_OperadorAritmetico.MODULO):
            output += f"{nombreOperacion}[label=\"<Expresion>\nModulo (%)\"];"
            output += f"{nombreOperacion}->{self.izq.graficarAst()};"
            output += f"{nombreOperacion}->{self.der.graficarAst()};"
            
        elif(self.operador == Tipo_OperadorAritmetico.NEGATIVO):
            output += f"{nombreOperacion}[label=\"<Expresion>\nNegacion (-)\"];"
            output += f"{nombreOperacion}->{self.unico.graficarAst()};"
            
        consola.set_AstGrafico(output)
        return nombreOperacion
    
    
    def traducir(self, ts: TablaSimbolos):
        consolaGlobal: Consola = Consola()
        cadenaRetornoExpresion = ""
        valorIzq : RetornoTraduccion = None
        valorDer : RetornoTraduccion = None
        valorUnico : RetornoTraduccion = None
        if self.unico != None:
            valorUnico = self.unico.traducir(ts)
            if valorUnico.tipo == TipoDato.ERROR:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                return RetornoTraduccion(valor="Error",
                                         tipo=TipoDato.ERROR,
                                         tipoVariable=TipoVariable.NORMAL)
        if self.unico == None:
            valorIzq = self.izq.traducir(ts)
        elif self.unico != None:
            valorIzq = valorUnico 
        if(self.der != None):
            valorDer = self.der.traducir(ts)

        if(self.operador == Tipo_OperadorAritmetico.SUMA):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                resultadoSuma = consolaGlobal.genNewTemp()
                cadenaRetornoExpresion += consolaGlobal.genComment("EXPRESIONES SUMA")
                
                cadenaRetornoExpresion += valorIzq.codigoTraducido
                cadenaRetornoExpresion += valorDer.codigoTraducido
                cadenaRetornoExpresion += consolaGlobal.genComment("OPERACION SUMA")
                cadenaRetornoExpresion += (resultadoSuma + 
                                             " = " +
                                             str(valorIzq.valor) +
                                             " + " +
                                             str(valorDer.valor) + "\n")
                
                return RetornoTraduccion(valor=resultadoSuma,
                                         tipo=TipoDato.NUMERO,
                                         tipoVariable=TipoVariable.NORMAL,
                                         codigoTraducido=cadenaRetornoExpresion)

            elif valorIzq.tipo == TipoDato.CADENA and valorDer.tipo == TipoDato.CADENA:
                cadenaRetornoExpresion += consolaGlobal.genComment("CADENAS CONCATENACION")
                cadenaRetornoExpresion += valorIzq.codigoTraducido
                cadenaRetornoExpresion += valorDer.codigoTraducido
                
                dirCadRes = consolaGlobal.genNewTemp()
                dirCadena = consolaGlobal.genNewTemp()
                charCadena = consolaGlobal.genNewTemp()
                l1 = consolaGlobal.genNewEtq()
                l2 = consolaGlobal.genNewEtq()
                l3 = consolaGlobal.genNewEtq()
                l4 = consolaGlobal.genNewEtq()
                # Crear una nueva cadena -> asignarle cadena 1 y 2
                cadenaRetornoExpresion += consolaGlobal.genComment("OPERACION CONCATENACION")
                cadenaRetornoExpresion += consolaGlobal.genAsignacion(dirCadRes, "HP")
                # cadena 1
                cadenaRetornoExpresion += consolaGlobal.genAsignacion(dirCadena, valorIzq.valor)
                cadenaRetornoExpresion += "{}:\n".format(l1)
                cadenaRetornoExpresion += consolaGlobal.genAsignacion(charCadena,
                                                "HEAP[ int({})]".format(dirCadena))
                cadenaRetornoExpresion += consolaGlobal.genIf("{} == -1".format(charCadena),
                                        consolaGlobal.genGoto2(l2))
                cadenaRetornoExpresion += consolaGlobal.genAsignacion("HEAP[int(HP)]", charCadena)
                cadenaRetornoExpresion += consolaGlobal.genAsignacion("HP", "HP + 1")
                cadenaRetornoExpresion += consolaGlobal.genAsignacion(dirCadena, "{} + 1".format(dirCadena))
                cadenaRetornoExpresion += consolaGlobal.genGoto(l1)
                cadenaRetornoExpresion += "{}:\n".format(l2)
                # cadena 2
                cadenaRetornoExpresion += consolaGlobal.genAsignacion(dirCadena, valorDer.valor)
                cadenaRetornoExpresion += "{}:\n".format(l3)

                cadenaRetornoExpresion += consolaGlobal.genAsignacion(charCadena,
                                                "HEAP[ int({})]".format(dirCadena))
                cadenaRetornoExpresion += consolaGlobal.genIf("{} == -1".format(charCadena),
                                        consolaGlobal.genGoto2(l4))
                cadenaRetornoExpresion += consolaGlobal.genAsignacion("HEAP[int(HP)]", charCadena)
                cadenaRetornoExpresion += consolaGlobal.genAsignacion("HP", "HP + 1")
                cadenaRetornoExpresion += consolaGlobal.genAsignacion(dirCadena, "{} + 1".format(dirCadena))
                cadenaRetornoExpresion += consolaGlobal.genGoto(l3)
                cadenaRetornoExpresion += "{}:\n".format(l4)
                cadenaRetornoExpresion +=consolaGlobal.genAsignacion("HEAP[int(HP)]",-1) # fin de cadena
                cadenaRetornoExpresion += consolaGlobal.genAsignacion("HP", "HP + 1")
                
                return RetornoTraduccion(valor=dirCadRes,
                                         tipo=TipoDato.CADENA,
                                         tipoVariable=TipoVariable.NORMAL,
                                         codigoTraducido=cadenaRetornoExpresion)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                return RetornoTraduccion(valor="Error",
                                         tipo=TipoDato.ERROR,
                                         tipoVariable=TipoVariable.NORMAL)
        elif(self.operador == Tipo_OperadorAritmetico.RESTA):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                resultadoSuma = consolaGlobal.genNewTemp()
                cadenaRetornoExpresion += consolaGlobal.genComment("EXPRESIONES RESTA")
                cadenaRetornoExpresion += valorIzq.codigoTraducido
                cadenaRetornoExpresion += valorDer.codigoTraducido
                cadenaRetornoExpresion += consolaGlobal.genComment("OPERACION RESTA")
                cadenaRetornoExpresion += (resultadoSuma + 
                                             " = " +
                                             str(valorIzq.valor) +
                                             " - " +
                                             str(valorDer.valor) + "\n")
                
                return RetornoTraduccion(valor=resultadoSuma,
                                         tipo=TipoDato.NUMERO,
                                         tipoVariable=TipoVariable.NORMAL,
                                         codigoTraducido=cadenaRetornoExpresion)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                return RetornoTraduccion(valor="Error",
                                         tipo=TipoDato.ERROR,
                                         tipoVariable=TipoVariable.NORMAL)
        elif(self.operador == Tipo_OperadorAritmetico.MULTIPLICACION):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                resultadoSuma = consolaGlobal.genNewTemp()
                cadenaRetornoExpresion += consolaGlobal.genComment("EXPRESIONES MULTIPLICACION")
                cadenaRetornoExpresion += valorIzq.codigoTraducido
                cadenaRetornoExpresion += valorDer.codigoTraducido
                cadenaRetornoExpresion += consolaGlobal.genComment("OPERACION MULTIPLICACION")
                
                cadenaRetornoExpresion += (resultadoSuma + 
                                             " = " +
                                             str(valorIzq.valor) +
                                             " * " +
                                             str(valorDer.valor) + "\n")
                
                return RetornoTraduccion(valor=resultadoSuma,
                                         tipo=TipoDato.NUMERO,
                                         tipoVariable=TipoVariable.NORMAL,
                                         codigoTraducido=cadenaRetornoExpresion)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                return RetornoTraduccion(valor="Error",
                                         tipo=TipoDato.ERROR,
                                         tipoVariable=TipoVariable.NORMAL)
        elif(self.operador == Tipo_OperadorAritmetico.DIVISION):
            if(valorDer.valor != 0):
                if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                    resultadoSuma = consolaGlobal.genNewTemp()
                    cadenaRetornoExpresion += consolaGlobal.genComment("EXPRESIONES DIVISION")
                    cadenaRetornoExpresion += valorIzq.codigoTraducido
                    cadenaRetornoExpresion += valorDer.codigoTraducido
                    cadenaRetornoExpresion += consolaGlobal.genComment("OPERACION DIVISION")
                    
                    cadenaRetornoExpresion += (resultadoSuma + 
                                                " = " +
                                                str(valorIzq.valor) +
                                                " / " +
                                                str(valorDer.valor) + "\n")
                    
                    return RetornoTraduccion(valor=resultadoSuma,
                                            tipo=TipoDato.NUMERO,
                                            tipoVariable=TipoVariable.NORMAL,
                                            codigoTraducido=cadenaRetornoExpresion)
                else:
                    # ERROR
                    consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                    return RetornoTraduccion(valor="Error",
                                         tipo=TipoDato.ERROR,
                                         tipoVariable=TipoVariable.NORMAL)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "division por cero imposible de realizar", self.line, self.column, datetime.now()))
                cadena = consolaGlobal.genPrintC(77)
                cadena += consolaGlobal.genPrintC(97)
                cadena += consolaGlobal.genPrintC(116)
                cadena += consolaGlobal.genPrintC(104)
                cadena += consolaGlobal.genPrintC(69)
                cadena += consolaGlobal.genPrintC(114)
                cadena += consolaGlobal.genPrintC(114)
                cadena += consolaGlobal.genPrintC(111)
                cadena += consolaGlobal.genPrintC(114)
                return RetornoTraduccion(valor="Error",
                                         tipo=TipoDato.ERROR,
                                         tipoVariable=TipoVariable.NORMAL,
                                         codigoTraducido=cadena)
        elif(self.operador == Tipo_OperadorAritmetico.POTENCIA):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                resultadoSuma = consolaGlobal.genNewTemp()
                cadenaRetornoExpresion += consolaGlobal.genComment("EXPRESIONES POTENCIA")
                cadenaRetornoExpresion += valorIzq.codigoTraducido
                cadenaRetornoExpresion += valorDer.codigoTraducido
                cadenaRetornoExpresion += consolaGlobal.genComment("OPERACION POTENCIA")
                # math.Pow(base, exponente)
                cadenaRetornoExpresion += (resultadoSuma + 
                                             " = math.Pow(" +
                                             str(valorIzq.valor) +
                                             " , " +
                                             str(valorDer.valor) + ")\n")
                
                return RetornoTraduccion(valor=resultadoSuma,
                                         tipo=TipoDato.NUMERO,
                                         tipoVariable=TipoVariable.NORMAL,
                                         codigoTraducido=cadenaRetornoExpresion)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                return RetornoTraduccion(valor="Error",
                                         tipo=TipoDato.ERROR,
                                         tipoVariable=TipoVariable.NORMAL)
        elif(self.operador == Tipo_OperadorAritmetico.MODULO):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                resultadoSuma = consolaGlobal.genNewTemp()
                cadenaRetornoExpresion += consolaGlobal.genComment("EXPRESIONES MODULO")
                cadenaRetornoExpresion += valorIzq.codigoTraducido
                cadenaRetornoExpresion += valorDer.codigoTraducido
                cadenaRetornoExpresion += consolaGlobal.genComment("OPERACION MODULO")
                
                cadenaRetornoExpresion += (resultadoSuma + 
                                             " = math.Mod(" +
                                             str(valorIzq.valor) +
                                             "," +
                                             str(valorDer.valor) + ")\n")
                
                return RetornoTraduccion(valor=resultadoSuma,
                                         tipo=TipoDato.NUMERO,
                                         tipoVariable=TipoVariable.NORMAL,
                                         codigoTraducido=cadenaRetornoExpresion)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR)
        elif(self.operador == Tipo_OperadorAritmetico.NEGATIVO):
            if valorUnico.tipo == TipoDato.NUMERO:
                resultadoSuma = consolaGlobal.genNewTemp()
                cadenaRetornoExpresion += consolaGlobal.genComment("EXPRESION NEGATIVO")
                cadenaRetornoExpresion += valorUnico.codigoTraducido
                cadenaRetornoExpresion += consolaGlobal.genComment("OPERACION NEGATIVO")
                
                cadenaRetornoExpresion += (resultadoSuma + 
                                             " = " +
                                             str(valorUnico.valor) +
                                             " * (-1) " + "\n")
                
                return RetornoTraduccion(valor=resultadoSuma,
                                         tipo=TipoDato.NUMERO,
                                         tipoVariable=TipoVariable.NORMAL,
                                         codigoTraducido=cadenaRetornoExpresion)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                return RetornoTraduccion(valor="Error",
                                         tipo=TipoDato.ERROR,
                                         tipoVariable=TipoVariable.NORMAL)
        else:
            # ERROR
            consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
            return RetornoTraduccion(valor="Error",
                                        tipo=TipoDato.ERROR,
                                        tipoVariable=TipoVariable.NORMAL)