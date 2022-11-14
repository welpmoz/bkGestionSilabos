from rest_framework import serializers
from .models import Semestre, Curso, CursosOfrecido, Horario, Matricula, Docente, Alumno

class SemestreSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Semestre
    fields = ['idSemestre', 'anio', 'periodoSemestre']

class CursoSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Curso
    fields = ['idCurso', 'nombreCurso', 'tipo', 'numCreditos']

class CursosOfrecidoSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = CursosOfrecido
    fields = ['id', 'idSemestre', 'idCurso', 'codDocente']

class HorarioSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Horario
    fields = ['idHorario', 'dia', 'horaInicio', 'horaFin', 'aula']

class MatriculaSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Matricula
    fields = ['id', 'idCursosOfrecido', 'codAlumno', 'tipo']

class DocenteSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Docente
    fields = ['codDocente', 'nombreApellido', 'tipo', 'sexo', 'anioNacimiento']

class AlumnoSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Alumno
    fields = ['codAlumno', 'nombreApellido', 'sexo', 'anioNacimiento']