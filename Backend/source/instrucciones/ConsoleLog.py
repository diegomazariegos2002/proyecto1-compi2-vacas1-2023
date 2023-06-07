
from source.abstracto.Retorno import Retorno, Tipo, TipoDato
from source.consola_singleton.Consola import Consola
from source.abstracto.Expresion import Expresion
from source.abstracto.Instruccion import Instruccion
from source.simbolo.TablaSimbolos import TablaSimbolos


class ConsoleLog(Instruccion):

    def __init__(self, valor:Expresion, line: int, column: int):
        super().__init__(line, column)
        self.valor = valor

    def ejecutar(self, ts: TablaSimbolos):
        consola = Consola()
        for expresion in self.valor:
            retorno:Retorno = expresion.ejecutar(ts)
            if(retorno.tipo != TipoDato.ERROR):
                if(retorno != None):
                    if(retorno.tipo == TipoDato.CADENA):
                        consola.set_Consola(retorno.valor)
                        continue
                    if(retorno.tipo == TipoDato.NUMERO):
                        consola.set_Consola(str(retorno.valor))
                        continue
                    if(retorno.tipo == TipoDato.BOOLEANO):
                        if(retorno.valor == True):
                            consola.set_Consola("true")
                        elif(retorno.valor == False):
                            consola.set_Consola("false")
                        continue
                    if(retorno.tipo == TipoDato.NULL):
                        consola.set_Consola("null")
                        continue
                    if(retorno.tipo == TipoDato.ANY):
                        consola.set_Consola(str(retorno.valor))
                        continue
                    continue
                continue
            # consola.set_Consola("Error en la ejecucion de la instruccion ConsoleLog")
            return