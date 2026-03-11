from django.forms import ModelForm

from mi_aplicacion.models import Escuela

class EscuelaForm(ModelForm):
    class Meta:
        model = Escuela
        fields = ['nombre', 'siglas']
