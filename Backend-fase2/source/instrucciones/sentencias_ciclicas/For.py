from datetime import datetime
from typing import Union
from source.abstracto.Retorno import Retorno, TipoDato, TipoVariable
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.abstracto.Expresion import Expresion
from source.abstracto.Instruccion import Instruccion
from source.instrucciones.sentencias_de_transferencia.Break import Break
from source.instrucciones.sentencias_de_transferencia.Continue import Continue
from source.instrucciones.sentencias_de_transferencia.Return import Return
from source.simbolo.TablaSimbolos import TablaSimbolos
from source.simbolo.Simbolo import Simbolo, TiposSimbolos


class For(Instruccion):

    def __init__(self, declaracion:Instruccion, condicion:Expresion, asignacion:Instruccion, insEntraFor:list[Instruccion], line: int, column: int):
        super().__init__(line, column)
        self.declaracion : Instruccion = declaracion
        self.condicion : Expresion = condicion
        self.asignacion : Instruccion = asignacion
        self.insEntraFor : list[Instruccion] = insEntraFor

    def ejecutar(self, ts: TablaSimbolos):
        """
        For al ejecutar va a devolver un valor (return)
        """
        consola = Consola()
        newEnviromentFor = TablaSimbolos(ts, "FOR-")
        retornoDeclaracion = None
        retornoCondicion:Retorno = None
        retornoAsignacion = None
        
        # Validaciones
        if self.declaracion != None:
            retornoDeclaracion = self.declaracion.ejecutar(newEnviromentFor)
        if isinstance(retornoDeclaracion, Excepcion):
            return Excepcion()
        if self.condicion == None:
            # ERROR
            consola.set_Excepcion(Excepcion("Error Semantico", "Error la condicion en el for no viene", self.line, self.column, datetime.now()))
            return Excepcion()
        retornoCondicion = self.condicion.ejecutar(newEnviromentFor)
        if retornoCondicion.tipo != TipoDato.BOOLEANO:
            # ERROR
            consola.set_Excepcion(Excepcion("Error Semantico", "Error la condicion en el for no es de tipo boolean", self.line, self.column, datetime.now()))
            return Excepcion()
        
        
        # Ejecutar el for
        while self.condicion.ejecutar(newEnviromentFor).valor:
            newEnviromentForBlk = TablaSimbolos(newEnviromentFor, "FOR-BLOQUE")
            for instruccion in self.insEntraFor:
                resultIns : Union[None, Instruccion, Excepcion]= instruccion.ejecutar(newEnviromentForBlk)
                # Verificar que instancias nos devuelve
                if isinstance(resultIns, Excepcion):
                    return Excepcion()
                if isinstance(resultIns, Return):
                    return resultIns
                if isinstance(resultIns, Break):
                    return
                if isinstance(resultIns, Continue):
                    break
            if self.asignacion != None:
                retornoAsignacion = self.asignacion.ejecutar(newEnviromentFor)
            if isinstance(retornoAsignacion, Excepcion):
                return Excepcion()
        return
    
    def graficarAst(self):
        consola = Consola()
        #declaraciones de los nodos
        nombreNodoPrincipal = f"instruccion_{self.line}_{self.column}_{str(id(self))}_"
        consola.set_AstGrafico(f"{nombreNodoPrincipal}[label=\"\\<Instruccion\\>\\nFor\"];\n")
        
        nombreNodoDeclaracion = f"instruccion_{self.line}_{self.column}_{str(id(self))}_Declaracion_"
        consola.set_AstGrafico(f"{nombreNodoDeclaracion}[label=\"\\<Instruccion\\>\\nDeclaracion\"];\n")
        nombreNodoCondicion = f"instruccion_{self.line}_{self.column}_{str(id(self))}_Condicion_"
        consola.set_AstGrafico(f"{nombreNodoCondicion}[label=\"\\<Instruccion\\>\\nCondicion\"];\n")
        nombreNodoAsignacion = f"instruccion_{self.line}_{self.column}_{str(id(self))}_Asignacion_"
        consola.set_AstGrafico(f"{nombreNodoAsignacion}[label=\"\\<Instruccion\\>\\nAsignacion\"];\n")
        
        nombreNodoBloqueIns = f"instruccion_{self.line}_{self.column}_{str(id(self))}_BloqueInsFor_"
        consola.set_AstGrafico(f"{nombreNodoBloqueIns}[label=\"\\<Bloque\\>\\nInstrucciones For\"];\n")
        
        # uniones de los nodos
        consola.set_AstGrafico(f"{nombreNodoPrincipal}->{nombreNodoAsignacion}\n")
        consola.set_AstGrafico(f"{nombreNodoPrincipal}->{nombreNodoCondicion}\n")
        consola.set_AstGrafico(f"{nombreNodoPrincipal}->{nombreNodoDeclaracion}\n")
        consola.set_AstGrafico(f"{nombreNodoPrincipal}->{nombreNodoBloqueIns}\n")
        
        # Graficando los hijos.
        if self.declaracion != None:
            consola.set_AstGrafico(f"{nombreNodoCondicion}->{self.asignacion.graficarAst()}\n")
        if self.condicion != None:
            consola.set_AstGrafico(f"{nombreNodoCondicion}->{self.condicion.graficarAst()}\n")
        if self.asignacion != None:
            consola.set_AstGrafico(f"{nombreNodoCondicion}->{self.declaracion.graficarAst()}\n")
            
        
        # INSTRUCCIONES FOR
        cont = 0
        nombreNodoAnterior = ""

        for instruccion in self.insEntraFor:
            try:
                if cont == 0:
                    nombreNodoAnterior = instruccion.graficarAst()
                    consola.set_AstGrafico(f"{nombreNodoBloqueIns}->{nombreNodoAnterior};\n")
                else:
                    nombreNodoNuevo = instruccion.graficarAst()
                    consola.set_AstGrafico(f"{nombreNodoAnterior}->{nombreNodoNuevo};\n")
                    nombreNodoAnterior = nombreNodoNuevo
                    
            except Exception as error:
                print("soy un error en for entradas ast: " + error)
            cont += 1
        
        return nombreNodoPrincipal