from django.shortcuts import render, redirect
from django.views import View

from mi_aplicacion.forms import EscuelaForm, MaestroForm

from .models import Escuela, Maestro, Alumno

class Home(View):
    def get(self, request):
        cdx={
            "titulo":"Home",
            "subtitulo":"Bienvenido a mi aplicación"}
        return render(request, "home/home.html", cdx)
    
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
        maestros = Maestro.objects.all()
        cdx={
            "titulo":"Maestros",
            "subtitulo":"Lista de maestros",
            "maestros": maestros}
        return render(request, "maestros/maestros.html", cdx)
    
class MaestrosAlta(View):
    def get(self, request):
        cdx={
        "titulo":"Maestros",
        "subtitulo":"Alta de maestro",
        "form":MaestroForm(),
        "fondo":"bg-success p-3",
        "texto_boton":"Guardar"
        }
        return render(request, 'maestros/CRUD.html', cdx)
    def post(self, request):
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
        maestro = Maestro.objects.filter(id=id).first()
        form = MaestroForm(request.POST, request.FILES, instance=maestro)
        if form.is_valid():
            form.save()
            return redirect('maestros')
        return redirect("home") 
    
class MaestroEliminar(View):
    def get(self, request, id):
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