class Carrera:
  
    def __init__(self, id_carrera: str, nombre: str, facultad: str,
                 duracion_semestres: int, modalidad: str = "Presencial"):
        self.__id_carrera = id_carrera
        self.__nombre = nombre
        self.__facultad = facultad
        self.__duracion_semestres = duracion_semestres
        self.__modalidad = modalidad
        self.__cursos_nivelacion: list = []

    @property
    def id_carrera(self) -> str:
        return self.__id_carrera

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def facultad(self) -> str:
        return self.__facultad

    @property
    def duracion_semestres(self) -> int:
        return self.__duracion_semestres

    @property
    def modalidad(self) -> str:
        return self.__modalidad

    @modalidad.setter
    def modalidad(self, valor: str):
        opciones = ["Presencial", "Virtual", "Semipresencial"]
        if valor not in opciones:
            raise ValueError(f"Modalidad debe ser: {opciones}")
        self.__modalidad = valor

    @property
    def total_cursos_nivelacion(self) -> int:
        return len(self.__cursos_nivelacion)


    def agregar_curso_nivelacion(self, curso):
        self.__cursos_nivelacion.append(curso)

    def get_cursos_nivelacion(self) -> list:
        return list(self.__cursos_nivelacion)