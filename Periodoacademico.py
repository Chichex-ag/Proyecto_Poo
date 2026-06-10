class PeriodoAcademico:
    def __init__(self, id_periodo, nombre, fecha_inicio, fecha_fin, estado):
        self._id_periodo = id_periodo
        self._nombre = nombre
        self._fecha_inicio = fecha_inicio
        self._fecha_fin = fecha_fin
        self._estado = estado

    @property
    def id_periodo(self):
        return self._id_periodo

    @id_periodo.setter
    def id_periodo(self, valor):
        self._id_periodo = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def fecha_inicio(self):
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, valor):
        self._fecha_inicio = valor

    @property
    def fecha_fin(self):
        return self._fecha_fin

    @fecha_fin.setter
    def fecha_fin(self, valor):
        self._fecha_fin = valor

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, valor):
        self._estado = valor

    def abrir_periodo(self):
        pass

    def cerrar_periodo(self):
        pass