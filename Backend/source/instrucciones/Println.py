
from source.abstracto.Retorno import Retorno, Tipo
from source.consola_singleton.Consola import Consola
from source.abstracto.Expresion import Expresion
from source.abstracto.Instruccion import Instruccion
from source.simbolo.TablaSimbolos import TablaSimbolos


class Println(Instruccion):

    def __init__(self, valor:Expresion, line: int, column: int):
        super().__init__(line, column)
        self.valor = valor

    def ejecutar(self, ts: TablaSimbolos):
        
        consola = Consola()
        retorno:Retorno = self.valor.ejecutar(ts)
        if(retorno != None):
            if(retorno.tipo != Tipo.ERROR):
                consola.set_Consola(retorno.valor + "\n")

        return super().ejecutar(ts)