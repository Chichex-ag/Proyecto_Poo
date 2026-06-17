from datetime import datetime

class Notificacion:

    def __init__(self, mensaje, destinatario):
        self.__mensaje = mensaje
        self.__destinatario = destinatario
        self.__fecha = datetime.now()
        self.__leida = False

    @property
    def mensaje(self):
        return self.__mensaje

    @property
    def destinatario(self):
        return self.__destinatario

    @property
    def fecha(self):
        return self.__fecha

    @property
    def leida(self):
        return self.__leida

    def marcar_como_leida(self):
        self.__leida = True

    def enviar(self):
        print(f"Mensaje enviado a {self.__destinatario}")

    def mostrar(self):
        estado = "Leída" if self.__leida else "No Leída"

        print(f"""
        Mensaje: {self.__mensaje}
        Fecha: {self.__fecha}
        Estado: {estado}
        """)