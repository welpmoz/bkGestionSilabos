from django.contrib import admin

from .models import Semestre, Curso, Horario, Docente, Alumno, CursosOfrecido, Matricula
# Register your models here.
admin.site.register(Semestre)
admin.site.register(Curso)
admin.site.register(Horario)
admin.site.register(Docente)
admin.site.register(Alumno)
admin.site.register(CursosOfrecido)
admin.site.register(Matricula)