
class Aula:

    def __init__(self, id_aula: str, nombre: str, capacidad: int = True):
        self.__id_aula = id_aula                 
        self.__nombre = nombre
        self.__capacidad = capacidad
        self.__disponible = True
        self.__horarios_ocupados: list = []

    # ── Propiedades ──────────────────────────────────────
    @property
    def id_aula(self) -> str:
        return self.__id_aula

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def capacidad(self) -> int:
        return self.__capacidad

    @capacidad.setter
    def capacidad(self, valor: int):
        if valor <= 0:
            raise ValueError("La capacidad debe ser mayor a 0")
        self.__capacidad = valor

    @property
    def edificio(self) -> str:
        return self.__edificio

    @property
    def tiene_proyector(self) -> bool:
        return self.__tiene_proyector

    @property
    def disponible(self) -> bool:
        return self.__disponible

    # Metodo
    def reservar(self, horario: str) -> bool:
        if horario in self.__horarios_ocupados:
            print(f"Aula {self.__codigo} ya ocupada en {horario}.")
            return False
        self.__horarios_ocupados.append(horario)
        return True

    def liberar(self, horario: str) -> bool:
        if horario in self.__horarios_ocupados:
            self.__horarios_ocupados.remove(horario)
            return True
        return False

    def get_horarios_ocupados(self) -> list:
        return list(self.__horarios_ocupados)

    def es_apta_para(self, num_estudiantes: int) -> bool:
        return self.__capacidad >= num_estudiantes


