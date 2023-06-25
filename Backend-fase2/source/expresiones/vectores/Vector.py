
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, Tipo, TipoDato, TipoVariable, RetornoTraduccion
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.TablaSimbolos import TablaSimbolos


class Vector(Expresion):

    def __init__(self, valor, line: int, column: int):
        super().__init__(line, column)
        self.valor = valor
        self.dimensiones = 1
        
    def ejecutar(self, ts: TablaSimbolos) -> Retorno:
        consolaGlobal = Consola()
        error = False
        esAnyFijo = False
        vectorAux = []
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
            vectorAux.append(expresionRetorno)
        
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

        return Retorno(vectorAux, tipoVector, TipoVariable.VECTOR)
    
    def traducir(self, ts):
        consolaGlobal = Consola()
        error = False
        vectorAux = []
        expre: Expresion = None
        longitud = len(self.valor)
        cadena = ""
        yaEncontreVector = False
        
        tipoVector: TipoDato = TipoDato.ANY
            
        for expre in self.valor: # En este for ejecuto cada expresion y voy agregando al vector auxiliar
            expresionRetorno : RetornoTraduccion = expre.traducir(ts)
            cadena += expresionRetorno.codigoTraducido
            
            if expresionRetorno.tipoVariable == TipoVariable.VECTOR and yaEncontreVector == False:
                yaEncontreVector = True
                self.dimensiones = self.dimensiones + expresionRetorno.dimensiones
            
            if expresionRetorno.tipo == TipoDato.ERROR:
                error = True
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Existe un error en un dato del vector.", self.line, self.column))
            vectorAux.append(expresionRetorno)
            
        tipoVector = vectorAux[0].tipo
        
        expresion: RetornoTraduccion = None
        
        for expresion in vectorAux:
            if(expresionRetorno.tipo != tipoVector):
                    tipoVector = TipoDato.ANY
                    break 
        
        
        tmp1 = consolaGlobal.genNewTemp() # Temporal que guarda la dirección del vector en el heap
        cadena += consolaGlobal.genComment("----CREACION DE VECTOR----")
        cadena += consolaGlobal.genAsignacion(tmp1, "HP")
        cadena += consolaGlobal.genAsignacion(
            "HEAP[int({})]".format("HP"), longitud)
        cadena += consolaGlobal.genAsignacion("HP", "HP + 1")
        
        for expresion in vectorAux:
            cadena += consolaGlobal.genAsignacion(
                "HEAP[int({})]".format("HP"), expresion.valor)
            cadena += consolaGlobal.genAsignacion("HP", "HP + 1")
        
        if error == True:
            return RetornoTraduccion(valor=0,
                                tipo=TipoDato.ERROR,
                                tipoVariable=TipoVariable.NORMAL,
                                codigoTraducido="")
        
            
        return RetornoTraduccion(valor=tmp1,
                                tipo=tipoVector,
                                tipoVariable=TipoVariable.VECTOR,
                                codigoTraducido=cadena,
                                contenidoVector=vectorAux,
                                dimensiones = self.dimensiones)