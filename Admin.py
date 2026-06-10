from Usuario import Usuario
from GestionReportes import GestionReportes

class Administrador(Usuario, GestionReportes):
    def __init__(self, id_usuario, cedula, nombres, apellidos, correo, telefono, estado, contraseña, cargo):
        super().__init__(id_usuario, cedula, nombres, apellidos, correo, telefono, estado, contraseña)
        self._cargo = cargo

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, valor):
        self._cargo = valor

    def gestionar_usuarios(self):
        pass

    def configurar_parametros(self):
        pass

    def mostrar_rol(self):
        return "Administrador"