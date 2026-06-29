from Universidad import Universidad
from Sede import Sede
from Carrera import Carrera
from Periodoacademico import PeriodoAcademico
from Curso import CursoNivelacion
from aula import Aula
from AulaVirtual import AulaVirtual
from Horario import Horario
from Usuario import Usuario
from Matricula import Matricula
from CargaAcademica import CargaAcademica
from Evaluacion import Evaluacion
from Examen_escrito import Examen_escrito
from Examen_virtual import Examen_virtual
from Calificacion import Calificacion
from Nota import Nota
from Asistencia import Asistencia
from Detalleasistencia import DetalleAsistencia
from Detallecalificacion import DetalleCalificacion
from Notificacion import Notificacion
from Tarea import Tarea

from usuarios.Admin import Administrador
from usuarios.Decano import Decano
from usuarios.Docente import Docente
from usuarios.Estudiante import Estudiante

from reportes.GestionReportes import Reporte
from reportes.ReporteCalificacion import ReporteCalificacion
from reportes.ReporteCurso import ReporteCurso
from reportes.ReporteEstudiante import ReporteEstudiante

def ejecutar_prueba():
    print("=== INICIANDO PRUEBA DE ESCRITORIO: SISTEMA DE NIVELACIÓN ===\n")

    # 1. INSTANCIACIÓN DE LAESTRUCTURA INSTITUCIONAL
    print("[+] Configurando infraestructura institucional...")
    universidad = Universidad(nombre="Universidad de Manta", ruc="1390000000001")
    sede = Sede(nombre="Sede Central", ubicacion="Manta")
    carrera = Carrera(nombre="Tecnologías de la Información", facultad="Ingeniería")
    periodo = PeriodoAcademico(nombre="2026-1", fecha_inicio="2026-05-01", fecha_fin="2026-09-30")

    # 2. CREACIÓN DE USUARIOS (Roles del Sistema)
    print("[+] Registrando usuarios en el sistema...")
    admin = Administrador(id="A001", nombre="Carlos", apellido="Mendoza", correo="carlos@uleam.edu.ec")
    decano = Decano(id="D001", nombre="Dra. María", apellido="Vélez", titulo="PhD. en Ciencias")
    docente = Docente(id="DOC01", nombre="Ing. Jhon", apellido="Doe", especialidad="Programación")
    estudiante = Estudiante(id="EST01", nombre="Luis", apellido="Piguave", edad=19)

    # 3. INFRAESTRUCTURA ACADÉMICA Y HORARIOS
    print("[+] Creando entorno de clases y horarios...")
    aula = Aula(bloque="Bloque Alpha", numero="Aula 102", capacidad=35)
    aula_virtual = AulaVirtual(enlace_teams="https://teams.microsoft.com/l/meetup...", plataforma="Moodle")
    horario = Horario(dia="Lunes", hora_inicio="08:00", hora_fin="10:00")
    
    # Curso de nivelación vinculando los elementos
    curso_nivelacion = CursoNivelacion(nombre="Nivelación TI - Paralelo A", periodo=periodo, carrera=carrera)

    # 4. PROCESO DE MATRICULACIÓN
    print("[+] Ejecutando matrícula del estudiante...")
    matricula = Matricula(codigo="MAT-2026-001", estudiante=estudiante, curso=curso_nivelacion, fecha="2026-04-25")
    carga_academica = CargaAcademica(docente=docente, curso=curso_nivelacion, materia="Algoritmos")

    # 5. GESTIÓN DEL DÍA A DÍA (Asistencia y Tareas)
    print("[+] Registrando actividad diaria en el aula...")
    asistencia = Asistencia(fecha="2026-06-28", curso=curso_nivelacion)
    detalle_asistencia = DetalleAsistencia(asistencia=asistencia, estudiante=estudiante, estado="Presente")
    
    tarea = Tarea(titulo="Taller de POO en Python", descripcion="Implementar herencia y polimorfismo", fecha_entrega="2026-07-02")
    notificacion = Notificacion(destinatario=estudiante, mensaje="Se ha asignado una nueva tarea de Algoritmos.")

    # 6. EVALUACIONES Y CALIFICACIONES
    print("[+] Simulando proceso de evaluación...")
    # Creamos una evaluación general, y luego subtipos (escrito o virtual) según requieras
    evaluacion_parcial = Evaluacion(titulo="Primer Parcial", ponderacion=30)
    examen_v = Examen_virtual(titulo="Examen Teórico Moodle", link_acceso="...", limite_tiempo=60)
    
    # Asignación de notas
    nota_final = Nota(valor=9.5, equivalencia="Sobresaliente")
    calificacion = Calificacion(estudiante=estudiante, evaluacion=evaluacion_parcial)
    detalle_calificacion = DetalleCalificacion(calificacion=calificacion, nota=nota_final, observacion="Excelente desempeño")

    # 7. GENERACIÓN DE REPORTES
    print("[+] Generando reportes del sistema...")
    reporte_gestion = Reporte(tipo="Académico", fecha_generacion="2026-06-28")
    reporte_estudiante = ReporteEstudiante(estudiante=estudiante, promedio_general=9.5)
    reporte_curso = ReporteCurso(curso=curso_nivelacion, total_aprobados=1, total_reprobados=0)

    # 8. VERIFICACIÓN EN CONSOLA (Output de control)
    print("\n=== VERIFICACIÓN DE DATOS VINCULADOS ===")
    print(f"Universidad: {universidad.nombre}")
    print(f"Carrera del Curso: {curso_nivelacion.carrera.nombre}")
    print(f"Estudiante Matriculado: {matricula.estudiante.nombre} {matricula.estudiante.apellido}")
    print(f"Docente a cargo: {carga_academica.docente.nombre}")
    print(f"Estado de Asistencia de Luis: {detalle_asistencia.estado}")
    print(f"Nota final de evaluación: {detalle_calificacion.nota.valor} ({detalle_calificacion.nota.equivalencia})")
    
    print("\n[!] Prueba de escritorio finalizada con éxito. Todas las clases interactúan correctamente.")

if __name__ == "__main__":
    ejecutar_prueba()