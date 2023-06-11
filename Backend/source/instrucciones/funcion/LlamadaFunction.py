from datetime import datetime
from source.abstracto.Expresion import Expresion
from source.abstracto.Instruccion import Instruccion
from source.abstracto.Retorno import Retorno, Tipo
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.instrucciones.funcion.Function import Function
from source.simbolo.Simbolo import Simbolo, TiposSimbolos
from source.simbolo.TablaSimbolos import TablaSimbolos


class LlamadaFuncion(Expresion):

    def __init__(self, idFuncion:str, insEntraParam:list[Expresion], line: int, column: int):
        super().__init__(line, column)
        self.idFuncion = idFuncion
        self.insEntraParam = insEntraParam

    def ejecutar(self, ts: TablaSimbolos):
        consolaGlobal = Consola()
        simboloFuncion : Simbolo = ts.buscar(self.idFuncion)
        # validar que todo este bien antes de llamar a la funcion
        if simboloFuncion is None:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la llamada de funcion, funcion sin declarar", self.line, self.column, datetime.now()))
            return Excepcion()
                
        if simboloFuncion.tipoSimbolo != TiposSimbolos.FUNCTION:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la llamada de funcion, el nombre pertenece a otro tipo que no es funcion", self.line, self.column, datetime.now()))
            return Excepcion()
        
        funcionLLamada : Function = simboloFuncion.valor
        newEnviromentFunction = TablaSimbolos(ts, "FUNCION_"+self.idFuncion+"-")
        
        # validar que la cantidad de parametros sea la misma
        
