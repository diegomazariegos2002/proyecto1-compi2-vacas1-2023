
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, Tipo, TipoDato, TipoVariable, RetornoTraduccion
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.TablaSimbolos import TablaSimbolos


class Vector(Expresion):

    def __init__(self, valor, line: int, column: int):
        super().__init__(line, column)
        self.valor = valor
        self.tamano = 0
        
    def ejecutar(self, ts: TablaSimbolos) -> Retorno:
        consolaGlobal = Consola()
        error = False
        esAnyFijo = False
        vectorRetornar = []
        expre: Expresion = None
        
        tipoVector: TipoDato = TipoDato.ANY
        if len(self.valor) > 0:
            primeraExpre : Retorno = self.valor[0].ejecutar(ts)
            tipoVector = primeraExpre.tipo
            
        for expre in self.valor:
            expresionRetorno : Retorno = expre.ejecutar(ts)
            
            if expresionRetorno.tipoVariable == TipoVariable.VECTOR:
                esAnyFijo = True
            
            if expresionRetorno.tipo == TipoDato.ERROR:
                error = True
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Existe un error en un dato del vector.", self.line, self.column))
            vectorRetornar.append(expresionRetorno)
        
        if(esAnyFijo == False):
            for expre in self.valor:
                expresionRetorno : Retorno = expre.ejecutar(ts)
                if(expresionRetorno.tipo != tipoVector):
                    tipoVector = TipoDato.ANY
                    break
        else:
            tipoVector = TipoDato.ANY
        
        if error == True:
            return Retorno(None, TipoDato.ERROR, TipoVariable.NORMAL)

        return Retorno(vectorRetornar, tipoVector, TipoVariable.VECTOR)
    
    def traducir(self, ts):
        consolaGlobal = Consola()
        error = False
        esAnyFijo = False
        vectorRetornar = []
        expre: Expresion = None
        longitud = len(self.valor)
        cadena = ""
        
        tipoVector: TipoDato = TipoDato.ANY
        if len(self.valor) > 0:
            primeraExpre : RetornoTraduccion = self.valor[0].traducir(ts)
            tipoVector = primeraExpre.tipo
            
        for expre in self.valor:
            expresionRetorno : RetornoTraduccion = expre.traducir(ts)
            cadena += expresionRetorno.codigoTraducido
            
            if expresionRetorno.tipoVariable == TipoVariable.VECTOR:
                esAnyFijo = True
            
            if expresionRetorno.tipo == TipoDato.ERROR:
                error = True
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Existe un error en un dato del vector.", self.line, self.column))
            vectorRetornar.append(expresionRetorno)
        
        
        tmp1 = consolaGlobal.genNewTemp()
        tmp2 = consolaGlobal.genNewTemp()
        cadena += consolaGlobal.genAsignacion(tmp1, "HP")
        cadena += consolaGlobal.genAsignacion(tmp2, "HP")
        cadena += consolaGlobal.genAsignacion(tmp2,
                                               "{} + {}".format(tmp2, longitud))
        cadena += consolaGlobal.genAsignacion(
            "HEAP[int({})]".format(tmp1), tmp2)
        
        expresion: RetornoTraduccion = None
        for expresion in vectorRetornar:
            cadena += consolaGlobal.genAsignacion(
                "HEAP[int({})]".format("HP"), expresion.valor)
            cadena += consolaGlobal.genAsignacion("HP", "HP + 1")
        if(esAnyFijo == False):
            for expresion in self.valor:
                if(expresion.tipo != tipoVector):
                    tipoVector = TipoDato.ANY
                    break
        else:
            tipoVector = TipoDato.ANY
        
        if error == True:
            return RetornoTraduccion(valor=0,
                                 tipo=TipoDato.ERROR,
                                 tipoVariable=TipoVariable.NORMAL,
                                 codigoTraducido="")
        return RetornoTraduccion(valor=tmp1,
                                     tipo=tipoVector,
                                     tipoVariable=TipoVariable.VECTOR,
                                     codigoTraducido=cadena,
                                     contenidoVector=vectorRetornar)