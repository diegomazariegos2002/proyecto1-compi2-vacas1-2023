from datetime import datetime
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, RetornoTraduccion, TipoVariable, Tipo_OperadorAritmetico, TipoDato
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.Simbolo import Simbolo, SimboloTraduccion
from source.simbolo.TablaSimbolos import TablaSimbolos

class TypeOf(Expresion):
    def __init__(self, expresion, line, column):
        super().__init__(line, column)
        self.expresion : Expresion = expresion
        
    def ejecutar(self, ts: TablaSimbolos) -> Retorno:
        consolaGlobal = Consola()
        expresionEjecutada:Retorno = self.expresion.ejecutar(ts)

        if expresionEjecutada.tipo == TipoDato.ERROR:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Ocurrio un error ejecutando la expresion.", self.line, self.column, datetime.now()))
            return Retorno(0, TipoDato.ERROR, TipoVariable.NORMAL)
        
        if expresionEjecutada.tipoVariable == TipoVariable.VECTOR:
            return Retorno("Vector", TipoDato.CADENA, TipoVariable.NORMAL)
        elif expresionEjecutada.tipoVariable == TipoVariable.NORMAL:
            if expresionEjecutada.tipo == TipoDato.BOOLEANO:
                return Retorno("boolean", TipoDato.CADENA, TipoVariable.NORMAL)
            elif expresionEjecutada.tipo == TipoDato.CADENA:
                return Retorno("string", TipoDato.CADENA, TipoVariable.NORMAL)
            elif expresionEjecutada.tipo == TipoDato.NUMERO:
                return Retorno("number", TipoDato.CADENA, TipoVariable.NORMAL)
            elif expresionEjecutada.tipo == TipoDato.NULL:
                return Retorno("null", TipoDato.CADENA, TipoVariable.NORMAL)
            
        # ERROR
        consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error algo salio mal en la funcion nativa TypeOf(), revisar parametros de la funcion", self.line, self.column, datetime.now()))
        return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
    
    def graficarAst(self):
        consola = Consola()
        nombreNodo = f"instruccion_{self.line}_{self.column}_{str(id(self))}_"
        consola.set_AstGrafico(f"{nombreNodo}[label=\"\\<Expresion\\>\\ntoFixed\"];\n")
        consola.set_AstGrafico(f"{nombreNodo}->{self.expresion.graficarAst()};\n")
        return nombreNodo
    
    def traducir(self, ts: TablaSimbolos) -> RetornoTraduccion:
        consolaGlobal = Consola()
        expresionTraducida:RetornoTraduccion = self.expresion.traducir(ts)
        cadenaRetorno = ""
        

        if expresionTraducida.tipo == TipoDato.ERROR:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Ocurrio un error ejecutando la expresion.", self.line, self.column, datetime.now()))
            return RetornoTraduccion(valor=0,
                                    tipo=TipoDato.ERROR,
                                    tipoVariable=TipoVariable.NORMAL,
                                    codigoTraducido=consolaGlobal.genComment("La expresion de TypeOf no funciona."))
        
        cadenaRetorno += expresionTraducida.codigoTraducido
        
        if expresionTraducida.tipoVariable == TipoVariable.VECTOR:
            retornoCadena : RetornoTraduccion = self.addCadenaHeap("VECTOR")
            return RetornoTraduccion(valor=retornoCadena.valor,
                                         tipo=TipoDato.CADENA,
                                         tipoVariable=TipoVariable.NORMAL,
                                         codigoTraducido=cadenaRetorno + retornoCadena.codigoTraducido)
        
        elif expresionTraducida.tipoVariable == TipoVariable.NORMAL:
            retornoCadena : RetornoTraduccion = self.addCadenaHeap(consolaGlobal.getTipo(expresionTraducida.tipo).name)
            return RetornoTraduccion(valor=retornoCadena.valor,
                                         tipo=TipoDato.CADENA,
                                         tipoVariable=TipoVariable.NORMAL,
                                         codigoTraducido=cadenaRetorno + retornoCadena.codigoTraducido)
            
        # ERROR
        consolaGlobal.set_Excepcion(Excepcion("Semantico", "Error algo salio mal en la funcion nativa TypeOf(), revisar parametros de la funcion", self.line, self.column, datetime.now()))
        return RetornoTraduccion(valor=0,
                                tipo=TipoDato.ERROR,
                                tipoVariable=TipoVariable.NORMAL,
                                codigoTraducido=consolaGlobal.genComment("La expresion de TypeOf no funciona."))
        
        
    def addCadenaHeap(self, cadena) -> RetornoTraduccion:
        consolaGlobal = Consola()
        retornoMetodo:RetornoTraduccion = None
        cadenaRetorno = ""
        tCadNueva = consolaGlobal.genNewTemp()
        cadenaRetorno += consolaGlobal.genAsignacion(tCadNueva, "HP")
        for charac in cadena:
            cadenaRetorno += consolaGlobal.genAsignacion("HEAP[int(HP)]", "{}".format(ord(charac)))
            cadenaRetorno += consolaGlobal.genAsignacion("HP", "HP + 1")
            
        cadenaRetorno += consolaGlobal.genAsignacion("HEAP[int(HP)]", "-1")
        cadenaRetorno += consolaGlobal.genAsignacion("HP", "HP + 1")
        return RetornoTraduccion(valor=tCadNueva,
                                tipo=TipoDato.CADENA,
                                tipoVariable=TipoVariable.NORMAL,
                                codigoTraducido= consolaGlobal.genComment("Guardando en el Heap TYPEOF") + cadenaRetorno)
        