class CargaAcademica:

    def __init__(self, docente, periodo):
        self.__docente = docente
        self.__periodo = periodo
        self.__cursos: list = []
        self.__horas_asignadas: int = 0
        self.__horas_maximas: int = 40
        
    @property
    def docente(self):
        return self.__docente

    @property
    def periodo(self):
        return self.__periodo

    @property
    def horas_maximas(self) -> int:
        return self.__horas_maximas

    @property
    def horas_asignadas(self) -> int:
        return self.__horas_asignadas

    @property
    def horas_disponibles(self) -> int:
        return self.__horas_maximas - self.__horas_asignadas

    @property
    def porcentaje_carga(self) -> float:
        return round((self.__horas_asignadas / self.__horas_maximas) * 100, 1)

    # Metodos
    def agregar_curso(self, curso, horas_semanales: int) -> bool:
        if horas_semanales > self.horas_disponibles:
            print(f" No hay horas disponibles. Disponibles: {self.horas_disponibles}h")
            return False
        self.__cursos.append({"curso": curso, "horas": horas_semanales})
        self.__horas_asignadas += horas_semanales
        return True

    def remover_curso(self, id_curso: str) -> bool:
        for item in self.__cursos:
            if item["curso"].id_curso == id_curso:
                self.__horas_asignadas -= item["horas"]
                self.__cursos.remove(item)
                return True
        return False

    def get_cursos(self) -> list:
        return list(self.__cursos)

    def esta_completa(self) -> bool:
        return self.__horas_asignadas >= self.__horas_maximas
