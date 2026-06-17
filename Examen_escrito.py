from Evaluacion import Evaluacion
from datetime import date

class Examen_escrito(Evaluacion):

    def __init__(self, id_evaluacion: int, nombre: str, fecha: date,
                 puntaje_maximo: float, porcentaje: float, duracion_minutos: int):
        super().__init__(id_evaluacion, nombre, fecha, puntaje_maximo, porcentaje)
        self.__duracion_minutos = duracion_minutos

    @property
    def duracion_minutos(self) -> int:
        return self.__duracion_minutos

    def get_tipo(self) -> str:
        return "Examen Escrito"

    def calcular_nota(self, puntaje_obtenido: float) -> float:
        if puntaje_obtenido > self.puntaje_maximo:
            raise ValueError("Puntaje obtenido supera el máximo.")
        proporcion = puntaje_obtenido / self.puntaje_maximo
        return round(proporcion * 10 * (self.porcentaje / 100), 2)