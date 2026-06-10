from abc import ABC , abstractmethod

class Usuario(ABC):
    def __init__(self, id_usuario, cedula, nombres, apellidos, correo, telefono, estado, contraseña):
        self._id_usuario = id_usuario
        self._cedula = cedula
        self._nombres = nombres
        self._apellidos = apellidos
        self._correo = correo
        self._telefono = telefono
        self._estado = estado
        self._contraseña = contraseña

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, valor):
        self._id_usuario = valor

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, valor):
        self._cedula = valor

    @property
    def nombres(self):
        return self._nombres

    @nombres.setter
    def nombres(self, valor):
        self._nombres = valor

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, valor):
        self._apellidos = valor

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        self._correo = valor

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        self._telefono = valor

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, valor):
        self._estado = valor

    @property
    def contraseña(self):
        return self._contraseña

    @contraseña.setter
    def contraseña(self, valor):
        self._contraseña = valor

    @abstractmethod
    def mostrar_rol(self):
        pass

    def iniciar_sesion(self):
        pass

    def cerrar_sesion(self):
        pass

    def actualizar_perfil(self):
        pass

