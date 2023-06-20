from datetime import datetime
from typing import Union
from source.abstracto.Retorno import Retorno, TipoDato, TipoVariable
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.abstracto.Expresion import Expresion
from source.abstracto.Instruccion import Instruccion
from source.simbolo.TablaSimbolos import TablaSimbolos
from source.simbolo.Simbolo import Simbolo, TiposSimbolos


class Break(Instruccion):

    def __init__(self, line: int, column: int):
        super().__init__(line, column)


    def ejecutar(self, ts: TablaSimbolos):
        """
        BREAK al ejecutar va a devolver una instancia (BREAK)
        """
        
        return self
    
    def graficarAst(self):
        consola = Consola()
        nombreNodo = f"instruccion_{self.line}_{self.column}_{str(id(self))}_"
        consola.set_AstGrafico(f"{nombreNodo}[label=\"\\<Instruccion\\>\\nBreak\"];\n")
        return nombreNodo
    
    def traducir(self, ts: TablaSimbolos):
        consola: Consola = Consola()
        cadenaRetorno = ""
        if self.etqBreak == None:
            consola.set_Excepcion(Excepcion("Error Semantico", "Error sentencia break solo se puede utilizar adentro de un ciclo.", self.line, self.column, datetime.now()))
            return Excepcion()
        cadenaRetorno += consola.genComment("INSTRUCCION BREAK")
        cadenaRetorno += consola.genGoto(self.etqBreak)
        return cadenaRetorno