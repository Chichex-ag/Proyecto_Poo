class Matricula:
    def __init__(self, id_matricula, fecha, tipo, estado):
        self._id_matricula = id_matricula
        self._fecha = fecha
        self._tipo = tipo
        self._estado = estado

    @property
    def id_matricula(self):
        return self._id_matricula

    @id_matricula.setter
    def id_matricula(self, valor):
        self._id_matricula = valor

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        self._fecha = valor

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        self._tipo = valor

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, valor):
        self._estado = valor

    def procesar_matricula(self):
        pass

    def anular_matricula(self):
        pass