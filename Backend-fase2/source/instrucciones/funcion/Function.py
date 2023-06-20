from datetime import datetime
from source.abstracto.Retorno import Retorno, Tipo, TipoVariable, TipoDato
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.abstracto.Expresion import Expresion
from source.abstracto.Instruccion import Instruccion
from source.simbolo.TablaSimbolos import TablaSimbolos
from source.simbolo.Simbolo import Simbolo, TiposSimbolos


class Function(Instruccion):

    def __init__(self, id:str, insParamFunc:list[Instruccion], insEntraFunc:list[Instruccion], line: int, column: int):
        super().__init__(line, column)
        self.id = id
        self.insParamFunc = insParamFunc
        self.insEntraFunc = insEntraFunc
        self.entornoGlobal = None
        
    def ejecutar(self, ts: TablaSimbolos):
        consola = Consola()
        # DECLARACION DE LA VARIABLE FUNCION
        simboloFunc = Simbolo(TiposSimbolos.FUNCTION, Tipo.ANY, TipoDato.ANY, self.id, self, TipoVariable.FUNCTION, ts.nombreAmbito, self.line, self.column)
        existeVariable = ts.insertar(self.id, simboloFunc)
        if existeVariable == False:
            consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe, imposible declarar funcion asi.", self.line, self.column, datetime.now()))
            return Excepcion()
        self.entornoGlobal = ts
        # Podriamos validar que ts si sea el entorno global, pero si veo error lo hago.
        return
    
    def graficarAst(self):
        consola = Consola()
        nombreNodo = f"instruccion_{self.line}_{self.column}_{str(id(self))}_"
        consola.set_AstGrafico(f"{nombreNodo}[label=\"\\<Instruccion\\>\\nFuncion {self.id}\"];\n")
        nombreNodoParametros = f"instruccion_{self.line}_{self.column}_{str(id(self))}_Parametros_"
        consola.set_AstGrafico(f"{nombreNodoParametros}[label=\"\\<Instruccion\\>\\nParametros\"];\n")
        nombreNodoBloqueIns = f"instruccion_{self.line}_{self.column}_{str(id(self))}_BloqueInsFun_"
        consola.set_AstGrafico(f"{nombreNodoBloqueIns}[label=\"\\<Bloque\\>\\nInstrucciones Funcion\"];\n")
        consola.set_AstGrafico(f"{nombreNodo}->{nombreNodoParametros}\n")    
        consola.set_AstGrafico(f"{nombreNodo}->{nombreNodoBloqueIns}\n")
        # PARAMETROS
        cont = 0
        nombreNodoAnterior = ""

        for instruccion in self.insParamFunc:
            try:
                if cont == 0:
                    nombreNodoAnterior = instruccion.graficarAst()
                    consola.set_AstGrafico(f"{nombreNodoParametros}->{nombreNodoAnterior};\n")
                else:
                    nombreNodoNuevo = instruccion.graficarAst()
                    consola.set_AstGrafico(f"{nombreNodoAnterior}->{nombreNodoNuevo};\n")
                    nombreNodoAnterior = nombreNodoNuevo
                    
            except Exception as error:
                print("soy un error en los parametros de funcion ast: " + error)
            cont += 1
        
        # INSTRUCCIONES FUNCION
        cont = 0
        nombreNodoAnterior = ""

        for instruccion in self.insEntraFunc:
            try:
                if cont == 0:
                    nombreNodoAnterior = instruccion.graficarAst()
                    consola.set_AstGrafico(f"{nombreNodoBloqueIns}->{nombreNodoAnterior};\n")
                else:
                    nombreNodoNuevo = instruccion.graficarAst()
                    consola.set_AstGrafico(f"{nombreNodoAnterior}->{nombreNodoNuevo};\n")
                    nombreNodoAnterior = nombreNodoNuevo
                    
            except Exception as error:
                print("soy un error en los parametros de funcion ast: " + error)
            cont += 1
        
        return nombreNodo
    
    def traducir(self, ts: TablaSimbolos):
        consola: Consola = Consola()
        cadenaRetorno = ""
        newEnviromentFunction = TablaSimbolos(ts, "FUNCION_"+self.id+"-")
        self.etqSalida = consola.genNewEtq()
        self.etqReturn = self.etqSalida
        cadenaRetorno += "func {}(){{\n".format(self.id)
        for ins in self.insEntraFunc:
            ins.etqReturn = self.etqReturn
            resIn = ins.traducir(newEnviromentFunction)

            if isinstance(resIn, Excepcion):
                return Excepcion()

            cadenaRetorno += resIn
        cadenaRetorno += consola.genGoto(self.etqSalida)    
        cadenaRetorno += "{}:\n".format(self.etqSalida)
        cadenaRetorno += "return;\n"
        cadenaRetorno += "}\n\n"
        # Si todo esta bien, se agrega la funcion a la tabla de simbolos GLOBAL
        simboloFunc = Simbolo(TiposSimbolos.FUNCTION, Tipo.ANY, TipoDato.ANY, self.id, self, TipoVariable.FUNCTION, ts.nombreAmbito, self.line, self.column)
        existeVariable = ts.insertar(self.id, simboloFunc)
        if existeVariable == False:
            consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe, imposible declarar funcion asi.", self.line, self.column, datetime.now()))
            return Excepcion()
        self.entornoGlobal = ts
        return cadenaRetorno
        
        
        