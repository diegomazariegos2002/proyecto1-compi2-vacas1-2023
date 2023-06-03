class Excepcion:

    def __init__(self, titulo:str, descripcion:str, linea:str, columna:str):
        self.titulo = titulo
        self.descripcion = descripcion
        self.linea = linea
        self.columna = columna

    def __str__(self) -> str:
        return f"{self.titulo} {self.descripcion} en la linea {self.linea} y columna {self.columna}"
    
    def json(self):
        return {
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "linea": self.linea,
            "columna": self.columna
        }