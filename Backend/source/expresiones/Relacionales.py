from datetime import datetime
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, Tipo, TipoRelacionales, TipoDato, TipoVariable
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
        elif(self.operador == TipoRelacionales.MAYORIGUAL, TipoVariable.NORMAL):
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
                    return Retorno(False, TipoDato.BOOLEANO)
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
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error de tipos en operacion relacional", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)

        # ERROR
        consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error ese tipo en operacion relacional no existe", self.line, self.column, datetime.now()))
        return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)