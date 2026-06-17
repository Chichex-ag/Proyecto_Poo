from reportes.ReporteEstudiante import ReporteEstudiante
from reportes.ReporteCurso import ReporteCurso
from reportes.ReporteCalificacion import ReporteCalificacion

class ReporteFactory:

    @staticmethod
    def crear_reporte(tipo, objeto):

        if tipo == "estudiante":
            return ReporteEstudiante(objeto)

        elif tipo == "curso":
            return ReporteCurso(objeto)

        elif tipo == "calificacion":
            return ReporteCalificacion(objeto)

        else:
            raise ValueError("Tipo de reporte no válido")