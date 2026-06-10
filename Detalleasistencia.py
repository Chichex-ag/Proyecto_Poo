from Asistencia import Asistencia

class DetalleAsistencia(Asistencia):
    def __init__(self, id_asistencia, fecha, estado, observacion):
        super().__init__(id_asistencia, fecha, estado)
        self._observacion = observacion

    @property
    def observacion(self):
        return self._observacion

    @observacion.setter
    def observacion(self, valor):
        self._observacion = valor

    def validar_justificacion(self):
        pass
