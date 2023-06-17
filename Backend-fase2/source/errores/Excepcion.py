from datetime import datetime

class Excepcion:
    def __init__(self, titulo: str ="", descripcion: str="", linea: str=0, columna: str=0, fecha_hora: datetime=datetime.now()):
        self.titulo = titulo
        self.descripcion = descripcion
        self.linea = linea
        self.columna = columna
        self.fecha_hora = fecha_hora

    def __str__(self) -> str:
        return f"{self.titulo} {self.descripcion} en la línea {self.linea} y columna {self.columna} ({self.fecha_hora})"

    def json(self):
        return {
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "linea": self.linea,
            "columna": self.columna,
            "fecha_hora": self.fecha_hora.strftime("%Y-%m-%d %H:%M:%S")
        }
