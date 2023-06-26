from datetime import datetime
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, RetornoTraduccion, TipoVariable, Tipo_OperadorAritmetico, TipoDato
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.Simbolo import Simbolo, SimboloTraduccion
from source.simbolo.TablaSimbolos import TablaSimbolos

class ToLowerCase(Expresion):
    def __init__(self, nombreVar, line, column):
        super().__init__(line, column)
        self.nombreVar : str = nombreVar
        

    def ejecutar(self, ts: TablaSimbolos) -> Retorno:
        """igual que con toString() no se valida funcion.toLowerCase()"""
        consolaGlobal = Consola()
        idSimbolo : Simbolo = None
        if self.nombreVar != None:
            idSimbolo = ts.buscar(self.nombreVar)
            if idSimbolo == None:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error la variable no existe en llamada a toLowerCase(), no se puede operar expresion con ERROR", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)

            if idSimbolo.tipoDato == TipoDato.ERROR:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error de tipos en toLowerCase(), no se puede operar expresion con ERROR", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
            # si no hay error, se puede operar
            # se verifica el valor primitivo            
            if idSimbolo.tipoDato == TipoDato.CADENA:
                return Retorno(str(idSimbolo.valor).lower(), TipoDato.CADENA, TipoVariable.NORMAL)
        
        # ERROR
        consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error algo salio mal en la funcion nativa ToLowerCase(), revisar parametros de la funcion", self.line, self.column, datetime.now()))
        return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
    
    def graficarAst(self):
        consola = Consola()
        nombreNodo = f"instruccion_{self.line}_{self.column}_{str(id(self))}_"
        consola.set_AstGrafico(f"{nombreNodo}[label=\"\\<Expresion\\>\\ntoLowerCase\"];\n")
        nombreNodoId = f"instruccion_{self.line}_{self.column}_{str(id(self))}_id_"
        consola.set_AstGrafico(f"{nombreNodoId}[label=\"\\<Identificador\\>\\n{self.nombreVar}\"];\n")
        consola.set_AstGrafico(f"{nombreNodo}->{nombreNodoId};\n")
        return nombreNodo
    
    def traducir(self, ts: TablaSimbolos) -> RetornoTraduccion:
        consolaGlobal = Consola()
        variable:SimboloTraduccion = ts.buscar(self.nombreVar)
        cadenaRetorno = ""
        idSimbolo : SimboloTraduccion = None
        if self.nombreVar != None:
            idSimbolo = ts.buscar(self.nombreVar)    
            
            if idSimbolo == None:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error algo salio mal en la funcion nativa toLowerCase(), revisar parametros de la funcion", self.line, self.column, datetime.now()))
                return RetornoTraduccion(valor=0,
                                        tipo=TipoDato.ERROR,
                                        tipoVariable=TipoVariable.NORMAL,
                                        codigoTraducido=consolaGlobal.genComment("La variable con el nombre '"+ self.nombreVar +"' no existe."))
            
            if idSimbolo.tipoDato == TipoDato.ERROR:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error algo salio mal en la funcion nativa toLowerCase(), revisar parametros de la funcion", self.line, self.column, datetime.now()))
                return RetornoTraduccion(valor=0,
                                        tipo=TipoDato.ERROR,
                                        tipoVariable=TipoVariable.NORMAL,
                                        codigoTraducido=consolaGlobal.genComment("La variable con el nombre '"+ self.nombreVar +"' no existe."))
            
            # si no hay error, se puede operar
            # se verifica el valor primitivo            
            if idSimbolo.tipoDato == TipoDato.CADENA:
                tAuxVar = consolaGlobal.genNewTemp()
                tVarDirec = consolaGlobal.genNewTemp()
                cadenaRetorno += consolaGlobal.genAsignacion(tAuxVar, "SP + {}".format(variable.direccion))
                cadenaRetorno += consolaGlobal.genAsignacion(tVarDirec, "STACK[int({})]".format(tAuxVar))
                
                tVarDirec2 = consolaGlobal.genNewTemp()
                tChar = consolaGlobal.genNewTemp()
                tCadNueva = consolaGlobal.genNewTemp()

                lSeguirChar = consolaGlobal.genNewEtq()
                lSeguirChar2 = consolaGlobal.genNewEtq()
                lEscribirChar = consolaGlobal.genNewEtq()
                lFin = consolaGlobal.genNewEtq()
                
                cadenaRetorno += consolaGlobal.genAsignacion(tCadNueva, "HP")
                # Recorriendo la cadena
                cadenaRetorno += consolaGlobal.genAsignacion(tVarDirec2, tVarDirec)
                cadenaRetorno += "{}:\n".format(lSeguirChar)
                cadenaRetorno += consolaGlobal.genAsignacion(tChar,"HEAP[int({})]".format(tVarDirec2))
                cadenaRetorno += consolaGlobal.genIf("{} == -1".format(tChar),consolaGlobal.genGoto2(lFin))
                
                # Verificando si es minuscula
                cadenaRetorno += consolaGlobal.genIf("{} < 65".format(tChar),consolaGlobal.genGoto2(lEscribirChar))
                cadenaRetorno += consolaGlobal.genIf("{} > 90".format(tChar),consolaGlobal.genGoto2(lEscribirChar))
                
                # Convirtiendo a mayuscula
                cadenaRetorno += consolaGlobal.genAsignacion("HEAP[int(HP)]", "{} + 32".format(tChar))
                cadenaRetorno += consolaGlobal.genGoto(lSeguirChar2)
                
                # Escribiendo la mayuscula sin mas
                cadenaRetorno += "{}:\n".format(lEscribirChar)
                cadenaRetorno += consolaGlobal.genAsignacion("HEAP[int(HP)]", "{}".format(tChar))
                
                # Continuando recorrido cadena
                cadenaRetorno += "{}:\n".format(lSeguirChar2)
                cadenaRetorno += consolaGlobal.genAsignacion(tVarDirec2, "{} + 1".format(tVarDirec2))
                cadenaRetorno += consolaGlobal.genAsignacion("HP", "HP + 1")
                cadenaRetorno += consolaGlobal.genGoto(lSeguirChar)
                cadenaRetorno += "{}:\n".format(lFin)
                cadenaRetorno += consolaGlobal.genAsignacion("HEAP[int(HP)]", "-1")
                cadenaRetorno += consolaGlobal.genAsignacion("HP", "HP + 1")
                
                return RetornoTraduccion(valor=tCadNueva,
                                tipo=TipoDato.CADENA,
                                tipoVariable=TipoVariable.NORMAL,
                                codigoTraducido= consolaGlobal.genComment("toLowerCase {}".format(self.nombreVar))+cadenaRetorno)
        
        # ERROR
        consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error algo salio mal en la funcion nativa toLowerCase(), revisar parametros de la funcion", self.line, self.column, datetime.now()))
        return RetornoTraduccion(valor=0,
                                tipo=TipoDato.ERROR,
                                tipoVariable=TipoVariable.NORMAL,
                                codigoTraducido=consolaGlobal.genComment("La variable con el nombre '"+ self.nombreVar +"' no existe."))