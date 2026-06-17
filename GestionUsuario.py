from Usuario import Usuario

class GestionUsuario:

    def __init__(self):
        self.__usuarios: dict[str, Usuario] = {}    # username -> Usuario
        self.__usuario_activo: Usuario | None = None

    @property
    def usuario_activo(self) -> Usuario | None:
        return self.__usuario_activo

    @property
    def total_usuarios(self) -> int:
        return len(self.__usuarios)


    def registrar_usuario(self, usuario: Usuario) -> bool:
        if usuario.username in self.__usuarios:
            print(f" El usuario '{usuario.username}' ya existe.")
            return False
        self.__usuarios[usuario.username] = usuario
        print(f" Usuario '{usuario.username}' registrado correctamente.")
        return True

    def iniciar_sesion(self, username: str, contrasena: str) -> bool:
        usuario = self.__usuarios.get(username)
        if not usuario:
            print("  Usuario no encontrado.")
            return False
        if not usuario.activo:
            print("  Usuario desactivado.")
            return False
        if not usuario.verificar_contrasena(contrasena):
            print(" Contraseña incorrecta.")
            return False
        self.__usuario_activo = usuario
        print(f" Sesión iniciada como {usuario.get_rol()}: {username}")
        return True

    def cerrar_sesion(self):
        if self.__usuario_activo:
            print(f" Sesión cerrada: {self.__usuario_activo.username}")
            self.__usuario_activo = None
        else:
            print("  No hay sesión activa.")

    def desactivar_usuario(self, username: str) -> bool:
        usuario = self.__usuarios.get(username)
        if not usuario:
            return False
        usuario.activo = False
        return True

    def buscar_usuario(self, username: str) -> Usuario | None:
        return self.__usuarios.get(username)

    def listar_usuarios(self):
        print(f"\n{'─'*45}")
        print(f"  Usuarios registrados ({self.total_usuarios})")
        print(f"{'─'*45}")
        for u in self.__usuarios.values():
            print(f"  {u}")
        print(f"{'─'*45}")

    def __str__(self) -> str:
        activo = self.__usuario_activo.username if self.__usuario_activo else "Ninguno"
        return f"GestionUsuario | Usuarios: {self.total_usuarios} | Activo: {activo}"