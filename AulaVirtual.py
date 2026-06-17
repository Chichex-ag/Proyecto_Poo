class AulaVirtual:

    def __init__(self, id_aula: str, nombre: str, plataforma: str,url: str, capacidad_max: int = 100):
        self.__id_aula = id_aula
        self.__nombre = nombre
        self.__plataforma = plataforma     
        self.__url = url
        self.__capacidad_max = capacidad_max
        self.__participantes: list = []
        self.__activa = True

    @property
    def id_aula(self) -> str:
        return self.__codigo

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def plataforma(self) -> str:
        return self.__plataforma

    @property
    def url(self) -> str:
        return self.__url

    @property
    def capacidad_max(self) -> int:
        return self.__capacidad_max

    @property
    def activa(self) -> bool:
        return self.__activa

    @property
    def participantes_actuales(self) -> int:
        return len(self.__participantes)

    @property
    def cupo_disponible(self) -> int:
        return self.__capacidad_max - self.participantes_actuales

    # Metodo
    def agregar_participante(self, cedula: str) -> bool:
        if self.cupo_disponible <= 0:
            print(" Aula virtual sin cupo.")
            return False
        if cedula not in self.__participantes:
            self.__participantes.append(cedula)
            return True
        return False

    def remover_participante(self, cedula: str) -> bool:
        if cedula in self.__participantes:
            self.__participantes.remove(cedula)
            return True
        return False

    def activar(self):
        self.__activa = True

    def desactivar(self):
        self.__activa = False