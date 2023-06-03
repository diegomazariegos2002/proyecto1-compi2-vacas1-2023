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

    def clean_Consola(self):
        self.consola = ""

    def set_Consola (self, consola):
        self.consola += consola

    def get_Consola (self):
        return self.consola