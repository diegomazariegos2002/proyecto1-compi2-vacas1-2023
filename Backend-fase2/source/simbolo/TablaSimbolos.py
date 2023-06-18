from source.simbolo.Simbolo import Simbolo
from source.consola_singleton.Consola import Consola


class TablaSimbolos:

    def __init__(self, anterior, nombreAmbito):
        self.nombreAmbito = nombreAmbito    # nombre del ambito
        self.anterior = anterior    # tabla anterior de simbolos
        self.tablaActual = {}       # diccionario de simbolos
        self.size = 0
        if anterior != None:
            self.size = self.anterior.size

    def insertar(self, id: str, simbolo):
        consolaGlobal = Consola()
        """
        Inserta un símbolo en la tabla actual.

        :param id: El identificador/nombre del símbolo a insertar.
        :param simbolo: El objeto Simbolo a insertar en la tabla.
        :return: None
        """

        if self.buscar_variable(id) == False :
            self.tablaActual[id] = simbolo
            consolaGlobal.set_Simbolo(simbolo)
            self.size += 1
            self.recorrerTablaSimbolos()
            return True
        return False

    def buscar_variable(self, nombre):
        if(self.tablaActual.get(nombre) != None):
            return True
        else:
            return False
        
    def buscar(self, id: str) -> Simbolo:
        ts = self

        while ts is not None:
            exist = ts.tablaActual.get(id)

            if exist is not None:
                return exist

            ts = ts.anterior

        return None

    def buscarActual(self, id: str) -> Simbolo:
        return self.tablaActual.get(id)
    
    def actualizarVariable(self, nombre, valor):
        env = self

        while env != None:
            if(env.tablaActual.get(nombre) != None):
                variable:Simbolo = env.tablaActual.get(nombre)
                variable.valor = valor
                return 
            env = env.anterior

    def recorrerTablaSimbolos(self):
        for simbolo in self.tablaActual:
            valor:Simbolo = self.tablaActual[simbolo]
            print(str(simbolo) +": "+str(valor.id) +" / " + str(valor.tipo)+" / " + str(valor.tipoDato)+" / " + str(valor.tipoVariable))
