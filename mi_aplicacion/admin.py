from django.contrib import admin

from .models import Escuela, Maestro, Alumno
admin.site.register(Escuela)
admin.site.register(Maestro)
admin.site.register(Alumno)
