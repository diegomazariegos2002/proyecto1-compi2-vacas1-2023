from datetime import datetime
from source.abstracto.Expresion import Expresion
from source.abstracto.Retorno import Retorno, Tipo, TipoDato, TipoVariable
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.Simbolo import Simbolo
from source.simbolo.TablaSimbolos import TablaSimbolos


class Push(Expresion):

    def __init__(self, id:str, expresion:Expresion, line: int, column: int):
        super().__init__(line, column)
        self.id = id
        self.expresion = expresion

    def ejecutar(self, ts: TablaSimbolos):
        consolaGlobal = Consola()
        simboloVec : Simbolo = ts.buscar(self.id)
        # validar que todo este bien antes de llamar a la funcion
        if simboloVec is None:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la llamada de funcion, funcion sin declarar", self.line, self.column, datetime.now()))
            return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
                
        if simboloVec.tipoVariable != TipoVariable.VECTOR:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "La variable para usar la función Push() debe ser un vector.", self.line, self.column, datetime.now()))
            return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
        
        expresionEjecutada = self.expresion.ejecutar(ts)
        if expresionEjecutada.tipo == TipoDato.ERROR:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error al ejecutar la expresión.", self.line, self.column, datetime.now()))
            return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
        
        if simboloVec.tipo == Tipo.ANY:
            simboloVec.valor.append(expresionEjecutada)
            ts.actualizarVariable(self.id, simboloVec.valor)
            return Retorno(len(simboloVec.valor), TipoDato.NUMERO, TipoVariable.NORMAL)
        elif consolaGlobal.relacionarTipos(expresionEjecutada.tipo) != simboloVec.tipo:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "El tipo de la expresion no coincide con el tipo de dato del Vector.", self.line, self.column, datetime.now()))
            return Retorno("Error", TipoDato.ERROR, TipoVariable.NORMAL)
        
        simboloVec.valor.append(expresionEjecutada)
        ts.actualizarVariable(self.id, simboloVec.valor)
        return Retorno(len(simboloVec.valor), TipoDato.NUMERO, TipoVariable.NORMAL)
    
    def graficarAst(self):
        consola = Consola()
        nombreNodo = f"instruccion_{self.line}_{self.column}_{str(id(self))}_"
        consola.set_AstGrafico(f"{nombreNodo}[label=\"\\<Instruccion\\>\\nLlamada Funcion [{self.idFuncion}]\"];\n")
        nombreNodoParametros = f"instruccion_{self.line}_{self.column}_{str(id(self))}_parametro_"
        consola.set_AstGrafico(f"{nombreNodoParametros}[label=\"\\<Expresion\\>\\nParametros\"];\n")
        consola.set_AstGrafico(f"{nombreNodo}->{nombreNodoParametros};\n")
        # PARAMETROS
        cont = 0
        nombreNodoAnterior = ""

        for instruccion in self.insEntraParam:
            try:
                if cont == 0:
                    nombreNodoAnterior = instruccion.graficarAst()
                    consola.set_AstGrafico(f"{nombreNodoParametros}->{nombreNodoAnterior};\n")
                else:
                    nombreNodoNuevo = instruccion.graficarAst()
                    consola.set_AstGrafico(f"{nombreNodoAnterior}->{nombreNodoNuevo};\n")
                    nombreNodoAnterior = nombreNodoNuevo
                    
            except Exception as error:
                print("soy un error en llamada funcion -> parametros de funcion ast: " + error)
            cont += 1        
        return nombreNodo
    
    def traducir(self, ts: TablaSimbolos):
        consola: Consola = Consola()
        cadenaRetorno = ""
        simboloVec : Simbolo = ts.buscar(self.idFuncion)
        