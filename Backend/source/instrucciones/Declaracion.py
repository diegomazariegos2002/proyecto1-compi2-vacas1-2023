from datetime import datetime
from source.abstracto.Retorno import Retorno, Tipo, TipoVariable, TipoDato
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.abstracto.Expresion import Expresion
from source.abstracto.Instruccion import Instruccion
from source.simbolo.TablaSimbolos import TablaSimbolos
from source.simbolo.Simbolo import Simbolo, TiposSimbolos


class Declaracion(Instruccion):

    def __init__(self, id:str, tipo:Tipo, expresion:Expresion, tipoVariable: TipoVariable, line: int, column: int):
        super().__init__(line, column)
        self.id = id
        self.tipo = tipo
        self.expresion = expresion
        self.tipoVariable = tipoVariable


    def ejecutar(self, ts: TablaSimbolos):
        consola = Consola()
        if self.expresion == None:
            if self.tipo == None:
                simbol = Simbolo(TiposSimbolos.VARIABLE, Tipo.ANY, TipoDato.NULL, self.id, None, TipoVariable.NORMAL)
                existeVariable = ts.insertar(self.id, simbol)
                if existeVariable == False:
                    consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                    return Excepcion()
                    
            else:
                simbol = Simbolo(TiposSimbolos.VARIABLE, self.tipo, TipoDato.NULL, self.id, None, TipoVariable.NORMAL)
                existeVariable = ts.insertar(self.id, simbol)
                if existeVariable == False:
                    consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                    return Excepcion()
            return
        
        expreValor:Retorno = self.expresion.ejecutar(ts)
        if(expreValor.tipo != Tipo.ERROR):
            if(expreValor != None):
                if self.tipo != None:
                    if expreValor.tipoVariable == TipoVariable.NORMAL:
                        if consola.relacionarTipos(expreValor.tipo) == self.tipo:
                            if self.tipoVariable == expreValor.tipoVariable:
                                simbol = Simbolo(TiposSimbolos.VARIABLE, self.tipo, expreValor.tipo, self.id, expreValor.valor, TipoVariable.NORMAL)
                                existeVariable = ts.insertar(self.id, simbol)
                                if existeVariable == False:
                                    consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                                    return Excepcion()
                            else:
                                consola.set_Excepcion(Excepcion("Error Semantico", "La declaracion de la variable debe ser de un tipo primitivo.", self.line, self.column, datetime.now()))
                                return Excepcion()
                        elif expreValor.tipo == TipoDato.NULL:
                            simbol = Simbolo(TiposSimbolos.VARIABLE, self.tipo, expreValor.tipo, self.id, None, TipoVariable.NORMAL)
                            existeVariable = ts.insertar(self.id, simbol)
                            if existeVariable == False:
                                consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                                return Excepcion()
                        elif consola.relacionarTipos(expreValor.tipo) != Tipo.ERROR and self.tipo == Tipo.ANY:
                            simbol = Simbolo(TiposSimbolos.VARIABLE, self.tipo, expreValor.tipo, self.id, expreValor.valor, TipoVariable.NORMAL)
                            existeVariable = ts.insertar(self.id, simbol)
                            if existeVariable == False:
                                consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                                return Excepcion()
                        else:
                                consola.set_Excepcion(Excepcion("Error Semantico", "El tipo de la variable y el tipo del dato asignado no coinciden.", self.line, self.column, datetime.now()))
                                return Excepcion()
                    elif expreValor.tipoVariable == TipoVariable.VECTOR:
                        
                        if consola.relacionarTipos(expreValor.tipo) == self.tipo:
                            if self.tipoVariable == expreValor.tipoVariable:
                                simbol = Simbolo(TiposSimbolos.VARIABLE, self.tipo, expreValor.tipo, self.id, expreValor.valor, TipoVariable.VECTOR)
                                existeVariable = ts.insertar(self.id, simbol)
                                if existeVariable == False:
                                    consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                                    return Excepcion()
                            else:
                                consola.set_Excepcion(Excepcion("Error Semantico", "La declaracion de la variable debe ser de un tipo vector.", self.line, self.column, datetime.now()))
                                return Excepcion()
                        elif consola.relacionarTipos(expreValor.tipo) == Tipo.NULL:
                            simbol = Simbolo(TiposSimbolos.VARIABLE, self.tipo, expreValor.tipo, self.id, None, TipoVariable.NORMAL)
                            existeVariable = ts.insertar(self.id, simbol)
                            if existeVariable == False:
                                consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                                return Excepcion()
                        elif consola.relacionarTipos(expreValor.tipo) != Tipo.ERROR and self.tipo == Tipo.ANY:
                            if consola.relacionarTipos(expreValor.tipo) == self.tipo:
                                simbol = Simbolo(TiposSimbolos.VARIABLE, self.tipo, expreValor.tipo, self.id, expreValor.valor, TipoVariable.VECTOR)
                                existeVariable = ts.insertar(self.id, simbol)
                                if existeVariable == False:
                                    consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                                    return Excepcion()
                            else:
                                consola.set_Excepcion(Excepcion("Error Semantico", "La declaracion de la variable debe ser de un tipo vector.", self.line, self.column, datetime.now()))
                                return Excepcion()
                        else:
                                consola.set_Excepcion(Excepcion("Error Semantico", "El tipo de la variable y el tipo del dato asignado no coinciden.", self.line, self.column, datetime.now()))
                                return Excepcion()
                else:
                    if expreValor.tipoVariable == TipoVariable.NORMAL:
                        if consola.relacionarTipos(expreValor.tipo) == Tipo.NULL:
                            simbol = Simbolo(TiposSimbolos.VARIABLE, Tipo.ANY, expreValor.tipo, self.id, expreValor.valor, TipoVariable.NORMAL)
                            existeVariable = ts.insertar(self.id, simbol)
                            if existeVariable == False:
                                consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                                return Excepcion()
                        else:
                            simbol = Simbolo(TiposSimbolos.VARIABLE, consola.relacionarTipos(expreValor.tipo), expreValor.tipo, self.id, expreValor.valor, TipoVariable.NORMAL)
                            existeVariable = ts.insertar(self.id, simbol)
                            if existeVariable == False:
                                consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                                return Excepcion()
                    elif expreValor.tipoVariable == TipoVariable.VECTOR:
                        simbol = Simbolo(TiposSimbolos.VARIABLE, consola.relacionarTipos(expreValor.tipo), expreValor.tipo, self.id, expreValor.valor, TipoVariable.VECTOR)
                        existeVariable = ts.insertar(self.id, simbol)
                        if existeVariable == False:
                            consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                            return Excepcion()
        else:
            consola.set_Excepcion(Excepcion("Error Semantico", "El tipo de dato declarado a una variable no puede ser un error.", self.line, self.column, datetime.now()))
            return Excepcion()
        # consola.set_Consola("Error en la ejecucion de la instruccion ConsoleLog")
        return