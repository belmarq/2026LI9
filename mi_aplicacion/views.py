from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User

from mi_aplicacion.forms import EscuelaForm, MaestroForm, UsuarioForm

from .models import Escuela, Maestro, Alumno

class Home(View):
    def get(self, request):
        cdx={
            "titulo":"Home",
            "subtitulo":"Bienvenido a mi aplicación"}
        return render(request, "home/home.html", cdx)
    
class Usuarios(View):
    def get(self, request):
        usuarios = User.objects.all()
        cdx={
            "titulo":"Usuarios",
            "subtitulo":"Listado de usuarios",
            "usuarios": usuarios}
        return render(request, "usuarios/usuarios.html", cdx)
    
class UsuarioAlta(View):
    def get(self, request):
        cdx={
            "titulo":"Usuarios",
            "subtitulo":"Alta de usuario nuevo",
            "fondo":"bg-success bg-opacity-25 p-3",
            "texto_boton":"Guardar",
            "form": UsuarioForm()}
        return render(request, "usuarios/CRUD.html", cdx)
    
    def post(self, request):
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
        else:
            cdx={
                "titulo":"Altas de usuario",
                "subtitulo":"Alta de usuario",
                "texto_boton":"Guardar",
                "form":form,
                "fondo":"bg-success bg-opacity-25 p-3",
                "mensaje":"Error al crear el usuario"
            }
        return render(request, 'usuarios/CRUD.html', cdx)

class UsuarioEliminar(View):
    def get(self, request, id):
        usuario = User.objects.filter(id=id).first()
        form = UsuarioForm(instance=usuario)
        cdx={
        "titulo":"Usuarios",
        "subtitulo":"Eliminar usuario",
        "texto_boton":"Eliminar",
        "form":form,
        "fondo":"bg-danger bg-opacity-25 p-3"
        }
        return render(request, 'usuarios/CRUD.html', cdx)
    
    def post(self, request, id):
        usuario = User.objects.filter(id=id).first()
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario.delete()
            return redirect('usuarios')
        return redirect("home")


class Escuelas(View):
    def get(self, request):
        escuelas = Escuela.objects.all()
        cdx={
            "titulo":"Escuelas",
            "subtitulo":"Listado de escuelas",
            "escuelas": escuelas}
        return render(request, "escuelas/escuelas.html", cdx)
    
class Escuelas(View):
    def get(self, request):
        escuelas = Escuela.objects.all()
        cdx={
            "titulo":"Escuelas",
            "subtitulo":"Listado de escuelas",
            "escuelas": escuelas}
        return render(request, "escuelas/escuelas.html", cdx)

class EscuelaAlta(View):
    def get(self, request):
        cdx={
        "titulo":"Escuela",
        "subtitulo":"Alta de escuela",
        "form":EscuelaForm()
        }
        return render(request, 'escuelas/CRUD.html', cdx)
    
    def post(self, request):
        form = EscuelaForm(request.POST, request.FILES)
        print(f"form.errors: {form.errors}")
        print(f"form.is_valid(): {form.is_valid()}")
        print(f"form.cleaned_data: {form.cleaned_data if form.is_valid() else 'N/A'}")
        if form.is_valid():
            form.save()
            return redirect('escuelas')
        else:
            cdx={
                "titulo":"Escuela",
                "subtitulo":"Alta de escuela",
                "form":form,
                "mensaje":"Error al crear la escuela"
            }
        return render(request, 'escuelas/CRUD.html', cdx)
    
