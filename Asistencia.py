class Asistencia:
    def __init__(self, id_asistencia, fecha, estado):
        self._id_asistencia = id_asistencia
        self._fecha = fecha
        self._estado = estado

    @property
    def id_asistencia(self):
        return self._id_asistencia

    @id_asistencia.setter
    def id_asistencia(self, valor):
        self._id_asistencia = valor

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        self._fecha = valor

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, valor):
        self._estado = valor

    def registrar_asistencia(self):
        pass
