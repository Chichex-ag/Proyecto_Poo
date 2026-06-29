from abc import ABC, abstractmethod

class ObservadorCalificacion(ABC):
    @abstractmethod
    def actualizar(self, calificacion, evento: str) -> None:
        """Recibe la calificación afectada y el tipo de evento ocurrido."""
        pass


class ServicioNotificaciones(ObservadorCalificacion):
    def actualizar(self, calificacion, evento: str) -> None:
        estudiante = calificacion.estudiante
        curso = calificacion.curso
        
        print(f"\n[NOTIFICACIÓN ALUMNO] Para: {estudiante.username}")
        print(f"   Evento: {evento}")
        print(f"   Materia: {curso.nombre} | Periodo: {calificacion.periodo}")
        
        if evento == "NUEVA_NOTA_REGISTRADA":
            # Obtenemos la última nota agregada
            ultima_nota = calificacion.get_notas()[-1]
            print(f"   Detalle: Se registró un puntaje de {ultima_nota.nota_sobre_diez}/10 en '{ultima_nota.evaluacion.nombre}'")
            print(f"   Promedio Actual Acumulado: {calificacion.promedio}/10")
            
        elif evento == "PROMEDIO_FINAL_CALCULADO":
            estado = "APROBADO" if calificacion.aprobado else "REPROBADO"
            print(f"   Tu nota final ha sido publicada")
            print(f"   Nota Final: {calificacion.nota_final}/10 -> Estado: {estado}")
            
        print(f"{'─'*50}\n")