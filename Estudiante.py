class Estudiante(Usuario):
    def __init__(self, id_usuario, cedula, nombres, apellidos, correo, telefono, estado, contraseña, discapacidad=False):
        super().__init__(id_usuario, cedula, nombres, apellidos, correo, telefono, estado, contraseña)
        self._discapacidad = discapacidad

    @property
    def discapacidad(self):
        return self._discapacidad

    @discapacidad.setter
    def discapacidad(self, valor):
        self._discapacidad = valor

    def solicitar_cupo(self):
        pass

    def consultar_horario(self):
        pass

    def mostrar_rol(self):
        return "Estudiante"