from crispy_forms.layout import Row, Column, Layout, Submit
from crispy_forms.helper import FormHelper
from django import forms

from django.forms import ModelForm

from mi_aplicacion.models import Escuela, Maestro

class EscuelaForm(ModelForm):
    class Meta:
        model = Escuela
        fields = ['nombre', 'siglas']

class MaestroForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MaestroForm,self).__init__(*args, **kwargs)
        self.fields['escuela'].queryset = Escuela.objects.all()
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('nombre', css_class='form-group col-md-6 mb-0'),
                Column('escuela', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('sexo', css_class='form-group col-md-6 mb-0'),
                Column('fecha_nacimiento', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Guardar', css_class='btn btn-primary')
        )

    class Meta:
        model = Maestro
        fields = ['nombre', 'escuela', 'sexo', 'fecha_nacimiento']