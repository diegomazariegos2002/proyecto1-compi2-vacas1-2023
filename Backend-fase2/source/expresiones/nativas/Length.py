from datetime import datetime
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, TipoVariable, TipoDato, RetornoTraduccion
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.Simbolo import Simbolo
from source.simbolo.TablaSimbolos import TablaSimbolos

class Length(Expresion):
    def __init__(self, expresion : Expresion, line, column):
        super().__init__(line, column)
        self.expresion : Expresion = expresion
        
    def ejecutar(self, ts: TablaSimbolos) -> Retorno:
        """
        la funcion nativa ToString() recibe un id de una variable y retorna el valor de la variable en string
        recordar que al menos aquí no he tomado en cuenta
        el retorno de las funciones. [funcion.toString()]
        """
        consolaGlobal = Consola()
        if self.expresion != None:
            expresionEjecutada: Retorno = self.expresion.ejecutar(ts)

            if expresionEjecutada.tipo == TipoDato.ERROR:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Ocurrio un error al ejecutar la expresion para la función Length()", self.line, self.column, datetime.now()))
                return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
            
            # si no hay error, se puede operar
            # se verifica el valor primitivo            
            if expresionEjecutada.tipoVariable == TipoVariable.VECTOR:
                return Retorno(len(expresionEjecutada.valor), TipoDato.NUMERO, TipoVariable.NORMAL)
            elif expresionEjecutada.tipo == TipoDato.CADENA:
                return Retorno(len(expresionEjecutada.valor), TipoDato. NUMERO, TipoVariable.NORMAL)
            
        # ERROR
        consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error algo salio mal en la funcion nativa Length(), revisar parametros de la funcion", self.line, self.column, datetime.now()))
        return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
    
    def graficarAst(self):
        consola = Consola()
        nombreNodo = f"instruccion_{self.line}_{self.column}_{str(id(self))}_"
        consola.set_AstGrafico(f"{nombreNodo}[label=\"\\<Expresion\\>\\nLength\"];\n")
        nombreNodoId = f"instruccion_{self.line}_{self.column}_{str(id(self))}_id_"
        consola.set_AstGrafico(f"{nombreNodoId}[label=\"\\<Identificador\\>\\n{self.expresion.line}\"];\n")
        consola.set_AstGrafico(f"{nombreNodo}->{nombreNodoId};\n")
        return nombreNodo
    
    def traducir(self, ts:TablaSimbolos):
        
        consolaGlobal = Consola()
        if self.expresion != None:
            expresionEjecutada: RetornoTraduccion = self.expresion.traducir(ts)

            if expresionEjecutada.tipo == TipoDato.ERROR:
                # ERROR
                consolaGlobal.set_Excepcion(Excepcion("Semantico", "Ocurrio un error al ejecutar la expresion para la función Length()", self.line, self.column, datetime.now()))
                return RetornoTraduccion(valor=0,
                                tipo=TipoDato.ERROR,
                                tipoVariable=TipoVariable.NORMAL,
                                codigoTraducido="")
            
            # si no hay error, se puede operar
            # se verifica el valor primitivo       
            cadP = ""     
            cadP += expresionEjecutada.codigoTraducido
            if expresionEjecutada.tipoVariable == TipoVariable.VECTOR:
                tvalor = consolaGlobal.genNewTemp() # Genera nuevo tmp longitud
                cadP += consolaGlobal.genAsignacion(tvalor,
                                                "HEAP[int({})]".format(expresionEjecutada.valor))
                return RetornoTraduccion(valor=tvalor,
                                     tipo=TipoDato.NUMERO,
                                     tipoVariable=TipoVariable.NORMAL,
                                     codigoTraducido= consolaGlobal.genComment("FUNCION LENGTH") + cadP)
            elif expresionEjecutada.tipo == TipoDato.CADENA:
                t1 = consolaGlobal.genNewTemp()
                t2 = consolaGlobal.genNewTemp()
                tvalor = consolaGlobal.genNewTemp()

                l1 = consolaGlobal.genNewEtq()
                l2 = consolaGlobal.genNewEtq()
                cadP += consolaGlobal.genAsignacion(t1, expresionEjecutada.valor)
                cadP += "{}:\n".format(l1)
                cadP += consolaGlobal.genAsignacion(t2,
                                            "HEAP[int({})]".format(t1))
                cadP += consolaGlobal.genIf("{} == -1".format(t2),
                                    consolaGlobal.genGoto2(l2))
                cadP += consolaGlobal.genAsignacion(t1, "{} + 1".format(t1))
                cadP += consolaGlobal.genAsignacion(tvalor, "{} + 1".format(tvalor))
                cadP += consolaGlobal.genGoto(l1)
                cadP += "{}:\n".format(l2)
                return RetornoTraduccion(valor=tvalor,
                                     tipo=TipoDato.NUMERO,
                                     tipoVariable=TipoVariable.NORMAL,
                                     codigoTraducido= consolaGlobal.genComment("FUNCION LENGTH") + cadP)
        # ERROR
        consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error algo salio mal en la funcion nativa Length(), revisar parametros de la funcion", self.line, self.column, datetime.now()))
        return RetornoTraduccion(valor=0,
                                tipo=TipoDato.ERROR,
                                tipoVariable=TipoVariable.NORMAL,
                                codigoTraducido="")