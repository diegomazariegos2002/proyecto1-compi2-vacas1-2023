from source.simbolo.Simbolo import Simbolo


class TablaSimbolos:

    def __init__(self, anterior, nombreAmbito):
        self.nombreAmbito = nombreAmbito    # nombre del ambito
        self.anterior = anterior    # tabla anterior de simbolos
        self.tablaActual = {}       # diccionario de simbolos

    def insertar(self, id: str, simbolo: Simbolo):
        """
        Inserta un símbolo en la tabla actual.

        :param id: El identificador/nombre del símbolo a insertar.
        :param simbolo: El objeto Simbolo a insertar en la tabla.
        :return: None
        """
        self.tablaActual[id] = simbolo

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