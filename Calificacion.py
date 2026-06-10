class Calificacion:
    def __init__(self, id_calificacion, nota1, nota2, nota_final):
        self._id_calificacion = id_calificacion
        self._nota1 = nota1
        self._nota2 = nota2
        self._nota_final = nota_final

    @property
    def id_calificacion(self):
        return self._id_calificacion

    @id_calificacion.setter
    def id_calificacion(self, valor):
        self._id_calificacion = valor

    @property
    def nota1(self):
        return self._nota1

    @nota1.setter
    def nota1(self, valor):
        self._nota1 = valor

    @property
    def nota2(self):
        return self._nota2

    @nota2.setter
    def nota2(self, valor):
        self._nota2 = valor

    @property
    def nota_final(self):
        return self._nota_final

    @nota_final.setter
    def nota_final(self, valor):
        self._nota_final = valor

    def calcular_promedio(self):
        return (self._nota1 + self._nota2) / 2