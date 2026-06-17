class Calificacion:

    NOTA_APROBACION = 7.0

    def __init__(self, estudiante, curso, periodo):
        self.__estudiante = estudiante
        self.__curso = curso
        self.__periodo = periodo
        self.__notas: list = []         
        self.__nota_final: float | None = None

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
    def nota_final(self) -> float | None:
        return self.__nota_final

    @property
    def promedio(self) -> float:
        if not self.__notas:
            return 0.0
        return round(
            sum(n.nota_ponderada for n in self.__notas), 2
        )

    @property
    def aprobado(self) -> bool:
        if self.__nota_final is not None:
            return self.__nota_final >= self.NOTA_APROBACION
        return self.promedio >= self.NOTA_APROBACION

    @property
    def total_evaluaciones(self) -> int:
        return len(self.__notas)

    # ── Métodos ───────────────────────────────────────────
    def agregar_nota(self, nota):
        self.__notas.append(nota)

    def calcular_nota_final(self) -> float:
        self.__nota_final = self.promedio
        return self.__nota_final

    def get_notas(self) -> list:
        return list(self.__notas)

    def get_detalle(self) -> list:
        return [n for n in self.__notas]

#Sobrecarga

    def __str__(self) -> str:
        estado = "APROBADO" if self.aprobado else "REPROBADO"
        return (f"Calificación | {self.__estudiante.nombre_completo} | "
                f"Curso: {self.__curso.nombre} | "
                f"Promedio: {self.promedio}/10 | {estado}")

    def __float__(self) -> float:
        return self.promedio
