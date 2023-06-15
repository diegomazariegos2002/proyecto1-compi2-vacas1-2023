from datetime import datetime
from source.abstracto.Retorno import Retorno, Tipo, TipoVariable, TipoDato, EstructuraInterface
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.abstracto.Expresion import Expresion
from source.abstracto.Instruccion import Instruccion
from source.simbolo.TablaSimbolos import TablaSimbolos
from source.simbolo.Simbolo import Simbolo, TiposSimbolos


class InterfaceDefinicion(Instruccion):

    def __init__(self, id:str, insParamFunc:list[EstructuraInterface], line: int, column: int):
        super().__init__(line, column)
        self.id = id
        self.insParamFunc = insParamFunc
        
    def ejecutar(self, ts: TablaSimbolos):
        consola = Consola()
        # DECLARACION DE LA VARIABLE FUNCION
        for x in self.insParamFunc:
            print(x.id + "/" + str(x.tipo))
        simboloFunc = Simbolo(TiposSimbolos.INTERFACE, Tipo.ANY, TipoDato.ANY, self.id, self, TipoVariable.STRUCT)
        existeVariable = ts.insertar(self.id, simboloFunc)
        if existeVariable == False:
            consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe, imposible declarar funcion asi.", self.line, self.column, datetime.now()))
            return Excepcion()
        self.entornoGlobal = ts
        # Podriamos validar que ts si sea el entorno global, pero si veo error lo hago.
        return
    
    def graficarAst(self):
        pass