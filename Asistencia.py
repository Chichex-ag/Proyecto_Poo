from datetime import date

class Asistencia:
    def __init__(self, id_asistencia: int, curso, fecha: date ,docente):
        self._id_asistencia = id_asistencia
        self._curso = curso        
        self._fecha = fecha
        self._docente = docente
        self._detalles_asistencia: list = []
        self._asistencia_cerrada = False

    @property
    def id_asistencia(self):
        return self._id_asistencia
    
    @property
    def curso(self):
        return self._curso
    
    @property
    def fecha(self):
        return self._fecha
    
    @property
    def docente(self):
        return self._docente
    
    @property
    def asistencia_cerrada(self):
        return self._asistencia_cerrada
    
    @property
    def detalles_asistencia(self):
        return self._detalles_asistencia
    
    @property
    def total_registros(self):
        return len(self._detalles_asistencia)
    
    @property
    def total_asistencias(self) -> int:
        return sum(1 for detalle in self._detalles_asistencia if detalle.presente)
    
    @property
    def total_ausentes(self) -> int:
        return sum(1 for detalle in self._detalles_asistencia if not detalle.presente)

    @property
    def porcentaje_asistencia(self) -> float:
        if self.total_registros == 0:
            return 0.0
        return round((self.total_presentes / self.total_registros) * 100, 1)
    
    
    def agregar_detalle(self, detalle):
        if self.__cerrada:
            raise Exception("No se puede modificar una asistencia cerrada.")
        self.__detalles.append(detalle)

    def cerrar_asistencia(self):
        self.__cerrada = True

    def obtener_detalles(self) -> list:
        return list(self.__detalles)

    #Sobrecarga del metodo para mostrar el resumen de la asistencia
    
    def __str__(self) -> str:
        return (f"Asistencia #{self.__id_asistencia} | "
                f"Curso: {self.__curso.nombre} | Fecha: {self.__fecha} | "
                f"Presentes: {self.total_presentes}/{self.total_registros} "
                f"({self.porcentaje_asistencia}%)")
