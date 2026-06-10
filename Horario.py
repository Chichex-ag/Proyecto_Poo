class Horario:
    def __init__(self, id_horario, dia, hora_inicio, hora_fin):
        self._id_horario = id_horario
        self._dia = dia
        self._hora_inicio = hora_inicio
        self._hora_fin = hora_fin

    @property
    def id_horario(self):
        return self._id_horario

    @id_horario.setter
    def id_horario(self, valor):
        self._id_horario = valor

    @property
    def dia(self):
        return self._dia

    @dia.setter
    def dia(self, valor):
        self._dia = valor

    @property
    def hora_inicio(self):
        return self._hora_inicio

    @hora_inicio.setter
    def hora_inicio(self, valor):
        self._hora_inicio = valor

    @property
    def hora_fin(self):
        return self._hora_fin

    @hora_fin.setter
    def hora_fin(self, valor):
        self._hora_fin = valor

    def registrar_horario(self):
        pass