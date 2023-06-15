from source.errores.Excepcion import Excepcion
from source.simbolo.Simbolo import Simbolo
from source.abstracto.Retorno import TipoDato, Tipo, TipoVariable


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Consola(metaclass=SingletonMeta):
    """
    Aquí anadir todos los métodos necesarios de Consola y así.
    """

    consola = ""
    listaExcepciones : list[Excepcion] = []
    listaSimbolos : list[Simbolo] = []
    astGrafico: str = ""
    numErrores = 1
    errores = ""
    simbolos = ""

    def clean_Consola(self):
        self.consola = ""
        self.listaExcepciones = []
        self.listaSimbolos = []
        self.astGrafico = ""
        self.numErrores = 1
        self.errores = ""
        self.simbolos = ""

    def set_Consola (self, consola):
        self.consola += consola

    def get_Consola (self):
        return self.consola
    
    def set_Excepcion(self, excepcion: Excepcion):
        self.listaExcepciones.append(excepcion)
        fechaHora = str(excepcion.fecha_hora.day) +"/"+str(excepcion.fecha_hora.month) +"/"+str(excepcion.fecha_hora.year) +" " + str(excepcion.fecha_hora.hour) + ":"+ str(excepcion.fecha_hora.minute)
        self.errores += """<tr> 
        <td>""" + str(self.numErrores) + """</td>
        <td>""" + excepcion.descripcion + """</td>
        <td>""" + str(excepcion.linea) + """</td>
        <td>""" + str(excepcion.columna) + """</td>
        <td>""" + fechaHora + """</td>
        </tr>"""
        self.numErrores += 1
        return
    
    def get_Excepciones(self):
        return """
        <table class=\"table table-striped\" border=1 style="width: 75%;margin: 0 auto;" cellpadding ="5">
        <tr class=\"table-dark\">
            <th>No.</th>
            <th>Descripción</th>
            <th>Línea</th>
            <th>Columna</th>
            <th>Fecha y Hora</th>
        </tr>"""+self.errores+ """</table>"""
            
    def obtenerErrores(self):
        return self.listaExcepciones
    
    def set_Simbolo(self, simbolo:Simbolo):
        consolaGlobal: Consola = Consola()
        self.listaSimbolos.append(simbolo)
        self.simbolos += """<tr> 
        <td>""" + simbolo.id + """</td>
        <td>""" + consolaGlobal.tipoDeVariable(simbolo.tipoVariable) + """</td>
        <td>""" + simbolo.nombreAmbito + """</td>
        <td>""" + str(simbolo.linea) + """</td>
        <td>""" + str(simbolo.columna) + """</td>
        </tr>"""
        return

    def get_Simbolos(self):
        return self.listaSimbolos
    
    def obtenerSimbolos(self):
        return """
        <table class=\"table table-striped\" border=1 style="width: 75%;margin: 0 auto;" cellpadding ="5">
        <tr class=\"table-dark\">
            <th>Nombre</th>
            <th>Tipo</th>
            <th>Ámbito</th>
            <th>Fila</th>
            <th>Columna</th>
        </tr>"""+self.simbolos+ """</table>"""
    
    def relacionarTipos(self, tipo:TipoDato):
        if tipo == TipoDato.NUMERO:
            return Tipo.NUMBER
        elif tipo == TipoDato.CADENA:
            return Tipo.STRING
        elif tipo == TipoDato.BOOLEANO:
            return Tipo.BOOLEAN
        elif tipo == TipoDato.NULL:
            return Tipo.NULL
        elif tipo == TipoDato.ERROR:
            return Tipo.ERROR
        elif tipo == TipoDato.ANY:
            return Tipo.ANY
    
    def get_AstGrafico(self):
        return self.astGrafico
    
    def set_AstGrafico(self, ast):
        self.astGrafico += ast
        return
    
    def tipoDeVariable(self, tipoVar: TipoVariable):
        if tipoVar == TipoVariable.NORMAL:
            return "Variable"
        elif tipoVar == TipoVariable.FUNCTION:
            return "Funcion"
        elif tipoVar == TipoVariable.STRUCT:
            return "Struct"
        elif tipoVar == TipoVariable.VECTOR:
            return "Array"