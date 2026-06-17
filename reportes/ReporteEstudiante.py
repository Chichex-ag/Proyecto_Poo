from Reporte import Reporte

class ReporteEstudiante(Reporte):

    def __init__(self, estudiante):
        self.__estudiante = estudiante

    def generar(self):

        return f"""
        REPORTE ESTUDIANTE

        Nombre: {self.__estudiante.nombre_completo}
        Cédula: {self.__estudiante.cedula}
        """