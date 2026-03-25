from django.urls import path, include
from django.contrib.auth.models import Group, Permission, User
from rest_framework import routers, serializers, viewsets

from mi_aplicacion.models import Escuela, Maestro, Alumno
from mi_aplicacion.serializers import (
    AlumnoSerializer, 
    EscuelaSerializer, 
    GroupSerializer, 
    MaestroSerializer,
    PermissionSerializer, 
    UserSerializer 
)
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    
class EscuelaViewSet(viewsets.ModelViewSet):
    queryset = Escuela.objects.all()
    serializer_class = EscuelaSerializer

class MaestroViewSet(viewsets.ModelViewSet):
    queryset = Maestro.objects.all()
    serializer_class = MaestroSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer