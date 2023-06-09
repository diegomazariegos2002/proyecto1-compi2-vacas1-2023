from datetime import datetime
from typing import Union
from source.abstracto.Retorno import Retorno, TipoDato, TipoVariable
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.abstracto.Expresion import Expresion
from source.abstracto.Instruccion import Instruccion
from source.simbolo.TablaSimbolos import TablaSimbolos
from source.simbolo.Simbolo import Simbolo, TiposSimbolos


class Continue(Instruccion):
    def __init__(self, line: int, column: int):
        super().__init__(line, column)


    def ejecutar(self, ts: TablaSimbolos):
        """
        CONTINUE al ejecutar va a devolver una instancia (CONTINUE)
        """
        
        return self