from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, Tipo, Tipo_OperadorAritmetico
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
        valorIzq : Retorno = None
        valorDer : Retorno = None
        valorUnico : Retorno = None
        if self.unico != None:
            valorUnico = self.unico.ejecutar(ts)
            if valorUnico.tipo == Tipo.ERROR:
                return 

        valorIzq = self.izq.ejecutar(ts)
        if(self.der != None):
            valorDer = self.der.ejecutar(ts)

        if(self.operador == Tipo_OperadorAritmetico.SUMA):
            if valorIzq.tipo == Tipo.NUMBER and valorDer.tipo == Tipo.NUMBER:
                return Retorno(valorIzq.valor + valorDer.valor, Tipo.NUMBER)
            elif valorIzq.tipo == Tipo.string and valorDer.tipo == Tipo.str:
                return Retorno(str(valorIzq.valor) + str(valorDer.valor), Tipo.STRING)
            else:
                print("ERROR")
        elif(self.operador == Tipo_OperadorAritmetico.RESTA):
            if valorIzq.tipo == Tipo.NUMBER and valorDer.tipo == Tipo.NUMBER:
                return Retorno(valorIzq.valor-valorDer.valor, Tipo.NUMBER)
            else:
                print("ERROR")
        elif(self.operador == Tipo_OperadorAritmetico.MULTIPLICACION):
            if valorIzq.tipo == Tipo.NUMBER and valorDer.tipo == Tipo.NUMBER:
                return Retorno(valorIzq.valor*valorDer.valor, Tipo.NUMBER)
            else:
                print("ERROR")
        elif(self.operador == Tipo_OperadorAritmetico.DIVISION):
            if(valorDer.valor != 0):
                if valorIzq.tipo == Tipo.NUMBER and valorDer.tipo == Tipo.NUMBER:
                    return Retorno(valorIzq.valor/valorDer.valor, Tipo.NUMBER)
                else:
                    # No se puede realizar la división porque los tipos no son válidos.
                    print("ERROR")
            else:
                # división por cero
                print("ERROR")
        elif(self.operador == Tipo_OperadorAritmetico.POTENCIA):
            if valorIzq.tipo == Tipo.NUMBER and valorDer.tipo == Tipo.NUMBER:
                return Retorno(valorIzq.valor ** valorDer.valor, Tipo.NUMBER)
            else:
                print("ERROR")
        elif(self.operador == Tipo_OperadorAritmetico.MODULO):
            if valorIzq.tipo == Tipo.NUMBER and valorDer.tipo == Tipo.NUMBER:
                return Retorno(valorIzq.valor % valorDer.valor, Tipo.NUMBER)
            else:
                print("ERROR")
        elif(self.operador == Tipo_OperadorAritmetico.NEGATIVO):
            if valorUnico.tipo == Tipo.NUMBER:
                return Retorno(valorUnico.valor * (-1), Tipo.NUMBER)
            else:
                print("ERROR")
        else:
            print("ERROR")
            
        return Retorno(0, Tipo.ERROR)