from datetime import datetime
from typing import Union
from source.abstracto.Retorno import Retorno, RetornoTraduccion, TipoDato, TipoVariable
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.abstracto.Expresion import Expresion
from source.abstracto.Instruccion import Instruccion
from source.simbolo.TablaSimbolos import TablaSimbolos
from source.simbolo.Simbolo import Simbolo, TiposSimbolos


class Return(Instruccion):

    def __init__(self, expresionReturn:Expresion, line: int, column: int):
        super().__init__(line, column)
        self.expresionReturn : Expresion = expresionReturn

    def ejecutar(self, ts: TablaSimbolos):
        """
        RETURN al ejecutar va a devolver una instancia (RETURN) con su expresion 
        """
        consola = Consola()
        
        # validar lo que se tenga que validar
        return self
    
    def graficarAst(self):
        consola = Consola()
        nombreNodo = f"instruccion_{self.line}_{self.column}_{str(id(self))}_"
        consola.set_AstGrafico(f"{nombreNodo}[label=\"\\<Instruccion\\>\\nReturn\"];\n")
        consola.set_AstGrafico(f"{nombreNodo} -> {self.expresionReturn.graficarAst()};\n")
        return nombreNodo
    
    def traducir(self, ts: TablaSimbolos):
        """
        Recordar que aunque parezca que el return retorna algo
        realmente no lo hace, solo se encarga de guardar el valor
        en la posicion del return de la llamada
        y la llamada si es la que se encarga de retornar el valor.
        """
        consola: Consola = Consola()
        cadenaRetorno = ""
        if self.etqReturn == None:
            consola.set_Excepcion(Excepcion("Error Semantico", "Error sentencia return solo se puede utilizar adentro de una funcion.", self.line, self.column, datetime.now()))
            return Excepcion()
        
        cadenaRetorno += consola.genComment("INSTRUCCION RETURN")
        
        if self.expresionReturn == None:
            cadenaRetorno += consola.genGoto(self.etqBreak)
            
            return cadenaRetorno
        else:
            cadenaRetorno += consola.genComment("EXPRESION RETURN")
            retornoExpresion = self.expresionReturn.traducir(ts)
            if isinstance(retornoExpresion, Excepcion):
                consola.set_Excepcion(Excepcion("Error Semantico", "Error sentencia return expresion con error.", self.line, self.column, datetime.now()))
                return Excepcion()
            cadenaRetorno += retornoExpresion.codigoTraducido
            # PROCEDIMIENTO DE GUARDADO DEL RETURN
            t1 = consola.genNewTemp()
            cadenaRetorno += consola.genAsignacion(t1, f"SP + 0") # tecnicamente ahí esta el return
            cadenaRetorno += consola.genAsignacion("STACK[int({})]".format(t1),
                                       retornoExpresion.valor)
            return cadenaRetorno