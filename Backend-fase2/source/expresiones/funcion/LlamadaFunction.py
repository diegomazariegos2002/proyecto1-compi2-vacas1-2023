from datetime import datetime
from typing import Union
from source.abstracto.Expresion import Expresion
from source.expresiones.Acceso import Acceso
from source.abstracto.Instruccion import Instruccion
from source.abstracto.Retorno import Retorno, RetornoTraduccion, Tipo, TipoDato, TipoVariable
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.expresiones.Primitivos import Primitivos
from source.instrucciones.Asignacion import Asignacion
from source.instrucciones.AsignacionVec import AsignacionVec
from source.instrucciones.Declaracion import Declaracion
from source.instrucciones.funcion.AsignacionParametros import AsignacionParametros
from source.instrucciones.funcion.Function import Function
from source.instrucciones.sentencias_de_transferencia.Return import Return
from source.simbolo.Simbolo import Simbolo, SimboloTraduccion, TiposSimbolos
from source.simbolo.TablaSimbolos import TablaSimbolos


class LlamadaFunction(Expresion):

    def __init__(self, idFuncion:str, insEntraParam:list[Expresion], line: int, column: int):
        super().__init__(line, column)
        self.idFuncion = idFuncion
        self.insEntraParam = insEntraParam
        #fase 2
        self.retornoLlamada:RetornoTraduccion = None
        

    def ejecutar(self, ts: TablaSimbolos):
        print("LLAMAN")
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
        # NUEVO AMBITO PARA LA FUNCION LLAMADA
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
                asignacionParametroFuncion : AsignacionParametros = AsignacionParametros(parametroFuncion.id, parametroLlamada)  
                retornoAsignacion = asignacionParametroFuncion.ejecutar(newEnviromentFunction, ts)
                if isinstance(retornoAsignacion, Excepcion):
                    # ERROR
                    consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la llamada de funcion, un parametro no se puede asignar", self.line, self.column, datetime.now()))
                    return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
        #          FIN ASIGNACION DE PARAMETROS
        
        #           EJECTUAR INSTRUCCIONES DE LA FUNCION
        # ESTAS INSTRUCCIONES ESTAN EN EL ENTORNO GLOBAL -> ENTORNO DE LA FUNCION (para agarrar sus parametros)
        # Para esto se crea un entorno auxiliar con el entorno global como padre y el entorno de los parametro como anterior
        newEnviromentFunctionAux = newEnviromentFunction
        newEnviromentFunctionAux.anterior = funcionLLamada.entornoGlobal
        
        if len(funcionLLamada.insEntraFunc) > 0:
            for i in range(len(funcionLLamada.insEntraFunc)):
                instruccionFuncion : Instruccion = funcionLLamada.insEntraFunc[i]
                retornoInstruccion : Union[Excepcion, Return, None] = instruccionFuncion.ejecutar(newEnviromentFunctionAux)
                
                if isinstance(retornoInstruccion, Excepcion):
                    # ERROR
                    consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la llamada de funcion, una instruccion no se puede ejecutar", self.line, self.column, datetime.now()))
                    return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
                
                if isinstance(retornoInstruccion, Return):
                    expresionRetornada : Expresion = retornoInstruccion.expresionReturn
                    if expresionRetornada == None:
                        return Retorno(None, TipoDato.NULL, TipoVariable.NORMAL)
                    
                    if not isinstance(expresionRetornada, Expresion):
                        # ERROR
                        consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la llamada de funcion, el retorno de la funcion tiene errores", self.line, self.column, datetime.now()))
                        return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
                    
                    # si todo sale bien, yeiii se retorna la expresion para lo que se quiera.
                    retExpRetonarda : Retorno = expresionRetornada.ejecutar(newEnviromentFunction)
                    if retExpRetonarda.tipo == TipoDato.ERROR:
                        # ERROR
                        consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la llamada de funcion, el retorno de la funcion tiene errores", self.line, self.column, datetime.now()))
                        return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
                    
                    return retExpRetonarda
        return Retorno(None, TipoDato.NULL, TipoVariable.NORMAL)
    
    def graficarAst(self):
        consola = Consola()
        nombreNodo = f"instruccion_{self.line}_{self.column}_{str(id(self))}_"
        consola.set_AstGrafico(f"{nombreNodo}[label=\"\\<Instruccion\\>\\nLlamada Funcion [{self.idFuncion}]\"];\n")
        nombreNodoParametros = f"instruccion_{self.line}_{self.column}_{str(id(self))}_parametro_"
        consola.set_AstGrafico(f"{nombreNodoParametros}[label=\"\\<Expresion\\>\\nParametros\"];\n")
        consola.set_AstGrafico(f"{nombreNodo}->{nombreNodoParametros};\n")
        # PARAMETROS
        cont = 0
        nombreNodoAnterior = ""

        for instruccion in self.insEntraParam:
            try:
                if cont == 0:
                    nombreNodoAnterior = instruccion.graficarAst()
                    consola.set_AstGrafico(f"{nombreNodoParametros}->{nombreNodoAnterior};\n")
                else:
                    nombreNodoNuevo = instruccion.graficarAst()
                    consola.set_AstGrafico(f"{nombreNodoAnterior}->{nombreNodoNuevo};\n")
                    nombreNodoAnterior = nombreNodoNuevo
                    
            except Exception as error:
                print("soy un error en llamada funcion -> parametros de funcion ast: " + error)
            cont += 1        
        return nombreNodo
    
    def traducir(self, ts: TablaSimbolos):
        consolaGlobal: Consola = Consola()
        cadenaRetorno = ""
        simboloFuncion : SimboloTraduccion = ts.buscar(self.idFuncion)
        # validar que todo este bien antes de llamar a la funcion
        if simboloFuncion is None:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la llamada de funcion, funcion sin declarar", self.line, self.column, datetime.now()))
            return RetornoTraduccion(valor="Error",
                                         tipo=TipoDato.ERROR,
                                         tipoVariable=TipoVariable.NORMAL)
        
        if simboloFuncion.tipoSimbolo != TiposSimbolos.FUNCTION:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la llamada de funcion, el nombre pertenece a otro tipo que no es funcion", self.line, self.column, datetime.now()))
            return RetornoTraduccion(valor="Error",
                                         tipo=TipoDato.ERROR,
                                         tipoVariable=TipoVariable.NORMAL)
        
        funcionLLamada : Function = simboloFuncion.temporal
        # si y solo si la función no ha sido traducida al ser llamada.
        if not funcionLLamada.funcionTraducida:
            funcionLLamada.funcionTraducida = True
            funcionLLamada.entornoGlobal.actualizarVariable(funcionLLamada.id, funcionLLamada)
            # DECLARACION DE PARAMETROS
            # declaración de parametros necesaria para escribir la función.
            # Pero esta declaracion no se añade al código de traducción devuelto
            if len(funcionLLamada.insParamFunc) > 0:
                for i in range(len(funcionLLamada.insParamFunc)):
                    parametroFuncion : Declaracion = funcionLLamada.insParamFunc[i]
                    # Declarando el parametro en la tabla de simbolos de la funcion
                    retornoParametroFuncion:str = parametroFuncion.traducir(funcionLLamada.entornoFuncion)
                    
                    if isinstance(retornoParametroFuncion, Excepcion):
                        # ERROR
                        consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la llamada de funcion, un parametro no se puede asignar", self.line, self.column, datetime.now()))
                        return RetornoTraduccion(valor="Error",
                                         tipo=TipoDato.ERROR,
                                         tipoVariable=TipoVariable.NORMAL)
            
            for simbolo in funcionLLamada.entornoFuncion.tablaActual:
                valor:SimboloTraduccion = funcionLLamada.entornoFuncion.tablaActual[simbolo]
                if valor.tipoDato == TipoDato.NULL:
                    aux : Tipo = valor.tipo
                    valor.tipoDato = consolaGlobal.getTipoDato(aux)
                print(str(valor))
            
            # GENERACIÓN DE CÓDIGO DE INSTRUCCIONES DE LA FUNCIÓN
            funcionLLamada.etqSalida = consolaGlobal.genNewEtq()
            funcionLLamada.etqReturn = funcionLLamada.etqSalida
            consolaGlobal.codigo3dFunciones += "func {}(){{\n".format(funcionLLamada.id)
            for ins in funcionLLamada.insEntraFunc:
                ins.etqReturn = funcionLLamada.etqReturn
                resIn = ins.traducir(funcionLLamada.entornoFuncion)

                if isinstance(resIn, Excepcion):
                    return RetornoTraduccion(valor="Error",
                                         tipo=TipoDato.ERROR,
                                         tipoVariable=TipoVariable.NORMAL)

                consolaGlobal.codigo3dFunciones += resIn
            consolaGlobal.codigo3dFunciones += consolaGlobal.genGoto(funcionLLamada.etqSalida)    
            consolaGlobal.codigo3dFunciones += "{}:\n".format(funcionLLamada.etqSalida)
            consolaGlobal.codigo3dFunciones += "return;\n"
            consolaGlobal.codigo3dFunciones += "}\n\n"
            # actualizando los cambios de la tabla de simbolos de la funcion.
            funcionLLamada.funcionTraducida = True
            funcionLLamada.entornoGlobal.actualizarVariable(funcionLLamada.id, funcionLLamada)
        
        # NUEVO AMBITO PARA LA FUNCION LLAMADA
        newEnviromentFunction = TablaSimbolos(ts, "FUNCION_"+self.idFuncion+"-")
        inicioStackFuncion = newEnviromentFunction.size
        newEnviromentFunction.size += 1 # Se reserva el espacio para el return (0)
        
        
        # validar que la cantidad de parametros sea la misma
        if len(funcionLLamada.insParamFunc) != len(self.insEntraParam):
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la llamada de funcion, la cantidad de parametros no coincide", self.line, self.column, datetime.now()))
            return RetornoTraduccion(valor="Error",
                                         tipo=TipoDato.ERROR,
                                         tipoVariable=TipoVariable.NORMAL)
        
        # EMPEZANDO CUERPO FUNCION
        cadenaRetorno += consolaGlobal.genComment(f"INSTRUCCION DE LLAMADA DE FUNCION {funcionLLamada.id}")
        cadenaRetorno += consolaGlobal.genComment(f"DECLARACION Y ASIGNACION DE PARAMETROS {funcionLLamada.id}")
        
        
        
        #           ASIGNACION DE PARAMETROS
        # validar que los tipos de parametros sean los mismos y que no existan errores.
        # Esto se hace reutilizando código de la clase Declaracion.py
        # luego Asignacion.py
        if len(funcionLLamada.insParamFunc) > 0:
            for i in range(len(funcionLLamada.insParamFunc)):
                parametroFuncion : Declaracion = funcionLLamada.insParamFunc[i]
                # Declarando el parametro en la tabla de simbolos de la funcion
                retornoParametroFuncion:str = parametroFuncion.traducir(newEnviromentFunction)
                parametroLlamada : Expresion = self.insEntraParam[i]
                
                
                if isinstance(retornoParametroFuncion, Excepcion):
                    # ERROR
                    consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la llamada de funcion, un parametro no se puede asignar", self.line, self.column, datetime.now()))
                    return RetornoTraduccion(valor="Error",
                                         tipo=TipoDato.ERROR,
                                         tipoVariable=TipoVariable.NORMAL)
                cadenaRetorno += retornoParametroFuncion
                
                # una llamada de funcion como parametro
                if isinstance(self.insEntraParam[i], LlamadaFunction):
                    ts.size += len(funcionLLamada.insParamFunc)
                    # Asignando el parametro en la tabla de simbolos de la funcion
                    asignacionParametroFuncion : AsignacionParametros = AsignacionParametros(parametroFuncion.id, parametroLlamada)  
                    retornoAsignacion = asignacionParametroFuncion.traducir(newEnviromentFunction, ts)    
                    ts.size -= len(funcionLLamada.insParamFunc)
                # una variable o valor cualquiera como parametro
                else:
                    # Asignando el parametro en la tabla de simbolos de la funcion
                    asignacionParametroFuncion : AsignacionParametros = AsignacionParametros(parametroFuncion.id, parametroLlamada)  
                    retornoAsignacion = asignacionParametroFuncion.traducir(newEnviromentFunction, ts)    
                
                if isinstance(retornoAsignacion, Excepcion):
                    # ERROR
                    consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la llamada de funcion, un parametro no se puede asignar", self.line, self.column, datetime.now()))
                    return RetornoTraduccion(valor="Error",
                                         tipo=TipoDato.ERROR,
                                         tipoVariable=TipoVariable.NORMAL)
                cadenaRetorno += retornoAsignacion
        #          FIN ASIGNACION DE PARAMETROS
        
        # me di cuenta que una forma de que todo funcione si es ejecutando y creando
        # las instrucciones en cada llamada esto por como trabajamos las nativas.
        #           EJECTUAR INSTRUCCIONES DE LA FUNCION
        # ESTAS INSTRUCCIONES ESTAN EN EL ENTORNO GLOBAL -> ENTORNO DE LA FUNCION (para agarrar sus parametros)
        # Para esto se crea un entorno auxiliar con el entorno global como padre y el entorno de los parametro como anterior
        # newEnviromentFunctionAux = newEnviromentFunction
        # newEnviromentFunctionAux.anterior = funcionLLamada.entornoGlobal
        # self.etqSalida = consolaGlobal.genNewEtq()
        # self.etqReturn = self.etqSalida
        # cadenaRetorno += consolaGlobal.genComment(f"INICIO INSTRUCCIONES FUNCION {funcionLLamada.id}")
        # for ins in funcionLLamada.insEntraFunc:
        #     ins.etqReturn = self.etqReturn
        #     resIn = ins.traducir(newEnviromentFunctionAux)

        #     if isinstance(resIn, Excepcion):
        #         return Excepcion()
            
        #     if isinstance(resIn, RetornoTraduccion):
        #         if self.retornoLlamada == None:
        #             self.retornoLlamada = resIn
        #             cadenaRetorno += resIn.codigoTraducido
        #             continue

        #     cadenaRetorno += resIn
        # cadenaRetorno += consolaGlobal.genComment(f"FIN INSTRUCCIONES FUNCION {funcionLLamada.id}")
        # cadenaRetorno += consolaGlobal.genGoto(self.etqSalida)    
        # cadenaRetorno += "{}:\n".format(self.etqSalida)
        
        cadenaRetorno += consolaGlobal.genComment(f"moviendo puntero al ambito del stack de {funcionLLamada.id}")
        cadenaRetorno += consolaGlobal.genAsignacion("SP", "SP + {}".format(inicioStackFuncion))
        cadenaRetorno += "{}();\n".format(funcionLLamada.id)
        temporal = consolaGlobal.genNewTemp()
        temporal2 = consolaGlobal.genNewTemp()
        # Recuperando algún valor de retorno (RETURN)
        cadenaRetorno += consolaGlobal.genComment(f"obteniendo return funcion {funcionLLamada.id}")
        cadenaRetorno += consolaGlobal.genAsignacion(temporal, "SP + 0")
        cadenaRetorno += consolaGlobal.genAsignacion(temporal2,
                                   "STACK[int({})]".format(temporal))
        
        cadenaRetorno += consolaGlobal.genComment(f"restableciendo puntero al ambito anterior de {funcionLLamada.id}")
        cadenaRetorno += consolaGlobal.genAsignacion("SP", "SP - {}".format(inicioStackFuncion))
        
        #Reiniciando temporales de cada variable creada en la función.
        cadenaRetorno += consolaGlobal.genComment(f"reiniciando temporales funcion {funcionLLamada.id}")
        for contador, simbolo in enumerate(funcionLLamada.entornoFuncion.tablaActual):
                valor:SimboloTraduccion = funcionLLamada.entornoFuncion.tablaActual[simbolo]
                temporal = valor.temporal
                temporalAux = consolaGlobal.genNewTemp()
                cadenaRetorno += consolaGlobal.genAsignacion(temporalAux, f"SP + {contador+1}")
                cadenaRetorno += consolaGlobal.genAsignacion(valor.temporal,
                                   "STACK[int({})]".format(temporalAux))
                print("Valor {}: {}".format(contador, valor))
        
        
        # Se retorna el valor de llamada de la funcion.
        return RetornoTraduccion(valor=temporal2,
                                         tipo=funcionLLamada.tipoFuncion,
                                         tipoVariable=funcionLLamada.tipoVariableFuncion,
                                         codigoTraducido=cadenaRetorno)
        
        