class EscuelaEditar(View):
    def get(self, request, id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(instance=escuela)
        cdx={
        "titulo":"Escuela",
        "subtitulo":"Editar escuela",
        "form":form
        }
        return render(request, 'escuelas/CRUD.html', cdx)
    
    def post(self, request, id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(request.POST, request.FILES, instance=escuela)
        if form.is_valid():
            form.save()
            return redirect('escuelas')
        return redirect("home")

class EscuelaEliminar(View):
    def get(self, request, id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(instance=escuela)
        cdx={
        "titulo":"Escuela",
        "subtitulo":"Eliminar escuela",
        "form":form
        }
        return render(request, 'escuelas/CRUD.html', cdx)
    
    def post(self, request, id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(request.POST, request.FILES, instance=escuela)
        if form.is_valid():
            escuela.delete()
            return redirect('escuelas')
        return redirect("home")
    
class Maestros(View):
    def get(self, request):
        if not request.user.has_perm('mi_aplicacion.view_maestro'):
            messages.error(request, f" {request.user.username} No tienes permiso para ver la página de maestros.")
            return redirect("home")
        maestros = Maestro.objects.all()
        cdx={
            "titulo":"Maestros",
            "subtitulo":"Lista de maestros",
            "maestros": maestros,
            "escuelas": Escuela.objects.all(),
            }
        return render(request, "maestros/maestros.html", cdx)
    
    def post(self, request):
        if not request.user.has_perm('mi_aplicacion.view_maestro'):
            messages.error(request, f" {request.user.username} No tienes permiso para ver la página de maestros.")
            return redirect("home")
        escuela = request.POST.get("escuela")
        nombre = request.POST.get("nombre")
        escuela_id = int(escuela) if escuela else 0
        # print(f"escuela: {escuela}, nombre: {nombre}")
        # print(f"request.POST: {request.POST}")        
        if escuela_id != 0:
            maestros = Maestro.objects.filter(escuela_id=escuela_id, nombre__icontains=nombre).all()
        else:
            maestros = Maestro.objects.filter(nombre__icontains=nombre).all()   
        cdx={
            "titulo":"Maestros",
            "subtitulo":"Lista de maestros",
            "maestros": maestros,
            "escuelas": Escuela.objects.all(),
            "escuela_seleccionada": int(escuela_id) if escuela_id else None
            }
        return render(request, "maestros/maestros.html", cdx)
    
class MaestrosAlta(View):
    def get(self, request):
        if not request.user.has_perm('mi_aplicacion.add_maestro'):
            messages.error(request, f" {request.user.username} No tienes permiso para agregar maestros.")
            return redirect("home")
        cdx={
        "titulo":"Maestros",
        "subtitulo":"Alta de maestro",
        "form":MaestroForm(),
        "fondo":"bg-success p-3",
        "texto_boton":"Guardar"
        }
        return render(request, 'maestros/CRUD.html', cdx)
    def post(self, request):
        if not request.user.has_perm('mi_aplicacion.add_maestro'):
            messages.error(request, f" {request.user.username} No tienes permiso para agregar maestros.")
            return redirect("home")
        form = MaestroForm(request.POST, request.FILES)        
        if form.is_valid():
            form.save()
            return redirect('maestros')
        else:
            print(f"form.errors: {form.errors}")
            print(f"form.is_valid(): {form.is_valid()}")
            print(f"form.cleaned_data: {form.cleaned_data if form.is_valid() else 'N/A'}")
            cdx={
                "titulo":"Maestros",
                "subtitulo":"Alta de maestro",
                "form":form,
                "mensaje":"Error al crear el maestro",
                "fondo":"bg-success p-3",
                "texto_boton":"Guardar"
            }
        return render(request, 'maestros/CRUD.html', cdx)
    
class MaestroEditar(View):
    def get(self, request, id):
        if not request.user.has_perm('mi_aplicacion.change_maestro'):
            messages.error(request, f" {request.user.username} No tienes permiso para editar maestros.")
            return redirect("home")
        maestro = Maestro.objects.filter(id=id).first()
        form = MaestroForm(instance=maestro)
        cdx={
        "titulo":"Maestros",
        "subtitulo":"Editar maestro",
        "form":form,
        "fondo":"bg-warning p-3",
        "texto_boton":"Actualizar"
        }
        return render(request, 'maestros/CRUD.html', cdx)
    
    def post(self, request, id):
        if not request.user.has_perm('mi_aplicacion.change_maestro'):
            messages.error(request, f" {request.user.username} No tienes permiso para editar maestros.")
            return redirect("home")
        maestro = Maestro.objects.filter(id=id).first()
        form = MaestroForm(request.POST, request.FILES, instance=maestro)
        if form.is_valid():
            form.save()
            return redirect('maestros')
        return redirect("home") 
    
class MaestroEliminar(View):
    def get(self, request, id):
        if not request.user.has_perm('mi_aplicacion.delete_maestro'):
            messages.error(request, f" {request.user.username} No tienes permiso para eliminar maestros.")
            return redirect("home")
        maestro = Maestro.objects.filter(id=id).first()
        form = MaestroForm(instance=maestro)
        cdx={
        "titulo":"Maestros",
        "subtitulo":"Eliminar maestro",
        "form":form,
        "fondo":"bg-danger p-3",
        "texto_boton":"Eliminar"
        }
        return render(request, 'maestros/CRUD.html', cdx)
    
    def post(self, request, id):
        if not request.user.has_perm('mi_aplicacion.delete_maestro'):
            messages.error(request, f" {request.user.username} No tienes permiso para eliminar maestros.")
            return redirect("home")
        maestro = Maestro.objects.filter(id=id).first()
        form = MaestroForm(request.POST, request.FILES, instance=maestro)
        if form.is_valid():
            maestro.delete()
            return redirect('maestros')
        return redirect("home")
    
class Alumnos(View):
    def get(self, request):
        alumnos = Alumno.objects.all()
        cdx={
            "titulo":"Alumnos",
            "subtitulo":"Lista de alumnos",
            "alumnos": alumnos}
        return render(request, "alumnos/alumnos.html", cdx)