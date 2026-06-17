from abc import ABC, abstractmethod
from datetime import date


class Evaluacion(ABC):

    def __init__(self, id_evaluacion: int, nombre: str,
                 fecha: date, puntaje_maximo: float, porcentaje: float):
        if not (0 < porcentaje <= 10):
            raise ValueError("El porcentaje debe estar entre 0 y 10")
        self.__id_evaluacion = id_evaluacion
        self.__nombre = nombre
        self.__fecha = fecha
        self.__puntaje_maximo = puntaje_maximo
        self.__porcentaje = porcentaje
        self.__publicada = False

    @property
    def id_evaluacion(self) -> int:
        return self.__id_evaluacion

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def fecha(self) -> date:
        return self.__fecha

    @property
    def puntaje_maximo(self) -> float:
        return self.__puntaje_maximo

    @property
    def porcentaje(self) -> float:
        return self.__porcentaje

    @property
    def publicada(self) -> bool:
        return self.__publicada

    # Metodo abstracto
    @abstractmethod
    def get_tipo(self) -> str:
        pass

    @abstractmethod
    def calcular_nota(self, puntaje_obtenido: float) -> float:
        pass

    def publicar(self):
        self.__publicada = True