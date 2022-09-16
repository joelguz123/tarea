from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cursor
from .forms import CursorForm

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def materia(request):
    materia = Cursor.objects.all()
    return render(request, 'materia/index.html', {'materia': materia})

def crear(request):
    formulario = CursorForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('materia')
    return render(request, 'materia/crear.html', {'formulario': formulario})

def editar(request, id):
    mate = Cursor.objects.get(id=id)
    formulario = CursorForm(request.POST or None, instance=mate)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('materia')
    return render(request, 'materia/editar.html', {'formulario': formulario})

def eliminar(request, id):
    mate = Cursor.objects.get(id=id)
    mate.delete()
    return redirect('materia')




