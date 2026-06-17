from datetime import date

class Tarea:

    def __init__(self, id_tarea: int, titulo: str, descripcion: str,
                 fecha_entrega: date, puntaje_maximo: float,
                 curso=None, tipo: str = "Tarea"):
        self.__id_tarea = id_tarea
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__fecha_entrega = fecha_entrega
        self.__puntaje_maximo = puntaje_maximo
        self.__curso = curso
        self.__tipo = tipo                  # Tarea | Proyecto | Laboratorio
        self.__entregas: list = []

    @property
    def id_tarea(self) -> int:
        return self.__id_tarea

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def descripcion(self) -> str:
        return self.__descripcion

    @property
    def fecha_entrega(self) -> date:
        return self.__fecha_entrega

    @property
    def puntaje_maximo(self) -> float:
        return self.__puntaje_maximo

    @property
    def curso(self):
        return self.__curso

    @property
    def tipo(self) -> str:
        return self.__tipo

    @property
    def total_entregas(self) -> int:
        return len(self.__entregas)

    @property
    def vencida(self) -> bool:
        return date.today() > self.__fecha_entrega

# Métodos
    def registrar_entrega(self, entrega):
        self.__entregas.append(entrega)

    def get_entregas(self) -> list:
        return list(self.__entregas)

    def dias_restantes(self) -> int:
        delta = self.__fecha_entrega - date.today()
        return max(delta.days, 0)
