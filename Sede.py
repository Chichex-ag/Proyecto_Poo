class Sede:

    def __init__(self, id_aula: str, nombre: str, ciudad: str, direccion: str):
        self.__id_aula = id_aula
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__direccion = direccion
        self.__aulas: list = []
        self.__carreras: list = []

    @property
    def id_aula(self) -> str:
        return self.__id_aula

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def ciudad(self) -> str:
        return self.__ciudad

    @property
    def direccion(self) -> str:
        return self.__direccion

    @direccion.setter
    def direccion(self, valor: str):
        if not valor.strip():
            raise ValueError("La dirección no puede estar vacía.")
        self.__direccion = valor.strip()

    @property
    def total_aulas(self) -> int:
        return len(self.__aulas)

#Metodos 
    def agregar_aula(self, aula):
        self.__aulas.append(aula)

    def agregar_carrera(self, carrera):
        if carrera not in self.__carreras:
            self.__carreras.append(carrera)

    def get_aulas(self) -> list:
        return list(self.__aulas)

    def buscar_aula(self, id_aula: str):
        for a in self.__aulas:
            if a.id_aula == id_aula:
                return a
        return None