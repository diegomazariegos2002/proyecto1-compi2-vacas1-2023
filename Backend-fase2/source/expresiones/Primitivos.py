
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, RetornoTraduccion, Tipo, TipoDato, TipoVariable
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.TablaSimbolos import TablaSimbolos


class Primitivos(Expresion):

    def __init__(self, valor, tipo:Tipo, line: int, column: int):
        super().__init__(line, column)
        self.valor = valor
        self.tipo = tipo
    
    def ejecutar(self, ts: TablaSimbolos) -> Retorno:
        consolaGlobal = Consola()
        if(self.tipo == TipoDato.CADENA):
            return Retorno(self.valor, self.tipo, TipoVariable.NORMAL)
        if(self.tipo == TipoDato.NUMERO):
            return Retorno(self.valor, self.tipo, TipoVariable.NORMAL)
        if(self.tipo == TipoDato.BOOLEANO):
            if(self.valor == "true"):
                return Retorno(True, self.tipo, TipoVariable.NORMAL)
            if(self.valor == "false"):
                return Retorno(False, self.tipo, TipoVariable.NORMAL)
        if(self.tipo == TipoDato.NULL):
            return Retorno(None, self.tipo, TipoVariable.NORMAL)
        if(self.tipo == TipoDato.ANY):
            return Retorno(self.valor, self.tipo, TipoVariable.NORMAL)

        consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Tipo de dato no reconocido", self.line, self.column))
        return Retorno(0, TipoDato.ERROR, TipoVariable.NORMAL)
    
    def graficarAst(self) -> str:
        consola = Consola()
        nombre = f'instruccion_{self.line}_{self.column}_{str(id(self))}_'
        output = ""
        if(self.tipo == TipoDato.CADENA):
            output+= f"{nombre}[label=\"<Primitivo string>\\n\\\"{self.valor}\\\"\"];"
        if(self.tipo == TipoDato.NUMERO):
            output+= f"{nombre}[label=\"<Primitivo number>\\n{self.valor}\"];"
        if(self.tipo == TipoDato.BOOLEANO):
            output+= f"{nombre}[label=\"<Primitivo boolean>\\n{self.valor}\"];"
        if(self.tipo == TipoDato.NULL):
            output+= f"{nombre}[label=\"<Primitivo null>\\n{self.valor}\"];"
        if(self.tipo == TipoDato.ANY):
            output+= f"{nombre}[label=\"<Primitivo any>\\n\\\"{self.valor}\\\"\"];"
        
        consola.set_AstGrafico(output)
        return nombre
    
    def traducir(self, ts):
        consola: Consola = Consola()
        valorRetorno = self.valor
        if self.tipo == TipoDato.BOOLEANO:
            valorRetorno = 1 if self.valor == "true" else 0
            return RetornoTraduccion(valor=valorRetorno,
                                     tipo=TipoDato.BOOLEANO,
                                     tipoVariable=TipoVariable.NORMAL,
                                     codigoTraducido="")
            
        elif self.tipo == TipoDato.NUMERO:
            valorRetorno = float(self.valor)
            return RetornoTraduccion(valor=valorRetorno,
                                     tipo=TipoDato.NUMERO,
                                     tipoVariable=TipoVariable.NORMAL,
                                     codigoTraducido="")
            
        if(self.tipo == TipoDato.NULL):
            # guardado direccion de la cadena
            nuevoTemporal = consola.genNewTemp()
            codigoCadena = consola.genAsignacion(nuevoTemporal, "HP")
            # guardado cadena en el heap
            for i in str("null"):
                value = float(ord(i)) # ascii
                codigoCadena += consola.genAsignacion("HEAP[HP]", value)
                codigoCadena += consola.genAsignacion("HP", "HP + 1")
            # guardado fin de cadena
            codigoCadena += consola.genAsignacion("HEAP[HP]", -1)
            codigoCadena += consola.genAsignacion("HP", "HP + 1")
            return RetornoTraduccion(valor=nuevoTemporal,
                                     tipo=TipoDato.NULL,
                                     tipoVariable=TipoVariable.NORMAL,
                                     codigoTraducido="")
        if(self.tipo == TipoDato.ANY):
            valorRetorno = None
            return RetornoTraduccion(valor=valorRetorno,
                                     tipo=TipoDato.ANY,
                                     tipoVariable=TipoVariable.NORMAL,
                                     codigoTraducido="")
            
        elif self.tipo == TipoDato.CADENA:
            # guardado direccion de la cadena
            nuevoTemporal = consola.genNewTemp()
            codigoCadena = consola.genAsignacion(nuevoTemporal, "HP")
            # guardado cadena en el heap
            for i in str(self.valor):
                value = float(ord(i)) # ascii
                codigoCadena += consola.genAsignacion("HEAP[HP]", value)
                codigoCadena += consola.genAsignacion("HP", "HP + 1")
            # guardado fin de cadena
            codigoCadena += consola.genAsignacion("HEAP[HP]", -1)
            codigoCadena += consola.genAsignacion("HP", "HP + 1")
            return RetornoTraduccion(valor=nuevoTemporal,
                                     tipo=TipoDato.CADENA,
                                     tipoVariable=TipoVariable.NORMAL,
                                     codigoTraducido=codigoCadena)
        
        return RetornoTraduccion(valor=0,
                                 tipo=TipoDato.ERROR,
                                 tipoVariable=TipoVariable.NORMAL,
                                 codigoTraducido="")