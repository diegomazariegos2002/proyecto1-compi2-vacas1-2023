
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, Tipo, TipoDato, TipoVariable
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.TablaSimbolos import TablaSimbolos


class Vector(Expresion):

    def __init__(self, valor, line: int, column: int):
        super().__init__(line, column)
        self.valor = valor
        
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
                if(expre.tipo != tipoVector):
                    tipoVector = TipoDato.ANY
                    break
        else:
            tipoVector = TipoDato.ANY
        
        if error == True:
            return Retorno(None, TipoDato.ERROR, TipoVariable.NORMAL)

        return Retorno(vectorRetornar, tipoVector, Tipo.VECTOR)