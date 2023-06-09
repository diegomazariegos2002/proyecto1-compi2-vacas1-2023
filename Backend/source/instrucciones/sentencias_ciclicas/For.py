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


class For(Instruccion):

    def __init__(self, declaracion:Instruccion, condicion:Expresion, asignacion:Instruccion, insEntraFor:list[Instruccion], line: int, column: int):
        super().__init__(line, column)
        self.declaracion : Instruccion = declaracion
        self.condicion : Expresion = condicion
        self.asignacion : Instruccion = asignacion
        self.insEntraFor : list[Instruccion] = insEntraFor


    def ejecutar(self, ts: TablaSimbolos):
        """
        For al ejecutar va a devolver un valor (return)
        """
        consola = Consola()
        newEnviromentFor = TablaSimbolos(ts, "FOR-")
        retornoDeclaracion = None
        retornoCondicion:Retorno = None
        retornoAsignacion = None
        
        # Validaciones
        if self.declaracion != None:
            retornoDeclaracion = self.declaracion.ejecutar(newEnviromentFor)
        if isinstance(retornoDeclaracion, Excepcion):
            return Excepcion()
        if self.condicion == None:
            # ERROR
            consola.set_Excepcion(Excepcion("Error Semantico", "Error la condicion en el for no viene", self.line, self.column, datetime.now()))
            return Excepcion()
        retornoCondicion = self.condicion.ejecutar(newEnviromentFor)
        if retornoCondicion.tipo != TipoDato.BOOLEANO:
            # ERROR
            consola.set_Excepcion(Excepcion("Error Semantico", "Error la condicion en el for no es de tipo boolean", self.line, self.column, datetime.now()))
            return Excepcion()
        
        
        # Ejecutar el for
        while self.condicion.ejecutar(newEnviromentFor).valor:
            for instruccion in self.insEntraFor:
                resultIns : Union[None, Instruccion, Excepcion]= instruccion.ejecutar(newEnviromentFor)
                # Verificar que instancias nos devuelve
                if isinstance(resultIns, Excepcion):
                    return Excepcion()
                if isinstance(resultIns, Return):
                    return resultIns
                if isinstance(resultIns, Break):
                    return resultIns
                if isinstance(resultIns, Continue):
                    break
            if self.asignacion != None:
                retornoAsignacion = self.asignacion.ejecutar(newEnviromentFor)
            if isinstance(retornoAsignacion, Excepcion):
                return Excepcion()
        return