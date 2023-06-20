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
    temporales = 0
    labels = 0
    imports = ['fmt', 'math', 'strconv']
    

    def clean_Consola(self):
        self.consola = ""
        self.listaExcepciones = []
        self.listaSimbolos = []
        self.astGrafico = ""
        self.numErrores = 1
        self.errores = ""
        self.simbolos = ""
        self.temporales = 0
        self.labels = 0

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
    
    def set_Simbolo(self, simbolo):
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
        
    # fase 2
    def get_Encabezado(self):
        """
        Método que genera el encabezado del código de 3 direcciones en Go
        """
        codigo_Encabezado = '/* ---- HEADER ----- */\npackage main;\n\n'
        
        codigo_imports = "import(\n"
        for lib in self.imports:
            codigo_imports += f'\t\"{lib}\"\n'
        codigo_imports += "\n)\n\n"
                
        codigo_Encabezado += codigo_imports
        codigo_Encabezado += "var HP, SP float64;\nvar STACK[30101999] float64;\nvar HEAP[30101999] float64;\n\n"
        if self.temporales > 0:
            codigo_Encabezado += 'var ('
            for i in range(self.temporales):
                if i % 10 == 0:
                    codigo_Encabezado += "\n"
                codigo_Encabezado += "t{}".format(i)
                if i < self.temporales-1:
                    codigo_Encabezado += ","
            codigo_Encabezado += " float64 \n)\n"
        
        return codigo_Encabezado
    
    
    def genNewTemp(self):
        cadena = "t{}".format(str(self.temporales))
        self.temporales += 1
        return cadena

    def nuevoTemp(self, temp):
        return {'temp': temp, 'codigo': ""}

    def genNewEtq(self):
        cadena = "L{}".format(str(self.labels))
        self.labels += 1
        return cadena

    def genIf(self, cond, accion):
        if cond == 1:
            return "if true {"+str(accion)+"}\n"
        elif cond == 0:
            return "if false {"+str(accion)+"}\n"
        
        return "if "+str(cond)+" {"+str(accion)+"}\n"

    def genGoto(self, etq):
        return "goto "+etq+";\n"

    def genGoto2(self, etq):
        return "goto "+etq

    def genAsignacion(self, var, val):
        return str(var)+" = "+str(val)+";\n"

    def genPrintC(self, value):
        return "fmt.Printf(\"%c\", int({}))\n".format(str(value))

    def genPrintD(self, value):
        return "fmt.Printf(\"%d\", {})\n".format(str(value))

    def genPrintF(self, value):
        return "fmt.Printf(\"%f\", {})\n".format(str(value))

    def genComment(self, comment):
        return "\n/*{}*/\n".format(str(comment))
    
    def genCompStrings(self, dirCad1, dirCad2):
        """
        si son iguales retorna 1 y si son diferentes retorna 0
        Metodo utilizado para comparar con [===] y [!==] 
        """
        traduRet = ""
        #Labels previas a usar
        lIguales = self.genNewEtq()
        lDiferentes = self.genNewEtq()
        lFin = self.genNewEtq()
        lcontinuar1 = self.genNewEtq()
        lcontinuar2 = self.genNewEtq()
        lcontinuar3 = self.genNewEtq()
        ltrue1 = self.genNewEtq()
        ltrue2 = self.genNewEtq()
        ltrue3 = self.genNewEtq()
        
        #Temporales previos a usar
        tdirCad1 = self.genNewTemp()
        traduRet += self.genAsignacion(tdirCad1, dirCad1)
        tdirCad2 = self.genNewTemp()
        traduRet += self.genAsignacion(tdirCad2, dirCad2)
        trespuesta = self.genNewTemp()
        
        lFor = self.genNewEtq()
        traduRet += f"{lFor}:\n"
        tCharCad1 = self.genNewTemp()
        traduRet += self.genAsignacion(tCharCad1, f"HEAP[int({tdirCad1})]")
        tCharCad2 = self.genNewTemp()
        traduRet += self.genAsignacion(tCharCad2, f"HEAP[int({tdirCad2})]")
        t3 = self.genNewTemp()
        traduRet += self.genIf(f"{tCharCad1}==-1", self.genGoto(ltrue1))
        traduRet += self.genAsignacion(t3, f"0")
        traduRet += self.genGoto(lcontinuar1)
        traduRet += f"{ltrue1}:\n"
        traduRet += self.genAsignacion(t3, f"1")    
        traduRet += f"{lcontinuar1}:\n"
        t4 = self.genNewTemp()
        traduRet += self.genIf(f"{tCharCad2}==-1", self.genGoto(ltrue2))
        traduRet += self.genAsignacion(t4, f"0")
        traduRet += self.genGoto(lcontinuar2)
        traduRet += f"{ltrue2}:\n"
        traduRet += self.genAsignacion(t4, f"1")
        
        traduRet += f"{lcontinuar2}:\n"
        t5 = self.genNewTemp()
        traduRet += self.genIf(f"{t3}==1 && {t4}==1", self.genGoto(ltrue3))
        traduRet += self.genAsignacion(t5, f"0")
        traduRet += self.genGoto(lcontinuar3)
        traduRet += f"{ltrue3}:\n"
        traduRet += self.genAsignacion(t5, f"1")
        
        traduRet += f"{lcontinuar3}:\n"
        traduRet += self.genIf(f"{t5} == 1", self.genGoto(lIguales))
        traduRet += self.genIf(f"{tCharCad1} != {tCharCad2}", self.genGoto(lDiferentes))
        
        traduRet += self.genAsignacion(tdirCad1, f"{tdirCad1} + 1")
        traduRet += self.genAsignacion(tdirCad2, f"{tdirCad2} + 1")
        traduRet += self.genGoto(lFor)
        
        traduRet += f"{lIguales}:\n"
        traduRet += self.genAsignacion(trespuesta, "1")
        traduRet += self.genGoto(lFin)
        
        traduRet += f"{lDiferentes}:\n"
        traduRet += self.genAsignacion(trespuesta, "0")
        
        traduRet += f"{lFin}:\n"
        
        return {'temp': trespuesta, 'codigo': traduRet}
        
    def genCompStrings2(self, dirCad1, dirCad2, comparador):
        """
        Metodo utilizado para comparar con
        [>] [>=] [<] [<=]
        """
        traduRet = ""
        #Labels previas a usar
        lFin = self.genNewEtq()
        ltrue1 = self.genNewEtq()
        
        #Temporales previos a usar
        tdirCad1 = self.genNewTemp()
        traduRet += self.genAsignacion(tdirCad1, dirCad1)
        tdirCad2 = self.genNewTemp()
        traduRet += self.genAsignacion(tdirCad2, dirCad2)
        tCharCad1 = self.genNewTemp()
        tCharCad2 = self.genNewTemp()
        trespuesta = self.genNewTemp()
        
        # Codigo
        traduRet += self.genAsignacion(tCharCad1, f"HEAP[int({tdirCad1})]")
        traduRet += self.genAsignacion(tCharCad2, f"HEAP[int({tdirCad2})]")
        traduRet += self.genIf(f"{tCharCad1}{comparador}{tCharCad2}", self.genGoto(ltrue1))    
        traduRet += self.genAsignacion(trespuesta, f"0")
        traduRet += self.genGoto(lFin)
        traduRet += f"{ltrue1}:\n"
        traduRet += self.genAsignacion(trespuesta, f"1")
        traduRet += f"{lFin}:\n"
        
        return {'temp': trespuesta, 'codigo': traduRet}
        
    ################################################
    #               METODOS DE LOGICAS             #
    ################################################
    def genAnd(self, boolIzq, boolDer):
        """
        Metodo utilizado para generar codigo de la operacion [&&]
        """
        traduRet = ""
        #Labels previas a usar
        lFin = self.genNewEtq()
        ltrue1 = self.genNewEtq()
        #Temporales previos a usar
        tdir1 = self.genNewTemp()
        traduRet += self.genAsignacion(tdir1, boolIzq)
        tdir2 = self.genNewTemp()
        traduRet += self.genAsignacion(tdir2, boolDer)
        
        trespuesta = self.genNewTemp()
        
        # Codigo
        traduRet += self.genIf(f"{tdir1}==1 && {tdir2}==1", self.genGoto(ltrue1))
        traduRet += self.genAsignacion(trespuesta, f"0")
        traduRet += self.genGoto(lFin)
        traduRet += f"{ltrue1}:\n"
        traduRet += self.genAsignacion(trespuesta, f"1")
        traduRet += f"{lFin}:\n"
        
        return {'temp': trespuesta, 'codigo': traduRet}
    
    def genOr(self, boolIzq, boolDer):
        """
        Metodo utilizado para generar codigo de la operacion [||]
        """	
        traduRet = ""
        #Labels previas a usar
        lFin = self.genNewEtq()
        ltrue1 = self.genNewEtq()
        
        #Temporales previos a usar
        tdir1 = self.genNewTemp()
        traduRet += self.genAsignacion(tdir1, boolIzq)
        tdir2 = self.genNewTemp()
        traduRet += self.genAsignacion(tdir2, boolDer)
        trespuesta = self.genNewTemp()
        
        # Codigo
        traduRet += self.genIf(f"{tdir1}==1 || {tdir2}==1", self.genGoto(ltrue1))
        traduRet += self.genAsignacion(trespuesta, f"0")
        traduRet += self.genGoto(lFin)
        traduRet += f"{ltrue1}:\n"
        traduRet += self.genAsignacion(trespuesta, f"1")
        traduRet += f"{lFin}:\n"
        
        return {'temp': trespuesta, 'codigo': traduRet}
        
    def genNot(self, boolUnico):
        """
        Metodo utilizado para generar codigo de la operacion [!]
        """
        traduRet = ""
        #Labels previas a usar
        lFin = self.genNewEtq()
        ltrue1 = self.genNewEtq()
        
        #Temporales previos a usar
        tdir1 = self.genNewTemp()
        traduRet += self.genAsignacion(tdir1, boolUnico)
        trespuesta = self.genNewTemp()
        
        # Codigo
        traduRet += self.genIf(f"{tdir1}==1", self.genGoto(ltrue1))
        traduRet += self.genAsignacion(trespuesta, f"1")
        traduRet += self.genGoto(lFin)
        traduRet += f"{ltrue1}:\n"
        traduRet += self.genAsignacion(trespuesta, f"0")
        traduRet += f"{lFin}:\n"
        
        return {'temp': trespuesta, 'codigo': traduRet}
        
    
        
        
        