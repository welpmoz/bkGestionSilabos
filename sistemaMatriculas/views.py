from .serializers import *
from .models import *

from rest_framework import viewsets
# Create your views here.

class SemestreViewSet(viewsets.ModelViewSet):
  queryset = Semestre.objects.all()
  serializer_class = SemestreSerializer

class CursoViewSet(viewsets.ModelViewSet):
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer

class CursosOfrecidoViewSet(viewsets.ModelViewSet):
  queryset = CursosOfrecido.objects.all()
  serializer_class = CursosOfrecidoSerializer

class HorarioViewSet(viewsets.ModelViewSet):
  queryset = Horario.objects.all()
  serializer_class = HorarioSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
  queryset = Matricula.objects.all()
  serializer_class = MatriculaSerializer

class DocenteViewSet(viewsets.ModelViewSet):
  queryset = Docente.objects.all()
  serializer_class = DocenteSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
  queryset = Alumno.objects.all()
  serializer_class = AlumnoSerializer