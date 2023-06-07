from datetime import datetime
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, Tipo, Tipo_OperadorAritmetico, TipoDato
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
                return Retorno("Error", TipoDato.ERROR)

        valorIzq = self.izq.ejecutar(ts)
        if(self.der != None):
            valorDer = self.der.ejecutar(ts)

        if(self.operador == Tipo_OperadorAritmetico.SUMA):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                return Retorno(valorIzq.valor + valorDer.valor, TipoDato.NUMERO)
            elif valorIzq.tipo == TipoDato.CADENA and valorDer.tipo == TipoDato.CADENA:
                return Retorno(str(valorIzq.valor) + str(valorDer.valor), TipoDato.CADENA)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR)
        elif(self.operador == Tipo_OperadorAritmetico.RESTA):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                return Retorno(valorIzq.valor-valorDer.valor, TipoDato.NUMERO)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR)
        elif(self.operador == Tipo_OperadorAritmetico.MULTIPLICACION):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                return Retorno(valorIzq.valor*valorDer.valor, TipoDato.NUMERO)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR)
        elif(self.operador == Tipo_OperadorAritmetico.DIVISION):
            if(valorDer.valor != 0):
                if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                    return Retorno(valorIzq.valor/valorDer.valor, TipoDato.NUMERO)
                else:
                    # ERROR
                    consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                    return Retorno("Error", TipoDato.ERROR)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "division por cero imposible de realizar", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR)
        elif(self.operador == Tipo_OperadorAritmetico.POTENCIA):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                return Retorno(valorIzq.valor ** valorDer.valor, TipoDato.NUMERO)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR)
        elif(self.operador == Tipo_OperadorAritmetico.MODULO):
            if valorIzq.tipo == TipoDato.NUMERO and valorDer.tipo == TipoDato.NUMERO:
                return Retorno(valorIzq.valor % valorDer.valor, TipoDato.NUMERO)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR)
        elif(self.operador == Tipo_OperadorAritmetico.NEGATIVO):
            if valorUnico.tipo == TipoDato.NUMERO:
                return Retorno(valorUnico.valor * (-1), TipoDato.NUMERO)
            else:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR)
        else:
            # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en operacion aritmetica", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR)
            