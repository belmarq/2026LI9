from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from mi_aplicacion.models import Escuela, Maestro, Alumno

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class EscuelaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Escuela
        fields = "__all__"

class MaestroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Maestro
        fields = "__all__"

class AlumnoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alumno
        fields = "__all__"
