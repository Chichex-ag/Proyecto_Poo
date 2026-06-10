from Calificacion import Calificacion
class DetalleCalificacion(Calificacion):
    def __init__(self, id_calificacion, nota1, nota2, nota_final, descripcion):
        super().__init__(id_calificacion, nota1, nota2, nota_final)
        self._descripcion = descripcion

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor):
        self._descripcion = valor

    def registrar_detalle(self):
        pass