from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, Tipo, TipoRelacionales
from source.simbolo.TablaSimbolos import TablaSimbolos

class Relacionales(Expresion):
    def __init__(self, operador, izq, der, line, column):
        super().__init__(line, column)
        self.operador = operador
        self.izq : Expresion = izq
        self.der : Expresion = der
        

    def ejecutar(self, ts: TablaSimbolos) -> Retorno:
            
        valorIzq : Retorno = self.izq.ejecutar(ts)
        if(self.der != None):
            valorDer : Retorno  = self.der.ejecutar(ts)
            
        print(self.operador)
        print(valorIzq.tipo)
        print(valorDer.tipo)

        if(self.operador == TipoRelacionales.MAYORQUE):
            if valorIzq.tipo == Tipo.NUMBER and valorDer.tipo == Tipo.NUMBER:
                if(valorIzq.valor > valorDer.valor):
                    return Retorno(True, Tipo.BOOLEAN)
                else: 
                    return Retorno(False, Tipo.BOOLEAN)
            elif valorIzq.tipo == Tipo.STRING and valorDer.tipo == Tipo.STRING:
                if(valorIzq.valor > valorDer.valor):
                    return Retorno(True, Tipo.BOOLEAN)
                else: 
                    return Retorno(False, Tipo.BOOLEAN)
            else:
                print("ERROR")
        elif(self.operador == TipoRelacionales.MAYORIGUAL):
            if valorIzq.tipo == Tipo.NUMBER and valorDer.tipo == Tipo.NUMBER:
                if(valorIzq.valor >= valorDer.valor):
                    return Retorno(True, Tipo.BOOLEAN)
                else: 
                    return Retorno(False, Tipo.BOOLEAN)
            elif valorIzq.tipo == Tipo.STRING and valorDer.tipo == Tipo.STRING:
                if(valorIzq.valor >= valorDer.valor):
                    return Retorno(True, Tipo.BOOLEAN)
                else: 
                    return Retorno(False, Tipo.BOOLEAN)
            else:
                print("ERROR")
        elif(self.operador == TipoRelacionales.MENORQUE):
            if valorIzq.tipo == Tipo.NUMBER and valorDer.tipo == Tipo.NUMBER:
                if(valorIzq.valor < valorDer.valor):
                    return Retorno(True, Tipo.BOOLEAN)
                else: 
                    return Retorno(False, Tipo.BOOLEAN)
            elif valorIzq.tipo == Tipo.STRING and valorDer.tipo == Tipo.STRING:
                if(valorIzq.valor < valorDer.valor):
                    return Retorno(True, Tipo.BOOLEAN)
                else: 
                    return Retorno(False, Tipo.BOOLEAN)
            else:
                print("ERROR")
        elif(self.operador == TipoRelacionales.MENORIGUAL):
            if valorIzq.tipo == Tipo.NUMBER and valorDer.tipo == Tipo.NUMBER:
                if(valorIzq.valor <= valorDer.valor):
                    return Retorno(True, Tipo.BOOLEAN)
                else: 
                    return Retorno(False, Tipo.BOOLEAN)
            elif valorIzq.tipo == Tipo.STRING and valorDer.tipo == Tipo.STRING:
                if(valorIzq.valor <= valorDer.valor):
                    return Retorno(True, Tipo.BOOLEAN)
                else: 
                    return Retorno(False, Tipo.BOOLEAN)
            else:
                print("ERROR")
        
        elif(self.operador == TipoRelacionales.IGUALACION):
            if valorIzq.tipo == Tipo.NUMBER and valorDer.tipo == Tipo.NUMBER:
                if(valorIzq.valor == valorDer.valor):
                    return Retorno(True, Tipo.BOOLEAN)
                else: 
                    return Retorno(False, Tipo.BOOLEAN)
            elif valorIzq.tipo == Tipo.STRING and valorDer.tipo == Tipo.STRING:
                if(valorIzq.valor == valorDer.valor):
                    return Retorno(True, Tipo.BOOLEAN)
                else: 
                    return Retorno(False, Tipo.BOOLEAN)
            else:
                print("ERROR")
        elif(self.operador == TipoRelacionales.DIFERENTE):
            if valorIzq.tipo == Tipo.NUMBER and valorDer.tipo == Tipo.NUMBER:
                if(valorIzq.valor != valorDer.valor):
                    return Retorno(True, Tipo.BOOLEAN)
                else: 
                    return Retorno(False, Tipo.BOOLEAN)
            elif valorIzq.tipo == Tipo.STRING and valorDer.tipo == Tipo.STRING:
                if(valorIzq.valor != valorDer.valor):
                    return Retorno(True, Tipo.BOOLEAN)
                else: 
                    return Retorno(False, Tipo.BOOLEAN)
            else:
                print("ERROR")

        return Retorno(0, Tipo.ERROR)