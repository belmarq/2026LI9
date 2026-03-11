from django.forms import ModelForm

from mi_aplicacion.models import Escuela, Maestro

class EscuelaForm(ModelForm):
    class Meta:
        model = Escuela
        fields = ['nombre', 'siglas']

class MaestroForm(ModelForm):
    class Meta:
        model = Maestro
        fields = ['nombre', 'escuela', 'sexo', 'fecha_nacimiento']