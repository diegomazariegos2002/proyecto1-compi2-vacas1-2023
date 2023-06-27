from datetime import datetime
from source.abstracto.Retorno import Retorno, Tipo, TipoVariable, TipoDato, RetornoTraduccion
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.abstracto.Expresion import Expresion
from source.abstracto.Instruccion import Instruccion
from source.simbolo.TablaSimbolos import TablaSimbolos
from source.simbolo.Simbolo import Simbolo, TiposSimbolos, SimboloTraduccion


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
                
                simbol = Simbolo(TiposSimbolos.VARIABLE, Tipo.ANY, TipoDato.NULL, self.id, None, self.tipoVariable, ts.nombreAmbito, self.line, self.column)
                existeVariable = ts.insertar(self.id, simbol)
                if existeVariable == False:
                    consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                    return Excepcion()
                    
            else:
                simbol = Simbolo(TiposSimbolos.VARIABLE, self.tipo, TipoDato.NULL, self.id, None, self.tipoVariable, ts.nombreAmbito, self.line, self.column)
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
                                simbol = Simbolo(TiposSimbolos.VARIABLE, self.tipo, expreValor.tipo, self.id, expreValor.valor, TipoVariable.NORMAL, ts.nombreAmbito, self.line, self.column)
                                existeVariable = ts.insertar(self.id, simbol)
                                if existeVariable == False:
                                    consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                                    return Excepcion()
                            else:
                                consola.set_Excepcion(Excepcion("Error Semantico", "La declaracion de la variable debe ser de un tipo vector.", self.line, self.column, datetime.now()))
                                return Excepcion()
                        elif expreValor.tipo == TipoDato.NULL:
                            simbol = Simbolo(TiposSimbolos.VARIABLE, self.tipo, expreValor.tipo, self.id, None, TipoVariable.NORMAL, ts.nombreAmbito, self.line, self.column)
                            existeVariable = ts.insertar(self.id, simbol)
                            if existeVariable == False:
                                consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                                return Excepcion()
                        elif consola.relacionarTipos(expreValor.tipo) != Tipo.ERROR and self.tipo == Tipo.ANY:
                            if self.tipoVariable == expreValor.tipoVariable:
                                simbol = Simbolo(TiposSimbolos.VARIABLE, self.tipo, expreValor.tipo, self.id, expreValor.valor, TipoVariable.NORMAL, ts.nombreAmbito, self.line, self.column)
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
                    elif expreValor.tipoVariable == TipoVariable.VECTOR:
                        
                        if consola.relacionarTipos(expreValor.tipo) == self.tipo:
                            if self.tipoVariable == expreValor.tipoVariable:
                                simbol = Simbolo(TiposSimbolos.VARIABLE, self.tipo, expreValor.tipo, self.id, expreValor.valor, TipoVariable.VECTOR, ts.nombreAmbito, self.line, self.column)
                                existeVariable = ts.insertar(self.id, simbol)
                                if existeVariable == False:
                                    consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                                    return Excepcion()
                            else:
                                consola.set_Excepcion(Excepcion("Error Semantico", "La declaracion de la variable debe ser de un tipo primitivo.", self.line, self.column, datetime.now()))
                                return Excepcion()
                        elif expreValor.tipo == TipoDato.NULL:
                            simbol = Simbolo(TiposSimbolos.VARIABLE, self.tipo, expreValor.tipo, self.id, None, TipoVariable.NORMAL, ts.nombreAmbito, self.line, self.column)
                            existeVariable = ts.insertar(self.id, simbol)
                            if existeVariable == False:
                                consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                                return Excepcion()
                        elif consola.relacionarTipos(expreValor.tipo) != Tipo.ERROR and self.tipo == Tipo.ANY:
                            simbol = Simbolo(TiposSimbolos.VARIABLE, self.tipo, expreValor.tipo, self.id, expreValor.valor, TipoVariable.VECTOR, ts.nombreAmbito, self.line, self.column)
                            existeVariable = ts.insertar(self.id, simbol)
                            if existeVariable == False:
                                consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                                return Excepcion()
                        else:
                                consola.set_Excepcion(Excepcion("Error Semantico", "El tipo de la variable y el tipo del dato asignado no coinciden.", self.line, self.column, datetime.now()))
                                return Excepcion()
                else:
                    if expreValor.tipoVariable == TipoVariable.NORMAL:
                        if self.tipoVariable == expreValor.tipoVariable:
                            if consola.relacionarTipos(expreValor.tipo) == Tipo.NULL:
                                simbol = Simbolo(TiposSimbolos.VARIABLE, Tipo.ANY, expreValor.tipo, self.id, expreValor.valor, TipoVariable.NORMAL, ts.nombreAmbito, self.line, self.column)
                                existeVariable = ts.insertar(self.id, simbol)
                                if existeVariable == False:
                                    consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                                    return Excepcion()
                            else:
                                simbol = Simbolo(TiposSimbolos.VARIABLE, consola.relacionarTipos(expreValor.tipo), expreValor.tipo, self.id, expreValor.valor, TipoVariable.NORMAL, ts.nombreAmbito, self.line, self.column)
                                existeVariable = ts.insertar(self.id, simbol)
                                if existeVariable == False:
                                    consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                                    return Excepcion()
                        else:
                                consola.set_Excepcion(Excepcion("Error Semantico", "La declaracion de la variable debe ser de un tipo vector.", self.line, self.column, datetime.now()))
                                return Excepcion()
                    elif expreValor.tipoVariable == TipoVariable.VECTOR:
                        simbol = Simbolo(TiposSimbolos.VARIABLE, consola.relacionarTipos(expreValor.tipo), expreValor.tipo, self.id, expreValor.valor, TipoVariable.VECTOR, ts.nombreAmbito, self.line, self.column)
                        existeVariable = ts.insertar(self.id, simbol)
                        if existeVariable == False:
                            consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                            return Excepcion()
        else:
            consola.set_Excepcion(Excepcion("Error Semantico", "El tipo de dato declarado a una variable no puede ser un error.", self.line, self.column, datetime.now()))
            return Excepcion()
        # consola.set_Consola("Error en la ejecucion de la instruccion ConsoleLog")
        return
    
    
    def graficarAst(self):
        consola = Consola()
        nombreNodo = f"instruccion_{self.line}_{self.column}_{str(id(self))}_"
        consola.set_AstGrafico(f"{nombreNodo}[label=\"\\<Instruccion\\>\\nDeclaracion\"];\n")
        nombreNodoId = f"instruccion_{self.line}_{self.column}_{str(id(self))}_id"
        consola.set_AstGrafico(f"{nombreNodoId}[label=\"\\<Identificador\\>\\n{self.id}\"];\n")
        consola.set_AstGrafico(f"{nombreNodo} -> {nombreNodoId};\n")
        nombreNodoExpresion = ""
        if self.expresion == None:
            nombreNodoExpresion = f"instruccion_{self.line}_{self.column}_{str(id(self))}_expresion"
            if self.tipo == None:        
                #simbol = Simbolo(TiposSimbolos.VARIABLE, Tipo.ANY, TipoDato.NULL, self.id, None, self.tipoVariable, ts.nombreAmbito, self.line, self.column)
                consola.set_AstGrafico(f"{nombreNodoExpresion}[label=\"\\<Expresion\\>\\nnull\"];\n")
                
            else:
                consola.set_AstGrafico(f"{nombreNodoExpresion}[label=\"\\<Expresion\\>\\nnull\"];\n")
        else:
            nombreNodoExpresion = self.expresion.graficarAst()
            
        consola.set_AstGrafico(f"\n{nombreNodo} -> {nombreNodoExpresion};\n")
        return nombreNodo
    
    def traducir(self, ts: TablaSimbolos):
        consola = Consola()
        if self.expresion == None:
            if self.tipo == None:
                t1 = consola.genNewTemp()
                cadena = consola.genComment("Declaracion Variable {}".format(self.id))
                cadena += consola.genAsignacion(t1, "SP + {}".format(ts.size))
                cadena += consola.genAsignacion(
                "STACK[int ({})]".format(t1), "0")
                simbol = SimboloTraduccion(TiposSimbolos.VARIABLE, Tipo.ANY, TipoDato.NULL, self.id, t1, self.tipoVariable, False, ts.nombreAmbito, ts.size, self.line, self.column)
                existeVariable = ts.insertar(self.id, simbol)
                if existeVariable == False:
                    consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                    return Excepcion()
                return cadena
                    
            else:
                t1 = consola.genNewTemp()
                cadena = consola.genComment("Declaracion Variable {}".format(self.id))
                cadena += consola.genAsignacion(t1, "SP + {}".format(ts.size))
                cadena += consola.genAsignacion(
                "STACK[int ({})]".format(t1), "0")
                inHeap = self.tipo == Tipo.STRING or self.tipoVariable == TipoVariable.VECTOR
                simbol = SimboloTraduccion(TiposSimbolos.VARIABLE, self.tipo, TipoDato.NULL, self.id, t1, self.tipoVariable, inHeap, ts.nombreAmbito, ts.size, self.line, self.column)
                simbol.dimensiones = 1
                existeVariable = ts.insertar(self.id, simbol)
                if existeVariable == False:
                    consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                    return Excepcion()
                return cadena
            
        expreValor:RetornoTraduccion = self.expresion.traducir(ts)
        if(expreValor.tipo != Tipo.ERROR):
            if(expreValor != None):
                if self.tipo != None:
                    if expreValor.tipoVariable == TipoVariable.NORMAL:
                        if consola.relacionarTipos(expreValor.tipo) == self.tipo:
                            if self.tipoVariable == expreValor.tipoVariable:
                                t1 = consola.genNewTemp()
                                cadena = consola.genComment("Declaracion Variable {}".format(self.id))
                                cadena += expreValor.codigoTraducido
                                cadena += consola.genAsignacion(t1, "SP + {}".format(ts.size))
                                cadena += consola.genAsignacion(
                                    "STACK[int ({})]".format(t1), expreValor.valor)
                                inHeap = self.tipo == Tipo.STRING
                                simbol = SimboloTraduccion(TiposSimbolos.VARIABLE, self.tipo, expreValor.tipo, self.id, t1, TipoVariable.NORMAL, inHeap, ts.nombreAmbito, ts.size, self.line, self.column)
                                existeVariable = ts.insertar(self.id, simbol)
                                if existeVariable == False:
                                    print("EXCEPCION")
                                    consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                                    return Excepcion()
                                return cadena
                            else:
                                consola.set_Excepcion(Excepcion("Error Semantico", "La declaracion de la variable debe ser de un tipo vector.", self.line, self.column, datetime.now()))
                                return Excepcion()
                        elif expreValor.tipo == TipoDato.NULL:
                            t1 = consola.genNewTemp()
                            cadena = consola.genComment("Declaracion Variable {}".format(self.id))
                            cadena += expreValor.codigoTraducido
                            cadena += consola.genAsignacion(t1, "SP + {}".format(ts.size))
                            cadena += consola.genAsignacion(
                                "STACK[int ({})]".format(t1), "0")
                            inHeap = self.tipo == Tipo.STRING
                            simbol = SimboloTraduccion(TiposSimbolos.VARIABLE, self.tipo, expreValor.tipo, self.id, t1, TipoVariable.NORMAL, inHeap, ts.nombreAmbito, ts.size, self.line, self.column)
                            existeVariable = ts.insertar(self.id, simbol)
                            if existeVariable == False:
                                consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                                return Excepcion()
                            return cadena
                        elif consola.relacionarTipos(expreValor.tipo) != Tipo.ERROR and self.tipo == Tipo.ANY:
                            if self.tipoVariable == expreValor.tipoVariable:
                                t1 = consola.genNewTemp()
                                cadena = consola.genComment("Declaracion Variable {}".format(self.id))
                                cadena += expreValor.codigoTraducido
                                cadena += consola.genAsignacion(t1, "SP + {}".format(ts.size))
                                cadena += consola.genAsignacion(
                                    "STACK[int ({})]".format(t1), expreValor.valor)
                                inHeap = self.tipo == Tipo.STRING
                                simbol = SimboloTraduccion(TiposSimbolos.VARIABLE, self.tipo, expreValor.tipo, self.id, t1, TipoVariable.NORMAL, inHeap, ts.nombreAmbito, ts.size, self.line, self.column)
                                existeVariable = ts.insertar(self.id, simbol)
                                if existeVariable == False:
                                    consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                                    return Excepcion()
                                return cadena
                            else:
                                consola.set_Excepcion(Excepcion("Error Semantico", "La declaracion de la variable debe ser de un tipo vector.", self.line, self.column, datetime.now()))
                                return Excepcion()
                        else:
                                consola.set_Excepcion(Excepcion("Error Semantico", "El tipo de la variable y el tipo del dato asignado no coinciden.", self.line, self.column, datetime.now()))
                                return Excepcion()
                    elif expreValor.tipoVariable == TipoVariable.VECTOR:
                        
                        if consola.relacionarTipos(expreValor.tipo) == self.tipo:
                            if self.tipoVariable == expreValor.tipoVariable:
                                t1 = consola.genNewTemp()
                                cadena = consola.genComment("Declaracion Variable {}".format(self.id))
                                cadena += expreValor.codigoTraducido
                                cadena += consola.genAsignacion(t1, "SP + {}".format(ts.size))
                                cadena += consola.genAsignacion(
                                    "STACK[int ({})]".format(t1), expreValor.valor)
                                simbol = SimboloTraduccion(TiposSimbolos.VARIABLE, self.tipo, expreValor.tipo, self.id, t1, TipoVariable.VECTOR, True, ts.nombreAmbito, ts.size, self.line, self.column)
                                simbol.dimensiones = expreValor.dimensiones
                                existeVariable = ts.insertar(self.id, simbol)
                                if existeVariable == False:
                                    consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                                    return Excepcion()
                                return cadena
                            else:
                                consola.set_Excepcion(Excepcion("Error Semantico", "La declaracion de la variable debe ser de un tipo primitivo.", self.line, self.column, datetime.now()))
                                return Excepcion()
                        elif expreValor.tipo == TipoDato.NULL:
                            t1 = consola.genNewTemp()
                            cadena = consola.genComment("Declaracion Variable {}".format(self.id))
                            cadena += expreValor.codigoTraducido
                            cadena += consola.genAsignacion(t1, "SP + {}".format(ts.size))
                            cadena += consola.genAsignacion(
                                "STACK[int ({})]".format(t1), 0)
                            simbol = SimboloTraduccion(TiposSimbolos.VARIABLE, self.tipo, expreValor.tipo, self.id, t1, TipoVariable.VECTOR, True, ts.nombreAmbito, ts.size, self.line, self.column)
                            simbol.dimensiones = expreValor.dimensiones
                            existeVariable = ts.insertar(self.id, simbol)
                            if existeVariable == False:
                                consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                                return Excepcion()
                            return cadena
                        elif consola.relacionarTipos(expreValor.tipo) != Tipo.ERROR and self.tipo == Tipo.ANY:
                            if self.tipoVariable == expreValor.tipoVariable:
                                t1 = consola.genNewTemp()
                                cadena = consola.genComment("Declaracion Variable {}".format(self.id))
                                cadena += expreValor.codigoTraducido
                                cadena += consola.genAsignacion(t1, "SP + {}".format(ts.size))
                                cadena += consola.genAsignacion(
                                    "STACK[int ({})]".format(t1), expreValor.valor)
                                simbol = SimboloTraduccion(TiposSimbolos.VARIABLE, self.tipo, expreValor.tipo, self.id, t1, TipoVariable.VECTOR, True, ts.nombreAmbito, ts.size, self.line, self.column)
                                simbol.dimensiones = expreValor.dimensiones
                                existeVariable = ts.insertar(self.id, simbol)
                                if existeVariable == False:
                                    consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                                    return Excepcion()
                                return cadena
                            else:
                                consola.set_Excepcion(Excepcion("Error Semantico", "La declaracion de la variable debe ser de un tipo primitivo.", self.line, self.column, datetime.now()))
                                return Excepcion()
                        else:
                                consola.set_Excepcion(Excepcion("Error Semantico", "El tipo de la variable y el tipo del dato asignado no coinciden.", self.line, self.column, datetime.now()))
                                return Excepcion()
                else:
                    if expreValor.tipoVariable == TipoVariable.NORMAL:
                        if self.tipoVariable == expreValor.tipoVariable:
                            if consola.relacionarTipos(expreValor.tipo) == Tipo.NULL:
                                t1 = consola.genNewTemp()
                                cadena = consola.genComment("Declaracion Variable {}".format(self.id))
                                cadena += expreValor.codigoTraducido
                                cadena += consola.genAsignacion(t1, "SP + {}".format(ts.size))
                                cadena += consola.genAsignacion(
                                    "STACK[int ({})]".format(t1), "0")
                                inHeap = self.tipo == Tipo.STRING
                                simbol = SimboloTraduccion(TiposSimbolos.VARIABLE, Tipo.ANY, expreValor.tipo, self.id, t1, TipoVariable.NORMAL, inHeap, ts.nombreAmbito, ts.size, self.line, self.column)
                                existeVariable = ts.insertar(self.id, simbol)
                                if existeVariable == False:
                                    consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                                    return Excepcion()
                                return cadena
                            else:
                                t1 = consola.genNewTemp()
                                cadena = consola.genComment("Declaracion Variable {}".format(self.id))
                                cadena += expreValor.codigoTraducido
                                cadena += consola.genAsignacion(t1, "SP + {}".format(ts.size))
                                cadena += consola.genAsignacion(
                                    "STACK[int ({})]".format(t1), expreValor.valor)
                                inHeap = self.tipo == Tipo.STRING
                                simbol = SimboloTraduccion(TiposSimbolos.VARIABLE, consola.relacionarTipos(expreValor.tipo), expreValor.tipo, self.id, t1, TipoVariable.NORMAL, inHeap, ts.nombreAmbito, ts.size, self.line, self.column)
                                existeVariable = ts.insertar(self.id, simbol)
                                if existeVariable == False:
                                    consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                                    return Excepcion()
                                return cadena
                        else:
                                consola.set_Excepcion(Excepcion("Error Semantico", "La declaracion de la variable debe ser de un tipo vector.", self.line, self.column, datetime.now()))
                                return Excepcion()
                    elif expreValor.tipoVariable == TipoVariable.VECTOR:
                        t1 = consola.genNewTemp()
                        cadena = consola.genComment("Declaracion Variable {}".format(self.id))
                        cadena += expreValor.codigoTraducido
                        cadena += consola.genAsignacion(t1, "SP + {}".format(ts.size))
                        cadena += consola.genAsignacion(
                            "STACK[int ({})]".format(t1), expreValor.valor)
                        simbol = SimboloTraduccion(TiposSimbolos.VARIABLE, consola.relacionarTipos(expreValor.tipo), expreValor.tipo, self.id, t1, TipoVariable.VECTOR, True, ts.nombreAmbito, ts.size, self.line, self.column)
                        simbol.dimensiones = expreValor.dimensiones
                        existeVariable = ts.insertar(self.id, simbol)
                        if existeVariable == False:
                            consola.set_Excepcion(Excepcion("Error Semantico", "La variable con el nombre "+ self.id +" ya existe.", self.line, self.column, datetime.now()))
                            return Excepcion()
                        return cadena
        