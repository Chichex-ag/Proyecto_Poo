class CargaAcademica:
    def __init__(self, id_carga, total_asignaturas, total_creditos):
        self._id_carga = id_carga
        self._total_asignaturas = total_asignaturas
        self._total_creditos = total_creditos

    @property
    def id_carga(self):
        return self._id_carga

    @id_carga.setter
    def id_carga(self, valor):
        self._id_carga = valor

    @property
    def total_asignaturas(self):
        return self._total_asignaturas

    @total_asignaturas.setter
    def total_asignaturas(self, valor):
        self._total_asignaturas = valor

    @property
    def total_creditos(self):
        return self._total_creditos

    @total_creditos.setter
    def total_creditos(self, valor):
        self._total_creditos = valor

    def generar_carga(self):
        pass
