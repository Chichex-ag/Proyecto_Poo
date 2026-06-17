from datetime import date


class Matricula:

    def __init__(self, estudiante, curso, periodo):
        self.__id = id(self)
        self.__estudiante = estudiante
        self.__curso = curso
        self.__periodo = periodo
        self.__fecha_matricula = date.today()
        self.__estado = "Activa"        # Activa | Retirada | Aprobada | Reprobada

    @property
    def id(self) -> int:
        return self.__id

    @property
    def estudiante(self):
        return self.__estudiante

    @property
    def curso(self):
        return self.__curso

    @property
    def periodo(self):
        return self.__periodo

    @property
    def fecha_matricula(self) -> date:
        return self.__fecha_matricula

    @property
    def estado(self) -> str:
        return self.__estado

    # Metodos
    def retirar(self):
        if self.__estado == "Activa":
            self.__estado = "Retirada"
            print(f"  Matrícula #{self.__id} retirada.")
        else:
            print(f"  No se puede retirar. Estado actual: {self.__estado}")

    def aprobar(self):
        self.__estado = "Aprobada"

    def reprobar(self):
        self.__estado = "Reprobada"

    def esta_activa(self) -> bool:
        return self.__estado == "Activa"