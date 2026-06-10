class CursoNivelacion:
    def __init__(self, id_curso, nombre, nivel, cupo_maximo):
        self._id_curso = id_curso
        self._nombre = nombre
        self._nivel = nivel
        self._cupo_maximo = cupo_maximo

    @property
    def id_curso(self):
        return self._id_curso

    @id_curso.setter
    def id_curso(self, valor):
        self._id_curso = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, valor):
        self._nivel = valor

    @property
    def cupo_maximo(self):
        return self._cupo_maximo

    @cupo_maximo.setter
    def cupo_maximo(self, valor):
        self._cupo_maximo = valor

    def asignar_docente(self, docente=None):
        pass