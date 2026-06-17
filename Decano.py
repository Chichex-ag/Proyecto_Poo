from Usuario import Usuario


class Decano(Usuario):

    def __init__(self, id_usuario: int, username: str, contrasena: str, facultad: str, anios_cargo: int = 0):
        super().__init__(id_usuario, username, contrasena)
        self.__facultad = facultad
        self.__anios_cargo = anios_cargo
        self.__cursos_autorizados: list = []


    @property
    def facultad(self) -> str:
        return self.__facultad

    @property
    def facultad(self) -> str:
        return self.__facultad

    @facultad.setter
    def facultad(self, valor: str):
        if not valor.strip():
            raise ValueError("La facultad no puede estar vacía.")
        self.__facultad = valor.strip().title()

    @property
    def anios_cargo(self) -> int:
        return self.__anios_cargo

    @property
    def total_autorizados(self) -> int:
        return len(self.__cursos_autorizados)

    # Metodo para autorizar cursos
    def autorizar_curso(self, curso) -> str:
        self.__cursos_autorizados.append(curso)
        return f"Curso '{curso}' autorizado por Decano {self.nombre_completo}."

    def get_cursos_autorizados(self) -> list:
        return list(self.__cursos_autorizados)

    # Metodo para presentarse y mostrar su informacion
    
    def get_tipo(self) -> str:
        return "Decano"

    def presentarse(self) -> str:
        return (f"Soy el Decano {self.nombre_completo} de la Facultad de "
                f"{self.__facultad}, con {self.__anios_cargo} años en el cargo.")