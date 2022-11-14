from django.db import models

# Create your models here.
class Semestre(models.Model):
  idSemestre = models.CharField(max_length=6, primary_key=True)
  anio = models.IntegerField()
  periodoSemestre = models.CharField(max_length=1)

class Curso(models.Model):
  idCurso = models.CharField(max_length=10, primary_key=True)
  nombreCurso = models.CharField(max_length=100)
  tipo = models.CharField(max_length=20)
  numCreditos = models.IntegerField()

class Horario(models.Model):
  idHorario = models.AutoField(primary_key=True)
  DIAS = (
    ('L', 'Lunes'), ('M', 'Martes'), ('M', 'Miercoles'),
    ('J', 'Jueves'), ('V', 'Viernes'), ('S', 'Sábado'),
    ('D', 'Domingo'),
  )
  dia = models.CharField(max_length=10, choices=DIAS)
  horaInicio = models.TimeField()
  horaFin = models.TimeField()
  aula = models.CharField(max_length=10)

class Docente(models.Model):
  codDocente = models.CharField(max_length=6, primary_key=True)
  nombreApellido = models.CharField(max_length=50)
  STATUS = (
    ('C', 'Contratado'),
    ('N', 'Nombrado')
  )
  tipo = models.CharField(max_length=1, choices=STATUS)
  SEXO = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
  )
  sexo = models.CharField(max_length=1, choices=SEXO)
  anioNacimiento = models.DateField()

class Alumno(models.Model):
  codAlumno = models.CharField(max_length=6, primary_key=True)
  nombreApellido = models.CharField(max_length=50)
  SEXO = (
    # el primer valor es el campo para la base de datos
    # el segundo es el que aparece en el formulario
    ('M', 'Masculino'),
    ('F', 'Femenino'),
  )
  sexo = models.CharField(max_length=1, choices=SEXO)
  anioNacimiento = models.DateField(auto_now=True)

class CursosOfrecido(models.Model):
  idSemestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)
  idCurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
  codDocente = models.ForeignKey(Docente, on_delete=models.CASCADE)

class Matricula(models.Model):
  idCursoOfrecido = models.ForeignKey(CursosOfrecido, on_delete=models.CASCADE)
  codAlumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
  TIPO = (
    ('R', 'Regular'),
    ('T', 'Tricada'),
  )
  tipo = models.CharField(max_length=1, choices=TIPO)