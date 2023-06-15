from source.errores.Excepcion import Excepcion
from source.simbolo.Simbolo import Simbolo
from source.abstracto.Retorno import TipoDato, Tipo


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

    def clean_Consola(self):
        self.consola = ""
        self.listaExcepciones = []
        self.listaSimbolos = []
        self.astGrafico = ""
        self.numErrores = 1
        self.errores = ""

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
        <td>""" + excepcion.linea + """</td>
        <td>""" + excepcion.columna + """</td>
        <td>""" + fechaHora + """</td>
        </tr>"""
        return
    
    def get_Excepciones(self):
        return self.listaExcepciones
    
    def set_Simbolo(self, simbolo):
        self.listaSimbolos.append(simbolo)
        return

    def get_Simbolos(self):
        return self.listaSimbolos
    
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