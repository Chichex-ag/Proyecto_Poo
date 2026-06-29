from abc import ABC, abstractmethod
from Usuario import Usuario

# 1. PASO COMPONENTE: Clase abstracta base para los eslabones de la cadena
class EslabónAutenticacion(ABC):
    def __init__(self):
        self._siguiente: EslabónAutenticacion | None = None

    def establecer_siguiente(self, siguiente: 'EslabónAutenticacion') -> 'EslabónAutenticacion':
        self._siguiente = siguiente
        return siguiente  # Permite encadenamiento: e1.establecer_siguiente(e2).establecer_siguiente(e3)

    @abstractmethod
    def manejar(self, username: str, contrasena: str, usuarios: dict[str, Usuario]) -> Usuario | None:
        """
        Procesa la solicitud. Si pasa la validación, delega al siguiente eslabón.
        Retorna el objeto Usuario si todo es correcto, o None si falla.
        """
        if self._siguiente:
            return self._siguiente.manejar(username, contrasena, usuarios)
        return None


# 2. ESLABONES CONCRETOS (Cada validación por separado)
class ValidarExistencia(EslabónAutenticacion):
    def manejar(self, username: str, contrasena: str, usuarios: dict[str, Usuario]) -> Usuario | None:
        usuario = usuarios.get(username)
        if not usuario:
            print(" ⚠ Usuario no encontrado.")
            return None
        # Si existe, pasamos el flujo al siguiente eslabón
        return super().manejar(username, contrasena, usuarios) if self._siguiente else usuario


class ValidarEstado(EslabónAutenticacion):
    def manejar(self, username: str, contrasena: str, usuarios: dict[str, Usuario]) -> Usuario | None:
        usuario = usuarios.get(username)
        # Nota: Ya sabemos que existe porque pasó el eslabón anterior
        if usuario and not usuario.activo:
            print(" ⚠ Usuario desactivado.")
            return None
        return super().manejar(username, contrasena, usuarios) if self._siguiente else usuario


class ValidarContrasena(EslabónAutenticacion):
    def manejar(self, username: str, contrasena: str, usuarios: dict[str, Usuario]) -> Usuario | None:
        usuario = usuarios.get(username)
        if usuario and not usuario.verificar_contrasena(contrasena):
            print(" ⚠ Contraseña incorrecta.")
            return None
        # Si la contraseña es correcta y es el último eslabón, devolvemos el usuario exitosamente
        return usuario


# 3. CLASE GESTIONUSUARIO MODIFICADA

class GestionUsuario:

    def __init__(self):
        self.__usuarios: dict[str, Usuario] = {}    # username -> Usuario
        self.__usuario_activo: Usuario | None = None
        
        # Construimos y configuramos la cadena de responsabilidad una sola vez
        self.__cadena_autenticacion = ValidarExistencia()
        (self.__cadena_autenticacion
         .establecer_siguiente(ValidarEstado())
         .establecer_siguiente(ValidarContrasena()))

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

    # --- AQUÍ SUCEDE LA MAGIA DEL PATRÓN ---
    def iniciar_sesion(self, username: str, contrasena: str) -> bool:
        # Delejamos todo el procesamiento de las reglas a la cadena
        usuario_autenticado = self.__cadena_autenticacion.manejar(username, contrasena, self.__usuarios)
        
        if usuario_autenticado:
            self.__usuario_activo = usuario_autenticado
            print(f" Sesión iniciada como {usuario_autenticado.get_rol()}: {username}")
            return True
        
        return False

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