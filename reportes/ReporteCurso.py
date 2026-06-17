from Reporte import Reporte
    
class ReporteCurso(Reporte):

    def __init__(self, curso):
        self.__curso = curso

    def generar(self):

        return f"""
        REPORTE CURSO

        Código: {self.__curso.codigo}
        Nombre: {self.__curso.nombre}
        """