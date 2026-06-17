from Evaluacion import Evaluacion
from datetime import date

class Examen_virtual(Evaluacion):
    
    def __init__(self, id_evaluacion: int, nombre: str, fecha: date,
                 puntaje_maximo: float, porcentaje: float,
                 intentos_permitidos: int = 1, plataforma: str = "Moodle"):
        super().__init__(id_evaluacion, nombre, fecha, puntaje_maximo, porcentaje)
        self.__intentos_permitidos = intentos_permitidos
        self.__plataforma = plataforma

    @property
    def intentos_permitidos(self) -> int:
        return self.__intentos_permitidos

    @property
    def plataforma(self) -> str:
        return self.__plataforma

    def get_tipo(self) -> str:
        return "Examen Online"

    def calcular_nota(self, puntaje_obtenido: float) -> float:
        if puntaje_obtenido > self.puntaje_maximo:
            raise ValueError("Puntaje obtenido supera el máximo.")
        proporcion = puntaje_obtenido / self.puntaje_maximo
        return round(proporcion * 10 * (self.porcentaje / 100), 2)