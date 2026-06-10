class Docente(Usuario, GestionReportes):
    def __init__(self, id_usuario, cedula, nombres, apellidos, correo, telefono, estado, contraseña, titulo, especialidad):
        super().__init__(id_usuario, cedula, nombres, apellidos, correo, telefono, estado, contraseña)
        self._titulo = titulo
        self._especialidad = especialidad

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        self._titulo = valor

    @property
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, valor):
        self._especialidad = valor

    def registrar_notas(self):
        pass

    def registrar_asistencia(self):
        pass

    def mostrar_rol(self):
        return "Docente"