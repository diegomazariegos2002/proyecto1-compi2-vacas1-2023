from datetime import datetime
from source.abstracto.Expresion import Expresion
from source.abstracto.Instruccion import Instruccion
from source.abstracto.Retorno import Retorno, RetornoTraduccion, Tipo, TipoDato, TipoVariable
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.simbolo.Simbolo import Simbolo, SimboloTraduccion
from source.simbolo.TablaSimbolos import TablaSimbolos


class AsignacionParametros():

    def __init__(self, nombreVar:str, expresionAsignar:Expresion):
        self.nombreVar = nombreVar
        self.expresionAsignar = expresionAsignar
        self.line = expresionAsignar.line
        self.column = expresionAsignar.column

    def ejecutar(self, tsFuncion: TablaSimbolos, tsAnterior: TablaSimbolos):
        consolaGlobal = Consola()
        expresionRetorno : Retorno = self.expresionAsignar.ejecutar(tsAnterior)

        variable : Simbolo = tsFuncion.buscar(self.nombreVar)
        # validar que todo este bien antes de actualizar la variable
        if variable is None:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la asignacion, variable sin declarar", self.line, self.column, datetime.now()))
            return Excepcion()
        if variable.tipoVariable != expresionRetorno.tipoVariable:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "No se puede asignar un tipo primitivo y un vector", self.line, self.column, datetime.now()))
            return Excepcion()
        
        if variable.tipo != consolaGlobal.relacionarTipos(expresionRetorno.tipo): # validar que los tipos sean iguales
            if variable.tipo == Tipo.ANY: # si la variable es de tipo ANY, se le asigna el tipo de la expresion
                # Actualizando el tipoDato de la variable ANY
                variable.tipoDato = expresionRetorno.tipo
                variable.tipoVariable = expresionRetorno.tipoVariable
            else:   # si no, se lanza un error
                consolaGlobal.set_Excepcion(Excepcion("Error Semantico", f"Asignacion incorrecta, la variable con nombre '{self.nombreVar}' es de tipo [{variable.tipo}] y se le esta tratando de asignar un tipo [{consolaGlobal.relacionarTipos(expresionRetorno.tipo)}]", self.line, self.column, datetime.now()))                
                return Excepcion()
        
        # a un tipo de dato NULL que se le pueda asignar cualquier tipo de dato, cambia al tipo de dato de la expresion
        if variable.tipoDato == TipoDato.NULL:   
            variable.tipoDato = expresionRetorno.tipo
        # si todo esta bien, se actualiza la variable 
        tsFuncion.actualizarVariable(self.nombreVar, expresionRetorno.valor)

    def graficarAst(self):
        consola = Consola()
        nombreNodo = f"instruccion_{str(id(self))}_"
        consola.set_AstGrafico(f"{nombreNodo}[label=\"\\<Instruccion\\>\\nAsignacion Parametros\"];\n")
        nombreNodoId = f"instruccion_{str(id(self))}_id_"
        consola.set_AstGrafico(f"{nombreNodoId}[label=\"\\<Identificador\\>\\n{self.nombreVar}\"];\n")
        consola.set_AstGrafico(f"{nombreNodo} -> {nombreNodoId};\n")
        consola.set_AstGrafico(f"{nombreNodo} -> {self.expresionAsignar.graficarAst()};\n")
        return nombreNodo
    
    def traducir(self, tsFuncion: TablaSimbolos, tsAnterior: TablaSimbolos):
        consolaGlobal = Consola()
        expresionRetorno : RetornoTraduccion = None
        if isinstance(self.expresionAsignar, Expresion):
            expresionRetorno = self.expresionAsignar.traducir(tsAnterior)
        else:
            expresionRetorno = self.expresionAsignar

        variable : SimboloTraduccion = tsFuncion.buscar(self.nombreVar)
        # validar que todo este bien antes de actualizar la variable
        if variable is None:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "Error en la asignacion, variable sin declarar", self.line, self.column, datetime.now()))
            return Excepcion()
        if variable.tipoVariable != expresionRetorno.tipoVariable and variable.tipo != Tipo.ANY:
            consolaGlobal.set_Excepcion(Excepcion("Error Semantico", "No se puede asignar un tipo primitivo y un vector", self.line, self.column, datetime.now()))
            return Excepcion()
        
        if expresionRetorno.tipoVariable == TipoVariable.VECTOR:
            if variable.tipoVariable == TipoVariable.VECTOR:
                if variable.tipo == Tipo.ANY:
                    variable.tipoDato = expresionRetorno.tipo
                    variable.tipoVariable = expresionRetorno.tipoVariable
                    variable.dimensiones = expresionRetorno.dimensiones
                elif variable.tipo == consolaGlobal.relacionarTipos(expresionRetorno.tipo):
                    variable.tipoDato = expresionRetorno.tipo
                    variable.tipoVariable = expresionRetorno.tipoVariable
                    variable.dimensiones = expresionRetorno.dimensiones
                else:   # si no, se lanza un error
                    consolaGlobal.set_Excepcion(Excepcion("Error Semantico", f"Asignacion incorrecta, la variable con nombre '{self.nombreVar}' es de tipo [{variable.tipo}] y se le esta tratando de asignar un tipo [{consolaGlobal.relacionarTipos(expresionRetorno.tipo)}]", self.line, self.column, datetime.now()))                
                    return Excepcion()
            elif variable.tipo == Tipo.ANY:
                if variable.tipo == Tipo.ANY:
                    variable.tipoDato = expresionRetorno.tipo
                    variable.tipoVariable = expresionRetorno.tipoVariable
                    variable.dimensiones = expresionRetorno.dimensiones
                else:   # si no, se lanza un error
                    consolaGlobal.set_Excepcion(Excepcion("Error Semantico", f"Asignacion incorrecta, la variable con nombre '{self.nombreVar}' es de tipo [{variable.tipo}] y se le esta tratando de asignar un tipo [{consolaGlobal.relacionarTipos(expresionRetorno.tipo)}]", self.line, self.column, datetime.now()))                
                    return Excepcion()
        else:
            if variable.tipo != consolaGlobal.relacionarTipos(expresionRetorno.tipo): # validar que los tipos sean iguales
                if variable.tipo == Tipo.ANY: # si la variable es de tipo ANY, se le asigna el tipo de la expresion
                    # Actualizando el tipoDato de la variable ANY
                    variable.tipoDato = expresionRetorno.tipo
                    variable.tipoVariable = expresionRetorno.tipoVariable
                    variable.dimensiones = expresionRetorno.dimensiones
                    if expresionRetorno.tipo == TipoDato.CADENA:
                        variable.inHeap = True
                else:   # si no, se lanza un error
                    consolaGlobal.set_Excepcion(Excepcion("Error Semantico", f"Asignacion incorrecta, la variable con nombre '{self.nombreVar}' es de tipo [{variable.tipo}] y se le esta tratando de asignar un tipo [{consolaGlobal.relacionarTipos(expresionRetorno.tipo)}]", self.line, self.column, datetime.now()))                
                    return Excepcion()
        
        # a un tipo de dato NULL que se le pueda asignar cualquier tipo de dato, cambia al tipo de dato de la expresion
        if variable.tipoDato == TipoDato.NULL:   
            print("ES UN NULL")
            variable.tipoDato = expresionRetorno.tipo
            variable.tipoVariable = expresionRetorno.tipoVariable
            variable.dimensiones = expresionRetorno.dimensiones
        # si todo esta bien, se actualiza la variable 
        cad=consolaGlobal.genComment("Asignacion Variable {}".format(self.nombreVar))
        cad+=expresionRetorno.codigoTraducido
        cad+=consolaGlobal.genAsignacion("STACK[int({})]".format(variable.temporal),expresionRetorno.valor)
        tsFuncion.actualizarVariable(self.nombreVar, expresionRetorno.valor)
        return cad