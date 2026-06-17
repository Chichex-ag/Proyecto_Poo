from datetime import date

class Nota:
    
    def __init__(self, estudiante, evaluacion, puntaje_obtenido: float):
        if puntaje_obtenido < 0:
            raise ValueError("El puntaje no puede ser negativo.")
        if puntaje_obtenido > evaluacion.puntaje_maximo:
            raise ValueError(f"Puntaje supera el máximo ({evaluacion.puntaje_maximo}).")
        self.__estudiante = estudiante
        self.__evaluacion = evaluacion
        self.__puntaje_obtenido = puntaje_obtenido
        self.__fecha_registro = date.today()
        self.__observacion: str = ""

    @property
    def estudiante(self):
        return self.__estudiante

    @property
    def evaluacion(self):
        return self.__evaluacion

    @property
    def puntaje_obtenido(self) -> float:
        return self.__puntaje_obtenido

    @puntaje_obtenido.setter
    def puntaje_obtenido(self, valor: float):
        if valor < 0 or valor > self.__evaluacion.puntaje_maximo:
            raise ValueError("Puntaje fuera de rango.")
        self.__puntaje_obtenido = valor

    @property
    def nota_sobre_diez(self) -> float:
        return round(
            (self.__puntaje_obtenido / self.__evaluacion.puntaje_maximo) * 10, 2
        )

    @property
    def nota_ponderada(self) -> float:
        return self.__evaluacion.calcular_nota_ponderada(self.__puntaje_obtenido)

    @property
    def fecha_registro(self) -> date:
        return self.__fecha_registro

    @property
    def observacion(self) -> str:
        return self.__observacion

    @observacion.setter
    def observacion(self, valor: str):
        self.__observacion = valor

    @property
    def aprobada(self) -> bool:
        return self.nota_sobre_diez >= 7.0

    # ── Sobrecarga ────────────────────────────────────────
    def __str__(self) -> str:
        estado = "Aprobada" if self.aprobada else "Reprobada"
        return (f"Nota | {self.__estudiante.nombre_completo} | "
                f"{self.__evaluacion.nombre} | "
                f"Puntaje: {self.__puntaje_obtenido}/{self.__evaluacion.puntaje_maximo} "
                f"= {self.nota_sobre_diez}/10 | {estado}")