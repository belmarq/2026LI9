from django.urls import include, path
from mi_aplicacion.views import (
    Home,
    Escuelas, EscuelaAlta, EscuelaEditar, EscuelaEliminar,
    Maestros, MaestrosAlta, MaestroEditar, MaestroEliminar, 
    Usuarios, UsuarioAlta, UsuarioEliminar
    )
from rest_framework import routers
from mi_aplicacion.viewsets import (
    AlumnoViewSet, 
    AlumnoViewSet, 
    GroupViewSet, 
    MaestroViewSet,
    PermissionViewSet, 
    UserViewSet, 
    EscuelaViewSet,
)

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"groups", GroupViewSet)
router.register(r"permissions", PermissionViewSet)
router.register(r"escuelas", EscuelaViewSet)
router.register(r"maestros", MaestroViewSet)
router.register(r"alumnos", AlumnoViewSet)


urlpatterns = [
    path('', Home.as_view(), name="home"), 
    path('api/', include(router.urls)),
    path('usuarios/', Usuarios.as_view(), name="usuarios"),
    path('usuario_alta', UsuarioAlta.as_view(), name="usuario_alta"),
    path('usuario_eliminar/<int:id>/', UsuarioEliminar.as_view(), name="usuario_eliminar"),
    path('escuelas/', Escuelas.as_view(), name="escuelas"),
    path('escuelas_alta/', EscuelaAlta.as_view(), name="escuelas_alta"),    
    path('escuelas_editar/<int:id>/', EscuelaEditar.as_view(), name="escuelas_editar"),    
    path('escuelas_eliminar/<int:id>/', EscuelaEliminar.as_view(), name="escuelas_eliminar"),
    path('maestros/', Maestros.as_view(), name="maestros"),
    path('maestros_alta/', MaestrosAlta.as_view(), name="maestros_alta"),
    path('maestros_editar/<int:id>/', MaestroEditar.as_view(), name="maestros_editar"),
    path('maestros_eliminar/<int:id>/', MaestroEliminar.as_view(), name="maestros_eliminar"),

]