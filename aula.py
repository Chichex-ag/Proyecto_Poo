class Aula:
    def __init__(self, id_aula, codigo, capacidad, estado):
        self._id_aula = id_aula
        self._codigo = codigo
        self._capacidad = capacidad
        self._estado = estado

    @property
    def id_aula(self):
        return self._id_aula

    @id_aula.setter
    def id_aula(self, valor):
        self._id_aula = valor

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor

    @property
    def capacidad(self):
        return self._capacidad

    @capacidad.setter
    def capacidad(self, valor):
        self._capacidad = valor

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, valor):
        self._estado = valor

    def registrar_aula(self):
        pass
