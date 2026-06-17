from Reporte import Reporte

class ReporteCalificacion(Reporte):

    def __init__(self, calificacion):
        self.__calificacion = calificacion

    def generar(self):

        estado = "Aprobado"

        if not self.__calificacion.aprobado:
            estado = "Reprobado"

        return f"""
    REPORTE CALIFICACION
    Estudiante: {self.__calificacion.estudiante.nombre_completo}
    Curso: {self.__calificacion.curso.nombre}
    Promedio: {self.__calificacion.promedio}
    Estado: {estado}
    """