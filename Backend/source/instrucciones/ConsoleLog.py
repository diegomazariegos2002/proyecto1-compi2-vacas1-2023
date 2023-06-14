
from source.abstracto.Retorno import Retorno, Tipo, TipoDato, TipoVariable
from source.consola_singleton.Consola import Consola
from source.abstracto.Expresion import Expresion
from source.abstracto.Instruccion import Instruccion
from source.errores.Excepcion import Excepcion
from source.simbolo.TablaSimbolos import TablaSimbolos


class ConsoleLog(Instruccion):

    def __init__(self, valor:Expresion, line: int, column: int):
        super().__init__(line, column)
        self.valor : list[Expresion] = valor

    def ejecutar(self, ts: TablaSimbolos):
        consola = Consola()
        for expresion in self.valor:
            retorno:Retorno = expresion.ejecutar(ts)
            if(retorno.tipo != TipoDato.ERROR):
                if(retorno != None):
                    if retorno.tipoVariable == TipoVariable.NORMAL:
                        if(retorno.tipo == TipoDato.CADENA):
                            consola.set_Consola(retorno.valor)
                            continue
                        if(retorno.tipo == TipoDato.NUMERO):
                            consola.set_Consola(str(retorno.valor))
                            continue
                        if(retorno.tipo == TipoDato.BOOLEANO):
                            if(retorno.valor == True):
                                consola.set_Consola("true")
                            elif(retorno.valor == False):
                                consola.set_Consola("false")
                            continue
                        if(retorno.tipo == TipoDato.NULL):
                            consola.set_Consola("null")
                            continue
                        continue
                    elif retorno.tipoVariable == TipoVariable.VECTOR:
                        consola.set_Consola("[")
                        for x in range(0, len(retorno.valor)):
                            if x== 0:
                                if retorno.valor[x].tipoVariable == TipoVariable.VECTOR:
                                    self.agregarVectorConsola(retorno.valor[x])
                                else:
                                    if(retorno.valor[x].tipo == TipoDato.CADENA):
                                        consola.set_Consola(retorno.valor[x].valor)
                                    elif(retorno.valor[x].tipo == TipoDato.NUMERO):
                                        consola.set_Consola(str(retorno.valor[x].valor))
                                    elif(retorno.valor[x].tipo == TipoDato.BOOLEANO):
                                        if(retorno.valor[x].valor == True):
                                            consola.set_Consola("true")
                                        elif(retorno.valor[x].valor == False):
                                            consola.set_Consola("false")
                                    elif(retorno.valor[x].tipo == TipoDato.NULL):
                                        consola.set_Consola("null")
                            else:
                                consola.set_Consola(", ")
                                if retorno.valor[x].tipoVariable == TipoVariable.VECTOR:
                                    self.agregarVectorConsola(retorno.valor[x])
                                else:
                                    if(retorno.valor[x].tipo == TipoDato.CADENA):
                                        consola.set_Consola(retorno.valor[x].valor)
                                    elif(retorno.valor[x].tipo == TipoDato.NUMERO):
                                        consola.set_Consola(str(retorno.valor[x].valor))
                                    elif(retorno.valor[x].tipo == TipoDato.BOOLEANO):
                                        if(retorno.valor[x].valor == True):
                                            consola.set_Consola("true")
                                        elif(retorno.valor[x].valor == False):
                                            consola.set_Consola("false")
                                    elif(retorno.valor[x].tipo == TipoDato.NULL):
                                        consola.set_Consola("null")
                                
                        consola.set_Consola("]")
                continue
            else:
                consola.set_Consola("Error en la ejecucion de la instruccion ConsoleLog, tipo no valido")
                return Excepcion()
        consola.set_Consola("\n")
        return
    
    def graficarAst(self):
        consola = Consola()
        nombreNodo = f"instruccion_{self.line}_{self.column}_{str(id(self))}_"
        consola.set_AstGrafico(f"{nombreNodo}[label=\"\\<Instruccion\\>\\nconsole.log\"];\n")
        if self.valor != None or self.valor != []:        
            cont = 0
            nombreNodoAnterior = ""
            for expresion in self.valor:
                if cont == 0:
                    nombreNodoAnterior = expresion.graficarAst()
                    consola.set_AstGrafico(f"{nombreNodo} -> {nombreNodoAnterior};\n")
                else: 
                    nombreNodoNuevo = expresion.graficarAst()
                    consola.set_AstGrafico(f"{nombreNodoAnterior}-> {nombreNodoNuevo};\n")
                    nombreNodoAnterior = nombreNodoNuevo
                cont+=1 
        return nombreNodo
                
                
    def agregarVectorConsola(self, vectorNuevo: Retorno):
        consola = Consola()
        consola.set_Consola("[")
        for x in range(0, len(vectorNuevo.valor)):
            if x== 0:
                if vectorNuevo.valor[x].tipoVariable == TipoVariable.VECTOR:
                    self.agregarVectorConsola(vectorNuevo.valor[x])
                else:
                    if(vectorNuevo.valor[x].tipo == TipoDato.CADENA):
                        consola.set_Consola(vectorNuevo.valor[x].valor)
                    elif(vectorNuevo.valor[x].tipo == TipoDato.NUMERO):
                        consola.set_Consola(str(vectorNuevo.valor[x].valor))
                    elif(vectorNuevo.valor[x].tipo == TipoDato.BOOLEANO):
                        if(vectorNuevo.valor[x].valor == True):
                            consola.set_Consola("true")
                        elif(vectorNuevo.valor[x].valor == False):
                            consola.set_Consola("false")
                    elif(vectorNuevo.valor[x].tipo == TipoDato.NULL):
                        consola.set_Consola("null")
            else:
                consola.set_Consola(", ")
                if vectorNuevo.valor[x].tipoVariable == TipoVariable.VECTOR:
                    self.agregarVectorConsola(vectorNuevo.valor[x])
                else:
                    if(vectorNuevo.valor[x].tipo == TipoDato.CADENA):
                        consola.set_Consola(vectorNuevo.valor[x].valor)
                    elif(vectorNuevo.valor[x].tipo == TipoDato.NUMERO):
                        consola.set_Consola(str(vectorNuevo.valor[x].valor))
                    elif(vectorNuevo.valor[x].tipo == TipoDato.BOOLEANO):
                        if(vectorNuevo.valor[x].valor == True):
                            consola.set_Consola("true")
                        elif(vectorNuevo.valor[x].valor == False):
                            consola.set_Consola("false")
                    elif(vectorNuevo.valor[x].tipo == TipoDato.NULL):
                        consola.set_Consola("null")
                
        consola.set_Consola("]")