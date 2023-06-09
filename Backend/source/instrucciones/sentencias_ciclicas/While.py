from datetime import datetime
from typing import Union
from source.abstracto.Retorno import Retorno, TipoDato, TipoVariable
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.abstracto.Expresion import Expresion
from source.abstracto.Instruccion import Instruccion
from source.instrucciones.sentencias_de_transferencia.Break import Break
from source.instrucciones.sentencias_de_transferencia.Continue import Continue
from source.instrucciones.sentencias_de_transferencia.Return import Return
from source.simbolo.TablaSimbolos import TablaSimbolos
from source.simbolo.Simbolo import Simbolo, TiposSimbolos


class While(Instruccion):

    def __init__(self, condicion:Expresion, insEntraWhile:list[Instruccion], line: int, column: int):
        super().__init__(line, column)
        self.condicion : Expresion = condicion
        self.insEntraWhile : list[Instruccion] = insEntraWhile


    def ejecutar(self, ts: TablaSimbolos):
        """
        WHILE al ejecutar va a devolver un valor (return)
        """
        consola = Consola()
        retornoCondicion:Retorno = self.condicion.ejecutar(ts)
        if retornoCondicion.tipo != TipoDato.BOOLEANO:
            # ERROR
            consola.set_Excepcion(Excepcion("Error Semantico", "Error la condicion en el while no es de tipo boolean", self.line, self.column, datetime.now()))
            # nota: no retorna nada entonces cuidado con los ciclos infinitos
            return
        
        while retornoCondicion.valor:
            newEnviroment = TablaSimbolos(ts, "WHILE-")
            for instruccion in self.insEntraWhile:
                retorno : Union[None, Instruccion]= instruccion.ejecutar(newEnviroment)
                # Verificar que instancias nos devuelve
                if isinstance(retorno, Return):
                    return retorno

                if isinstance(retorno, Break):
                    return
                
                if isinstance(retorno, Continue):
                    break
                
                
        
        return