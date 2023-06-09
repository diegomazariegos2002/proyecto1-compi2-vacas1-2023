from datetime import datetime
from typing import Union
from source.abstracto.Retorno import Retorno, TipoDato, TipoVariable
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.abstracto.Expresion import Expresion
from source.abstracto.Instruccion import Instruccion
from source.simbolo.TablaSimbolos import TablaSimbolos
from source.simbolo.Simbolo import Simbolo, TiposSimbolos


class Return(Instruccion):

    def __init__(self, expresionReturn:Expresion, line: int, column: int):
        super().__init__(line, column)
        self.expresionReturn : Expresion = expresionReturn
        self.valorReturn : Retorno = None


    def ejecutar(self, ts: TablaSimbolos):
        """
        RETURN al ejecutar va a devolver una instancia (RETURN) con su expresion 
        """
        consola = Consola()
        self.valorReturn:Retorno = self.expresionReturn.ejecutar(ts)
        
        # validar lo que se tenga que validar
        
        
        return self