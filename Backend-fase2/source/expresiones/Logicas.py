from datetime import datetime
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, RetornoTraduccion, Tipo, TipoLogicas, TipoDato, TipoVariable
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.TablaSimbolos import TablaSimbolos

class Logicas(Expresion):
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
        valorUnico : Retorno = None
        if self.unico != None:
            valorUnico = self.unico.ejecutar(ts)
            if valorUnico.tipo == TipoDato.ERROR:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error de tipos en operacion logica", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL) 
            
        valorIzq : Retorno = self.izq.ejecutar(ts)
        if(self.der != None):
            valorDer : Retorno  = self.der.ejecutar(ts)

        if(self.operador == TipoLogicas.AND):
            if valorIzq.tipo == TipoDato.BOOLEANO and valorDer.tipo == TipoDato.BOOLEANO:
                if(valorIzq.valor == True and valorDer.valor == True):
                    return Retorno(True, TipoDato.BOOLEANO, TipoVariable.NORMAL)
                else: 
                    return Retorno(False, TipoDato.BOOLEANO, TipoVariable.NORMAL)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error de tipos en operacion logica", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
        elif(self.operador == TipoLogicas.OR):
            if valorIzq.tipo == TipoDato.BOOLEANO and valorDer.tipo == TipoDato.BOOLEANO:
                if(valorIzq.valor == False and valorDer.valor == False): 
                    return Retorno(False, TipoDato.BOOLEANO, TipoVariable.NORMAL)
                else:
                    return Retorno(True, TipoDato.BOOLEANO, TipoVariable.NORMAL)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error de tipos en operacion logica", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
        elif(self.operador == TipoLogicas.NOT):
            if valorUnico.tipo == TipoDato.BOOLEANO:
                if(valorIzq.valor == True):
                    return Retorno(True, TipoDato.BOOLEANO, TipoVariable.NORMAL)
                elif(valorIzq.valor == False): 
                    return Retorno(True, TipoDato.BOOLEANO, TipoVariable.NORMAL)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error de tipos en operacion logica", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)

        # ERROR
        consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "No existe ese tipo de logica", self.line, self.column, datetime.now()))
        return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
    
    def graficarAst(self):
        consola = Consola()
        nombreOperacion = f'instruccion_{self.line}_{self.column}_{str(id(self))}_'
        output = ""
        
        if(self.operador == TipoLogicas.AND):
            output += f"{nombreOperacion}[label=\"<Expresion>\nAND (&&)\"];"
            output += f"{nombreOperacion}->{self.izq.graficarAst()};"
            output += f"{nombreOperacion}->{self.der.graficarAst()};"
            
        elif(self.operador == TipoLogicas.OR):
            output += f"{nombreOperacion}[label=\"<Expresion>\nOR (||)\"];"
            output += f"{nombreOperacion}->{self.izq.graficarAst()};"
            output += f"{nombreOperacion}->{self.der.graficarAst()};"
            
        elif(self.operador == TipoLogicas.NOT):
            output += f"{nombreOperacion}[label=\"<Expresion>\nNOT (!)\"];"
            output += f"{nombreOperacion}->{self.unico.graficarAst()};"
            
        consola.set_AstGrafico(output)
        return nombreOperacion
    
    def traducir(self, ts: TablaSimbolos):
        consolaGlobal: Consola = Consola()
        cadenaRetornoExpresion = ""
        operador = ""
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
        
        if(self.operador == TipoLogicas.AND):
            if valorIzq.tipo == TipoDato.BOOLEANO and valorDer.tipo == TipoDato.BOOLEANO:
                operador = "&&"
                OpLogic = consolaGlobal.genAnd(valorIzq.valor, valorDer.valor)
                
                cadenaRetornoExpresion += (consolaGlobal.genComment(f"EXPRESIONES LOGICA {operador}")+
                                        consolaGlobal.genComment(f"EXPRESION IZQUIERDA {valorIzq.valor} [{operador}]")+
                                        str(valorIzq.codigoTraducido)+
                                        consolaGlobal.genComment(f"EXPRESION DERECHA {valorDer.valor} [{operador}]")+
                                        str(valorDer.codigoTraducido)+
                                        consolaGlobal.genComment(f"LOGICA AND {valorIzq.valor} {valorDer.valor}")+
                                        OpLogic["codigo"])
                resOpLogic = OpLogic["temp"]
                        
                return RetornoTraduccion(valor=resOpLogic,
                                            tipo=TipoDato.BOOLEANO,
                                            tipoVariable=TipoVariable.NORMAL,
                                            codigoTraducido=cadenaRetornoExpresion)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error de tipos en operacion logica", self.line, self.column, datetime.now()))
                return RetornoTraduccion(valor="Error",
                                                tipo=TipoDato.ERROR,
                                                tipoVariable=TipoVariable.NORMAL)
        elif(self.operador == TipoLogicas.OR):
            if valorIzq.tipo == TipoDato.BOOLEANO and valorDer.tipo == TipoDato.BOOLEANO:
                operador = "||"
                OpLogic = consolaGlobal.genOr(valorIzq.valor, valorDer.valor)
                
                cadenaRetornoExpresion += (consolaGlobal.genComment(f"EXPRESIONES LOGICA {operador}")+
                                        consolaGlobal.genComment(f"EXPRESION IZQUIERDA {valorIzq.valor} [{operador}]")+
                                        str(valorIzq.codigoTraducido)+
                                        consolaGlobal.genComment(f"EXPRESION DERECHA {valorDer.valor} [{operador}]")+
                                        str(valorDer.codigoTraducido)+
                                        consolaGlobal.genComment(f"LOGICA OR {valorIzq.valor} {valorDer.valor}")+
                                        OpLogic["codigo"])
                resOpLogic = OpLogic["temp"]
                        
                return RetornoTraduccion(valor=resOpLogic,
                                            tipo=TipoDato.BOOLEANO,
                                            tipoVariable=TipoVariable.NORMAL,
                                            codigoTraducido=cadenaRetornoExpresion)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error de tipos en operacion logica", self.line, self.column, datetime.now()))
                return RetornoTraduccion(valor="Error",
                                                tipo=TipoDato.ERROR,
                                                tipoVariable=TipoVariable.NORMAL)
        elif(self.operador == TipoLogicas.NOT):
            if valorUnico.tipo == TipoDato.BOOLEANO:
                operador = "!"
                OpLogic = consolaGlobal.genNot(valorUnico.valor)
                
                cadenaRetornoExpresion += (consolaGlobal.genComment(f"EXPRESIONES LOGICA {operador}")+
                                        consolaGlobal.genComment(f"EXPRESION IZQUIERDA {valorUnico.valor} [{operador}]")+
                                        str(valorIzq.codigoTraducido)+
                                        consolaGlobal.genComment(f"LOGICA NOT {valorUnico.valor}")+
                                        OpLogic["codigo"])
                resOpLogic = OpLogic["temp"]
                        
                return RetornoTraduccion(valor=resOpLogic,
                                            tipo=TipoDato.BOOLEANO,
                                            tipoVariable=TipoVariable.NORMAL,
                                            codigoTraducido=cadenaRetornoExpresion)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error de tipos en operacion logica", self.line, self.column, datetime.now()))
                return RetornoTraduccion(valor="Error",
                                                tipo=TipoDato.ERROR,
                                                tipoVariable=TipoVariable.NORMAL)

        # ERROR
        consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "No existe ese tipo de logica", self.line, self.column, datetime.now()))
        return RetornoTraduccion(valor="Error",
                                                tipo=TipoDato.ERROR,
                                                tipoVariable=TipoVariable.NORMAL)
        
            
        