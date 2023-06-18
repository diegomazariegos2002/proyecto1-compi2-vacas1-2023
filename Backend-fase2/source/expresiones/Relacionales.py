from datetime import datetime
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, RetornoTraduccion, Tipo, TipoRelacionales, TipoDato, TipoVariable
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.TablaSimbolos import TablaSimbolos

class Relacionales(Expresion):
    def __init__(self, operador, izq, der, line, column):
        super().__init__(line, column)
        self.operador = operador
        self.izq : Expresion = izq
        self.der : Expresion = der
        

    def ejecutar(self, ts: TablaSimbolos) -> Retorno:
        consolaGlobal = Consola()
        valorIzq : Retorno = self.izq.ejecutar(ts)
        if(self.der != None):
            valorDer : Retorno  = self.der.ejecutar(ts)

        if(self.operador == TipoRelacionales.MAYORQUE):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                if(valorIzq.valor > valorDer.valor):
                    return Retorno(True, TipoDato.BOOLEANO, TipoVariable.NORMAL)
                else: 
                    return Retorno(False, TipoDato.BOOLEANO, TipoVariable.NORMAL)
            elif valorIzq.tipo == TipoDato.CADENA and valorDer.tipo == TipoDato.CADENA:
                if(valorIzq.valor > valorDer.valor):
                    return Retorno(True, TipoDato.BOOLEANO, TipoVariable.NORMAL)
                else: 
                    return Retorno(False, TipoDato.BOOLEANO, TipoVariable.NORMAL)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error de tipos en operacion relacional", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL) 
        elif(self.operador == TipoRelacionales.MAYORIGUAL):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                if(valorIzq.valor >= valorDer.valor):
                    return Retorno(True, TipoDato.BOOLEANO, TipoVariable.NORMAL)
                else: 
                    return Retorno(False, TipoDato.BOOLEANO, TipoVariable.NORMAL)
            elif valorIzq.tipo == TipoDato.CADENA and valorDer.tipo == TipoDato.CADENA:
                if(valorIzq.valor >= valorDer.valor):
                    return Retorno(True, TipoDato.BOOLEANO, TipoVariable.NORMAL)
                else: 
                    return Retorno(False, TipoDato.BOOLEANO, TipoVariable.NORMAL)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error de tipos en operacion relacional", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
        elif(self.operador == TipoRelacionales.MENORQUE):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                if(valorIzq.valor < valorDer.valor):
                    return Retorno(True, TipoDato.BOOLEANO, TipoVariable.NORMAL)
                else: 
                    return Retorno(False, TipoDato.BOOLEANO, TipoVariable.NORMAL)
            elif valorIzq.tipo == TipoDato.CADENA and valorDer.tipo == TipoDato.CADENA:
                if(valorIzq.valor < valorDer.valor):
                    return Retorno(True, TipoDato.BOOLEANO, TipoVariable.NORMAL)
                else: 
                    return Retorno(False, TipoDato.BOOLEANO, TipoVariable.NORMAL)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error de tipos en operacion relacional", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
        elif(self.operador == TipoRelacionales.MENORIGUAL):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                if(valorIzq.valor <= valorDer.valor):
                    return Retorno(True, TipoDato.BOOLEANO, TipoVariable.NORMAL)
                else: 
                    return Retorno(False, TipoDato.BOOLEANO, TipoVariable.NORMAL)
            elif valorIzq.tipo == TipoDato.CADENA and valorDer.tipo == TipoDato.CADENA:
                if(valorIzq.valor <= valorDer.valor):
                    return Retorno(True, TipoDato.BOOLEANO, TipoVariable.NORMAL)
                else: 
                    return Retorno(False, TipoDato.BOOLEANO, TipoVariable.NORMAL)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error de tipos en operacion relacional", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
        
        elif(self.operador == TipoRelacionales.IGUALACION):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                if(valorIzq.valor == valorDer.valor):
                    return Retorno(True, TipoDato.BOOLEANO, TipoVariable.NORMAL)
                else: 
                    return Retorno(False, TipoDato.BOOLEANO, TipoVariable.NORMAL)
            elif valorIzq.tipo == TipoDato.CADENA and valorDer.tipo == TipoDato.CADENA:
                if(valorIzq.valor == valorDer.valor):
                    return Retorno(True, TipoDato.BOOLEANO, TipoVariable.NORMAL)
                else: 
                    return Retorno(False, TipoDato.BOOLEANO, TipoVariable.NORMAL)
            elif valorIzq.tipo == TipoDato.BOOLEANO and valorDer.tipo == TipoDato.BOOLEANO:
                if(valorIzq.valor == valorDer.valor):
                    return Retorno(True, TipoDato.BOOLEANO, TipoVariable.NORMAL)
                else: 
                    return Retorno(False, TipoDato.BOOLEANO, TipoVariable.NORMAL)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error de tipos en operacion relacional", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
        elif(self.operador == TipoRelacionales.DIFERENTE):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                if(valorIzq.valor != valorDer.valor):
                    return Retorno(True, TipoDato.BOOLEANO, TipoVariable.NORMAL)
                else: 
                    return Retorno(False, TipoDato.BOOLEANO, TipoVariable.NORMAL)
            elif valorIzq.tipo == TipoDato.CADENA and valorDer.tipo == TipoDato.CADENA:
                if(valorIzq.valor != valorDer.valor):
                    return Retorno(True, TipoDato.BOOLEANO, TipoVariable.NORMAL)
                else: 
                    return Retorno(False, TipoDato.BOOLEANO, TipoVariable.NORMAL)
            elif valorIzq.tipo == TipoDato.BOOLEANO and valorDer.tipo == TipoDato.BOOLEANO:
                if(valorIzq.valor != valorDer.valor):
                    return Retorno(True, TipoDato.BOOLEANO, TipoVariable.NORMAL)
                else: 
                    return Retorno(False, TipoDato.BOOLEANO, TipoVariable.NORMAL)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error de tipos en operacion relacional", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)

        # ERROR
        consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error ese tipo en operacion relacional no existe", self.line, self.column, datetime.now()))
        return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
    
    def graficarAst(self):
        consola = Consola()
        nombreOperacion = f'instruccion_{self.line}_{self.column}_{str(id(self))}_'
        output = ""
        
        if(self.operador == TipoRelacionales.MAYORQUE):
            output += f"{nombreOperacion}[label=\"<Expresion>\nMayorQue (>)\"];"
            output += f"{nombreOperacion}->{self.izq.graficarAst()};"
            output += f"{nombreOperacion}->{self.der.graficarAst()};"
            
        elif(self.operador == TipoRelacionales.MAYORIGUAL):
            output += f"{nombreOperacion}[label=\"<Expresion>\nMayorIgual (>=)\"];"
            output += f"{nombreOperacion}->{self.izq.graficarAst()};"
            output += f"{nombreOperacion}->{self.der.graficarAst()};"
            
        elif(self.operador == TipoRelacionales.MENORQUE):
            output += f"{nombreOperacion}[label=\"<Expresion>\nMenorQue (<)\"];"
            output += f"{nombreOperacion}->{self.izq.graficarAst()};"
            output += f"{nombreOperacion}->{self.der.graficarAst()};"
            
        elif(self.operador == TipoRelacionales.MENORIGUAL):
            output += f"{nombreOperacion}[label=\"<Expresion>\nMenorIgual (<=)\"];"
            output += f"{nombreOperacion}->{self.izq.graficarAst()};"
            output += f"{nombreOperacion}->{self.der.graficarAst()};"
            
        elif(self.operador == TipoRelacionales.IGUALACION):
            output += f"{nombreOperacion}[label=\"<Expresion>\nIgualacion (===)\"];"
            output += f"{nombreOperacion}->{self.izq.graficarAst()};"
            output += f"{nombreOperacion}->{self.der.graficarAst()};"
            
        elif(self.operador == TipoRelacionales.DIFERENTE):
            output += f"{nombreOperacion}[label=\"<Expresion>\nDiferente (!==)\"];"
            output += f"{nombreOperacion}->{self.izq.graficarAst()};"
            output += f"{nombreOperacion}->{self.der.graficarAst()};"
            
        consola.set_AstGrafico(output)
        return nombreOperacion
    
    def traducir(self, ts: TablaSimbolos):
        consolaGlobal: Consola = Consola()
        cadenaRetornoExpresion = ""
        operador = ""
        
        valorIzq : RetornoTraduccion = self.izq.traducir(ts)
        if valorIzq.tipo == TipoDato.ERROR: return RetornoTraduccion(valor="Error",
                                                                     tipo=TipoDato.ERROR,
                                                                     tipoVariable=TipoVariable.NORMAL) 
        valorDer : RetornoTraduccion  = self.der.traducir(ts)
        if valorDer.tipo == TipoDato.ERROR: return RetornoTraduccion(valor="Error",
                                                                     tipo=TipoDato.ERROR,
                                                                     tipoVariable=TipoVariable.NORMAL) 
        
        if(self.operador == TipoRelacionales.MAYORQUE):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                operador = " > "
            elif valorIzq.tipo == TipoDato.CADENA and valorDer.tipo == TipoDato.CADENA:
                operador = " > "
                comparacionCadenas = consolaGlobal.genCompStrings2(valorIzq.valor, valorDer.valor, operador)
                cadenaRetornoExpresion += (consolaGlobal.genComment(f"EXPRESIONES RELACION {operador}")+
                                   consolaGlobal.genComment(f"EXPRESION IZQUIERDA {valorIzq.valor} [{operador}]")+
                                   str(valorIzq.codigoTraducido)+
                                   consolaGlobal.genComment(f"EXPRESION DERECHA {valorDer.valor} [{operador}]")+
                                   str(valorDer.codigoTraducido)+
                                   consolaGlobal.genComment(f"COMPARACION [{operador}] {valorIzq.valor} {valorDer.valor}")+
                                   comparacionCadenas["codigo"])
                resultadoRelacion = comparacionCadenas["temp"]
                
                return RetornoTraduccion(valor=resultadoRelacion,
                                            tipo=TipoDato.BOOLEANO,
                                            tipoVariable=TipoVariable.NORMAL,
                                            codigoTraducido=cadenaRetornoExpresion)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error de tipos en operacion relacional", self.line, self.column, datetime.now()))
                return RetornoTraduccion(valor="Error",
                                            tipo=TipoDato.ERROR,
                                            tipoVariable=TipoVariable.NORMAL) 
        elif(self.operador == TipoRelacionales.MAYORIGUAL):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                operador = " >= "
            elif valorIzq.tipo == TipoDato.CADENA and valorDer.tipo == TipoDato.CADENA:
                operador = " >= "
                comparacionCadenas = consolaGlobal.genCompStrings2(valorIzq.valor, valorDer.valor, operador)
                cadenaRetornoExpresion += (consolaGlobal.genComment(f"EXPRESIONES RELACION {operador}")+
                                   consolaGlobal.genComment(f"EXPRESION IZQUIERDA {valorIzq.valor} [{operador}]")+
                                   str(valorIzq.codigoTraducido)+
                                   consolaGlobal.genComment(f"EXPRESION DERECHA {valorDer.valor} [{operador}]")+
                                   str(valorDer.codigoTraducido)+
                                   consolaGlobal.genComment(f"COMPARACION [{operador}] {valorIzq.valor} {valorDer.valor}")+
                                   comparacionCadenas["codigo"])
                resultadoRelacion = comparacionCadenas["temp"]
                
                return RetornoTraduccion(valor=resultadoRelacion,
                                            tipo=TipoDato.BOOLEANO,
                                            tipoVariable=TipoVariable.NORMAL,
                                            codigoTraducido=cadenaRetornoExpresion)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error de tipos en operacion relacional", self.line, self.column, datetime.now()))
                return RetornoTraduccion(valor="Error",
                                            tipo=TipoDato.ERROR,
                                            tipoVariable=TipoVariable.NORMAL) 
        elif(self.operador == TipoRelacionales.MENORQUE):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                operador = " < "
            elif valorIzq.tipo == TipoDato.CADENA and valorDer.tipo == TipoDato.CADENA:
                operador = " < "
                comparacionCadenas = consolaGlobal.genCompStrings2(valorIzq.valor, valorDer.valor, operador)
                cadenaRetornoExpresion += (consolaGlobal.genComment(f"EXPRESIONES RELACION {operador}")+
                                   consolaGlobal.genComment(f"EXPRESION IZQUIERDA {valorIzq.valor} [{operador}]")+
                                   str(valorIzq.codigoTraducido)+
                                   consolaGlobal.genComment(f"EXPRESION DERECHA {valorDer.valor} [{operador}]")+
                                   str(valorDer.codigoTraducido)+
                                   consolaGlobal.genComment(f"COMPARACION [{operador}] {valorIzq.valor} {valorDer.valor}")+
                                   comparacionCadenas["codigo"])
                resultadoRelacion = comparacionCadenas["temp"]
                
                return RetornoTraduccion(valor=resultadoRelacion,
                                            tipo=TipoDato.BOOLEANO,
                                            tipoVariable=TipoVariable.NORMAL,
                                            codigoTraducido=cadenaRetornoExpresion)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error de tipos en operacion relacional", self.line, self.column, datetime.now()))
                return RetornoTraduccion(valor="Error",
                                            tipo=TipoDato.ERROR,
                                            tipoVariable=TipoVariable.NORMAL) 
        elif(self.operador == TipoRelacionales.MENORIGUAL):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                operador = " <= "
            elif valorIzq.tipo == TipoDato.CADENA and valorDer.tipo == TipoDato.CADENA:
                operador = " <= "
                comparacionCadenas = consolaGlobal.genCompStrings2(valorIzq.valor, valorDer.valor, operador)
                cadenaRetornoExpresion += (consolaGlobal.genComment(f"EXPRESIONES RELACION {operador}")+
                                   consolaGlobal.genComment(f"EXPRESION IZQUIERDA {valorIzq.valor} [{operador}]")+
                                   str(valorIzq.codigoTraducido)+
                                   consolaGlobal.genComment(f"EXPRESION DERECHA {valorDer.valor} [{operador}]")+
                                   str(valorDer.codigoTraducido)+
                                   consolaGlobal.genComment(f"COMPARACION [{operador}] {valorIzq.valor} {valorDer.valor}")+
                                   comparacionCadenas["codigo"])
                resultadoRelacion = comparacionCadenas["temp"]
                
                return RetornoTraduccion(valor=resultadoRelacion,
                                            tipo=TipoDato.BOOLEANO,
                                            tipoVariable=TipoVariable.NORMAL,
                                            codigoTraducido=cadenaRetornoExpresion)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error de tipos en operacion relacional", self.line, self.column, datetime.now()))
                return RetornoTraduccion(valor="Error",
                                            tipo=TipoDato.ERROR,
                                            tipoVariable=TipoVariable.NORMAL)      
        elif(self.operador == TipoRelacionales.IGUALACION):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                operador = " == "
            elif valorIzq.tipo == TipoDato.CADENA and valorDer.tipo == TipoDato.CADENA:
                operador = " == "
                comparacionCadenas = consolaGlobal.genCompStrings(valorIzq.valor, valorDer.valor)
                cadenaRetornoExpresion += (consolaGlobal.genComment(f"EXPRESIONES RELACION {operador}")+
                                   consolaGlobal.genComment(f"EXPRESION IZQUIERDA {valorIzq.valor} [{operador}]")+
                                   str(valorIzq.codigoTraducido)+
                                   consolaGlobal.genComment(f"EXPRESION DERECHA {valorDer.valor} [{operador}]")+
                                   str(valorDer.codigoTraducido)+
                                   consolaGlobal.genComment(f"COMPARACION IGUALDAD {valorIzq.valor} {valorDer.valor}")+
                                   comparacionCadenas["codigo"])
                resultadoRelacion = comparacionCadenas["temp"]
                
                return RetornoTraduccion(valor=resultadoRelacion,
                                            tipo=TipoDato.BOOLEANO,
                                            tipoVariable=TipoVariable.NORMAL,
                                            codigoTraducido=cadenaRetornoExpresion)
                
            elif valorIzq.tipo == TipoDato.BOOLEANO and valorDer.tipo == TipoDato.BOOLEANO:
                operador = " == "
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error de tipos en operacion relacional", self.line, self.column, datetime.now()))
                return RetornoTraduccion(valor="Error",
                                            tipo=TipoDato.ERROR,
                                            tipoVariable=TipoVariable.NORMAL)
        elif(self.operador == TipoRelacionales.DIFERENTE):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                operador = " != "
            elif valorIzq.tipo == TipoDato.CADENA and valorDer.tipo == TipoDato.CADENA:
                operador = " != "
                comparacionCadenas = consolaGlobal.genCompStrings(valorIzq.valor, valorDer.valor)
                tNegado = consolaGlobal.genNewTemp()
                negado = consolaGlobal.genNot(comparacionCadenas["temp"])
                cadenaRetornoExpresion += (consolaGlobal.genComment(f"EXPRESIONES RELACION {operador}")+
                                   consolaGlobal.genComment(f"EXPRESION IZQUIERDA {valorIzq.valor} [{operador}]")+
                                   str(valorIzq.codigoTraducido)+
                                   consolaGlobal.genComment(f"EXPRESION DERECHA {valorDer.valor} [{operador}]")+
                                   str(valorDer.codigoTraducido)+
                                   consolaGlobal.genComment(f"COMPARACION DIFERENCIA {valorIzq.valor} {valorDer.valor}")+
                                   comparacionCadenas["codigo"]+
                                   negado["codigo"])
                cadenaRetornoExpresion += consolaGlobal.genAsignacion(tNegado, negado["temp"])
                resultadoRelacion = tNegado
                
                return RetornoTraduccion(valor=resultadoRelacion,
                                            tipo=TipoDato.BOOLEANO,
                                            tipoVariable=TipoVariable.NORMAL,
                                            codigoTraducido=cadenaRetornoExpresion)
            elif valorIzq.tipo == TipoDato.BOOLEANO and valorDer.tipo == TipoDato.BOOLEANO:
                operador = " != "
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error de tipos en operacion relacional", self.line, self.column, datetime.now()))
                return RetornoTraduccion(valor="Error",
                                            tipo=TipoDato.ERROR,
                                            tipoVariable=TipoVariable.NORMAL)
        else:
            # ERROR
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error ese tipo en operacion relacional no existe", self.line, self.column, datetime.now()))
            return RetornoTraduccion(valor="Error",
                                                tipo=TipoDato.ERROR,
                                                tipoVariable=TipoVariable.NORMAL)
        
        codigoRelacion = ""
        relacion = str(valorIzq.valor) + operador + str(valorDer.valor)
        resultadoRelacion = consolaGlobal.genNewTemp()
        ltrue1 = consolaGlobal.genNewEtq()
        lfinal = consolaGlobal.genNewEtq()
        
        codigoRelacion += consolaGlobal.genIf(relacion, consolaGlobal.genGoto2(ltrue1))
        codigoRelacion += consolaGlobal.genAsignacion(resultadoRelacion, "0")
        codigoRelacion += consolaGlobal.genGoto(lfinal)
        codigoRelacion += f"{ltrue1}:\n"
        codigoRelacion += consolaGlobal.genAsignacion(resultadoRelacion, "1")
        codigoRelacion += f"{lfinal}:\n"
        
        cadenaRetornoExpresion += (consolaGlobal.genComment(f"EXPRESIONES RELACION {operador}")+
                                consolaGlobal.genComment(f"EXPRESION IZQUIERDA {valorIzq.valor} [{operador}]")+
                                str(valorIzq.codigoTraducido)+
                                consolaGlobal.genComment(f"EXPRESION DERECHA {valorDer.valor} [{operador}]")+
                                str(valorDer.codigoTraducido)+
                                codigoRelacion)
                
        return RetornoTraduccion(valor=resultadoRelacion,
                                    tipo=TipoDato.BOOLEANO,
                                    tipoVariable=TipoVariable.NORMAL,
                                    codigoTraducido=cadenaRetornoExpresion)
        
