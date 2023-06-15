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
from source.instrucciones.Declaracion import Declaracion
from source.instrucciones.Asignacion import Asignacion
from source.simbolo.TablaSimbolos import TablaSimbolos
from source.simbolo.Simbolo import Simbolo, TiposSimbolos


class ForVec(Instruccion):

    def __init__(self, declaracion:Instruccion, expresionIterar:Expresion, insEntraFor:list[Instruccion], line: int, column: int):
        super().__init__(line, column)
        self.declaracion : Declaracion = declaracion
        self.expresionIterar : Expresion = expresionIterar
        self.insEntraFor : list[Instruccion] = insEntraFor

    def ejecutar(self, ts: TablaSimbolos):
        """
        For al ejecutar va a devolver un valor (return)
        """
        consola = Consola()
        newEnviromentFor = TablaSimbolos(ts, "FOR-")
        retornoDeclaracion = None
        retornoAsignacion = None
        
        # Validaciones
        if self.declaracion != None:
            retornoDeclaracion = self.declaracion.ejecutar(newEnviromentFor)
        if isinstance(retornoDeclaracion, Excepcion):
            return Excepcion()
        
        expresionIterar = self.expresionIterar.ejecutar(newEnviromentFor)
        vectorUtilizar = []
        
        tipoDatoAux = None 
        tipoVariableAux = None
        
        if expresionIterar.tipoVariable == TipoVariable.VECTOR:
            vectorUtilizar = expresionIterar.valor
            tipoDatoAux = expresionIterar.tipo
            tipoVariableAux = expresionIterar.tipoVariable
        else:
            if expresionIterar.tipo == TipoDato.CADENA:
                vectorUtilizar = list(expresionIterar.valor)
                tipoDatoAux = expresionIterar.tipo
                tipoVariableAux = expresionIterar.tipoVariable
            else:
                consola.set_Excepcion(Excepcion("Error Semantico", "La expresion a recorrer en el for no es iterable", self.line, self.column, datetime.now()))
                return Excepcion()
            
        cont = 0
            
        # Ejecutar el for
        while cont < len(vectorUtilizar):
            if expresionIterar.tipoVariable == TipoVariable.NORMAL:
                asignacionAux:Asignacion = Asignacion(self.declaracion.id,Retorno(vectorUtilizar[cont], tipoDatoAux, tipoVariableAux) , self.line, self.column)
                retornoAsignacion = asignacionAux.ejecutar(newEnviromentFor)
            else:
                asignacionAux:Asignacion = Asignacion(self.declaracion.id,vectorUtilizar[cont] , self.line, self.column)
                retornoAsignacion = asignacionAux.ejecutar(newEnviromentFor)
                
            if isinstance(retornoAsignacion, Excepcion):
                return Excepcion()
            newEnviromentForBlk = TablaSimbolos(newEnviromentFor, "FOR-BLOQUE")
            for instruccion in self.insEntraFor:
                resultIns : Union[None, Instruccion, Excepcion]= instruccion.ejecutar(newEnviromentForBlk)
                # Verificar que instancias nos devuelve
                if isinstance(resultIns, Excepcion):
                    return Excepcion()
                if isinstance(resultIns, Return):
                    return resultIns
                if isinstance(resultIns, Break):
                    return
                if isinstance(resultIns, Continue):
                    break
            cont = cont + 1
        return