from datetime import datetime
from typing import Union
from source.abstracto.Expresion import Expresion
from source.abstracto.Instruccion import Instruccion
from source.abstracto.Retorno import Retorno, Tipo, TipoDato, TipoVariable
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.expresiones.Primitivos import Primitivos
from source.instrucciones.Asignacion import Asignacion
from source.instrucciones.AsignacionVec import AsignacionVec
from source.instrucciones.Declaracion import Declaracion
from source.instrucciones.funcion.Function import Function
from source.instrucciones.sentencias_de_transferencia.Return import Return
from source.simbolo.Simbolo import Simbolo, TiposSimbolos
from source.simbolo.TablaSimbolos import TablaSimbolos


class LlamadaFunction(Expresion):

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
            return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
                
        if simboloFuncion.tipoSimbolo != TiposSimbolos.FUNCTION:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la llamada de funcion, el nombre pertenece a otro tipo que no es funcion", self.line, self.column, datetime.now()))
            return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
        
        funcionLLamada : Function = simboloFuncion.valor
        newEnviromentFunction = TablaSimbolos(ts, "FUNCION_"+self.idFuncion+"-")
        
        # validar que la cantidad de parametros sea la misma
        if len(funcionLLamada.insParamFunc) != len(self.insEntraParam):
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la llamada de funcion, la cantidad de parametros no coincide", self.line, self.column, datetime.now()))
            return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
        
        #           ASIGNACION DE PARAMETROS
        # validar que los tipos de parametros sean los mismos y que no existan errores.
        # Esto se hace reutilizando código de la clase Declaracion.py
        # luego Asignacion.py
        if len(funcionLLamada.insParamFunc) > 0:
            for i in range(len(funcionLLamada.insParamFunc)):
                parametroFuncion : Declaracion = funcionLLamada.insParamFunc[i]
                parametroLlamada : Expresion = self.insEntraParam[i]
                
                # Declarando el parametro en la tabla de simbolos de la funcion
                retornoParametroFuncion = parametroFuncion.ejecutar(newEnviromentFunction)
                
                if isinstance(retornoParametroFuncion, Excepcion):
                    # ERROR
                    consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la llamada de funcion, un parametro no se puede asignar", self.line, self.column, datetime.now()))
                    return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
                
                # Asignando el parametro en la tabla de simbolos de la funcion
                asignacionParametroFuncion : Asignacion = Asignacion(funcionLLamada.id, parametroLlamada, 0, 0)  
                retornoAsignacion = asignacionParametroFuncion.ejecutar(newEnviromentFunction)
                if isinstance(retornoAsignacion, Excepcion):
                    # ERROR
                    consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la llamada de funcion, un parametro no se puede asignar", self.line, self.column, datetime.now()))
                    return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
        #          FIN ASIGNACION DE PARAMETROS
        
        # ejecutar las instrucciones de la funcion
        if len(funcionLLamada.insEntraFunc) > 0:
            for i in range(len(funcionLLamada.insEntraFunc)):
                instruccionFuncion : Instruccion = funcionLLamada.insEntraFunc[i]
                retornoInstruccion : Union[Excepcion, Return, None] = instruccionFuncion.ejecutar(newEnviromentFunction)
                
                if isinstance(retornoInstruccion, Excepcion):
                    # ERROR
                    consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la llamada de funcion, una instruccion no se puede ejecutar", self.line, self.column, datetime.now()))
                    return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
                
                if isinstance(retornoInstruccion, Return):
                    expresionRetornada : Expresion = retornoInstruccion.expresionReturn
                    if expresionRetornada == None:
                        return Primitivos(None, TipoDato.NULL, 0, 0)
                    
                    if not isinstance(expresionRetornada, Expresion):
                        # ERROR
                        consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la llamada de funcion, el retorno de la funcion tiene errores", self.line, self.column, datetime.now()))
                        return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
                    
                    # si todo sale bien, yeiii se retorna la expresion para lo que se quiera.
                    return expresionRetornada
                
        return Primitivos(None, TipoDato.NULL, 0, 0)