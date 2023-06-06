from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, Tipo, TipoLogicas
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
        valorUnico : Retorno = None
        if self.unico != None:
            valorUnico = self.unico.ejecutar(ts)
            if valorUnico.tipo == Tipo.ERROR:
                return 
            
        valorIzq : Retorno = self.izq.ejecutar(ts)
        if(self.der != None):
            valorDer : Retorno  = self.der.ejecutar(ts)

        if(self.operador == TipoLogicas.AND):
            if valorIzq['tipo'] == Tipo.BOOLEAN and valorDer['tipo'] == Tipo.BOOLEAN:
                if(valorIzq['valor'] == True and valorDer['valor'] == True):
                    return Retorno(True, Tipo.BOOLEAN)
                else: 
                    return Retorno(False, Tipo.BOOLEAN)
            else:
                print("ERROR")
        elif(self.tipo == TipoLogicas.OR):
            if valorIzq['tipo'] == Tipo.bool and valorDer['tipo'] == Tipo.bool:
                if(valorIzq['valor'] == False and valorDer['valor'] == False): 
                    return Retorno(False, Tipo.BOOLEAN)
                else:
                    return Retorno(True, Tipo.BOOLEAN)
            else:
                print("ERROR")
        elif(self.tipo == TipoLogicas.NOT):
            if valorIzq['tipo'] == Tipo.bool:
                if(valorIzq['valor'] == True):
                    resultado = {'valor': False, 'tipo': Tipo.bool}
                elif(valorIzq['valor'] == False): 
                    resultado = {'valor': True, 'tipo': Tipo.bool}
            else:
                print("ERROR")

        return Retorno(0, Tipo.ERROR)