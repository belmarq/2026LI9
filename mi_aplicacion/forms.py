from crispy_forms.layout import Row, Column, Layout, Submit
from crispy_forms.helper import FormHelper
from django import forms

from django.forms import ModelForm

from mi_aplicacion.models import Escuela, Maestro
from django.contrib.auth.models import User, Group

class UsuarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UsuarioForm,self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('is_active', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', '{{ texto_boton }}', css_class='btn btn-primary')
        )
        
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "is_active")


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['username'])
        
        if commit:
            user.save()
            group = Group.objects.get(name='capturista')
            user.groups.add(group)
        return user


    

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
            Submit('submit', '{{ texto_boton }}', css_class='btn btn-primary')
        )

    class Meta:
        model = Maestro
        fields = ['nombre', 'escuela', 'sexo', 'fecha_nacimiento']
        labels = {
            'nombre': 'Nombre Completo',
            'escuela': 'Escuela a la que pertenece',
            'sexo': 'Sexo',
            'fecha_nacimiento': 'Fecha de Nacimiento'
        }
        widgets = {
            'fecha_nacimiento': forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date', 'class': 'form-control'}), 
        }