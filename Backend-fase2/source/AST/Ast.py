import os
from source.abstracto.Instruccion import Instruccion
from source.consola_singleton.Consola import Consola
from source.errores.Excepcion import Excepcion
from source.expresiones.nativas.TypeOf import TypeOf
from source.instrucciones.funcion.Function import Function


class Ast:
    """
    Mi clase AST que básicamente voy a utilizar como la clase para almacenar todas mis instrucciones
    que me devuelva la gramática y posteriormente ejecutar en el main (de ahí que tenga dos métodos).
    """

    def __init__(self, instrucciones=None):
        self.instrucciones : list[Instruccion]= None
        if instrucciones is None:
            instrucciones = []

        self.instrucciones = instrucciones

    def ejecutar(self, ts):
        # Primera pasada (Funciones)
        for instruccion in self.instrucciones:
            if isinstance(instruccion, Instruccion):
                if isinstance(instruccion, Function):
                    instruccion.ejecutar(ts)
                    
        # Segunda pasada (Instrucciones)
        for instruccion in self.instrucciones:
            if isinstance(instruccion, Instruccion):
                if not isinstance(instruccion, Function):
                    instruccion.ejecutar(ts)
                    
    def generarGrafico(self):
        consola = Consola()
        # For para armar el ast de las instrucciones
        consola.set_AstGrafico("digraph G { \nnode[shape=box];\nnodeInicio[label=\"<\\ INICIO \\>\"];\n\n");
        cont = 0
        nombreNodoAnterior = ""

        for instruccion in self.instrucciones:
            try:
                if cont == 0:
                    nombreNodoAnterior = instruccion.graficarAst()
                    consola.set_AstGrafico(f"nodeInicio->{nombreNodoAnterior};\n")
                    nombreNodoAnterior = "nodeInicio"
                else:
                    nombreNodoNuevo = instruccion.graficarAst()
                    consola.set_AstGrafico(f"{nombreNodoAnterior}->{nombreNodoNuevo};\n")
                    nombreNodoAnterior = nombreNodoNuevo
                    
            except Exception as error:
                print("soy un error" + error)
            cont += 1
        consola.set_AstGrafico("\n}"); #para cerrar el dot porque es más práctico hacerlo aquí que en la gramática
        self.generar_Archivo("ast", consola.get_AstGrafico(), "dot", "")
        
    def generar_Archivo(self, nombre_archivo, contenido_dot, extension, ruta):
        # Obtener la ruta de la carpeta donde se está ejecutando el script
        ruta_actual = os.getcwd()
        
        # Construir la ruta completa del archivo .dot
        ruta_archivo_dot = os.path.join(ruta_actual+ruta, nombre_archivo + "."+extension)
        
        # Escribir el contenido del archivo .dot
        with open(ruta_archivo_dot, "w") as archivo:
            archivo.write(contenido_dot)
        
        print(f"Archivo {nombre_archivo}.{extension} generado exitosamente en: {ruta_actual}")
            
    # Fase 2
    def traducirAst(self, ts):
        # Añadiendo el encabezado a la traducción
        consola:Consola = Consola()
        codigo3dFunciones = ""
        # Primera pasada (Funciones)
        for instruccion in self.instrucciones:
            if isinstance(instruccion, Instruccion):
                if isinstance(instruccion, Function):
                    res = instruccion.traducir(ts)
                    if not isinstance(res, Excepcion):
                        codigo3dFunciones += res
        
        # Segunda pasada
        # se añade todo lo que va en la main
        
        codigo3dMain = "func main() {\n HP = 0\n SP = 0\n"
        for instruccion in self.instrucciones:
            if isinstance(instruccion, Instruccion):
                if not isinstance(instruccion, Function):
                    res = instruccion.traducir(ts)
                    if not isinstance(res, Excepcion):
                        codigo3dMain += res
        codigo3dMain += "\n}"
        
        codigoUnido:str = consola.get_Encabezado()+codigo3dFunciones+codigo3dMain
        self.generar_Archivo("test", codigoUnido, "go", "\\test\\")
        return codigoUnido
        
    