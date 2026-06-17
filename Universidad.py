class Universidad:

    def __init__(self, nombre: str, ruc: str, ciudad: str, mision: str = ""):
        self.__nombre = nombre
        self.__ruc = ruc
        self.__ciudad = ciudad
        self.__mision = mision
        self.__sedes: list = []
        self.__carreras: list = []


    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor.strip():
            raise ValueError("El nombre de la universidad no puede estar vacío.")
        self.__nombre = valor.strip().title()

    @property
    def ruc(self) -> str:
        return self.__ruc

    @property
    def ciudad(self) -> str:
        return self.__ciudad

    @property
    def mision(self) -> str:
        return self.__mision

    @mision.setter
    def mision(self, valor: str):
        self.__mision = valor

    @property
    def total_sedes(self) -> int:
        return len(self.__sedes)

    @property
    def total_carreras(self) -> int:
        return len(self.__carreras)

#Metodos
    def agregar_sede(self, sede):
        self.__sedes.append(sede)

    def agregar_carrera(self, carrera):
        if carrera not in self.__carreras:
            self.__carreras.append(carrera)

    def get_sedes(self) -> list:
        return list(self.__sedes)

    def get_carreras(self) -> list:
        return list(self.__carreras)