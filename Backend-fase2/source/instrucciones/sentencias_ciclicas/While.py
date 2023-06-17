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


class While(Instruccion):

    def __init__(self, condicion:Expresion, insEntraWhile:list[Instruccion], line: int, column: int):
        super().__init__(line, column)
        self.condicion : Expresion = condicion
        self.insEntraWhile : list[Instruccion] = insEntraWhile


    def ejecutar(self, ts: TablaSimbolos):
        """
        WHILE al ejecutar va a devolver un valor (return)
        """
        consola = Consola()
        retornoCondicion:Retorno = self.condicion.ejecutar(ts)
        if retornoCondicion.tipo != TipoDato.BOOLEANO:
            # ERROR
            consola.set_Excepcion(Excepcion("Error Semantico", "Error la condicion en el while no es de tipo boolean", self.line, self.column, datetime.now()))
            # nota: no retorna nada entonces cuidado con los ciclos infinitos
            return Excepcion()
                            
        
        while self.condicion.ejecutar(ts).valor:
            newEnviroment = TablaSimbolos(ts, "WHILE-")
            for instruccion in self.insEntraWhile:
                resultIns : Union[None, Instruccion, Excepcion]= instruccion.ejecutar(newEnviroment)
                # Verificar que instancias nos devuelve
                if isinstance(resultIns, Excepcion):
                    return Excepcion()
                if isinstance(resultIns, Return):
                    return resultIns
                if isinstance(resultIns, Break):
                    return
                if isinstance(resultIns, Continue):
                    break
        return
    
    def graficarAst(self):
        consola = Consola()
        nombreNodoInstruccion = f"instruccion_{self.line}_{self.column}_{str(id(self))}_"
        consola.set_AstGrafico(f"{nombreNodoInstruccion}[label=\"\\<Instruccion\\>\\nWhile\"];\n")
        nombreNodoCondicion = f"instruccion_{self.line}_{self.column}_{str(id(self))}_Condicion_"
        consola.set_AstGrafico(f"{nombreNodoCondicion}[label=\"\\<Instruccion\\>\\nCondicion\"];\n")
        nombreNodoBloqueIns = f"instruccion_{self.line}_{self.column}_{str(id(self))}_BloqueInsWhile_"
        consola.set_AstGrafico(f"{nombreNodoBloqueIns}[label=\"\\<Bloque\\>\\nInstrucciones While\"];\n")
        
        consola.set_AstGrafico(f"{nombreNodoCondicion}->{self.condicion.graficarAst()}\n")    
        consola.set_AstGrafico(f"{nombreNodoInstruccion}->{nombreNodoBloqueIns}\n")
        
        # INSTRUCCIONES WHILE
        cont = 0
        nombreNodoAnterior = ""

        for instruccion in self.insEntraWhile:
            try:
                if cont == 0:
                    nombreNodoAnterior = instruccion.graficarAst()
                    consola.set_AstGrafico(f"{nombreNodoBloqueIns}->{nombreNodoAnterior};\n")
                else:
                    nombreNodoNuevo = instruccion.graficarAst()
                    consola.set_AstGrafico(f"{nombreNodoAnterior}->{nombreNodoNuevo};\n")
                    nombreNodoAnterior = nombreNodoNuevo
                    
            except Exception as error:
                print("soy un error en while entradas ast: " + error)
            cont += 1
        
        return nombreNodoInstruccion