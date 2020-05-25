from django.shortcuts import render
from misiones.models import mision
from django.views import generic
from misiones.forms import misionForm
from django.urls import reverse_lazy
# Create your views here.
class ListarMision(generic.ListView):
    model=mision
    template_name="mision/listar_mision.html"
    context_object_name="cosa"
class InsertarMision(generic.CreateView):
    model=mision #Modelo de la vista
    template_name="mision/insertar_mision.html" #Donde esta la plantilla
    context_object_name="cosa"
    form_class=misionForm #Formulario creado en django
    success_url=reverse_lazy("misiones:insertar_mision") #Rediccionar luego de insertar
class EditarMision(generic.UpdateView):
    model=mision #Modelo de la vista
    template_name="mision/insertar_mision.html" #Donde esta la plantilla
    context_object_name="cosa"
    form_class=misionForm #Formulario creado en django
    success_url=reverse_lazy("misiones:insertar_mision") #Rediccionar luego de insertar
class BorrarMision(generic.DeleteView):
    model=mision 
    template_name="mision/borrar_mision.html" 
    context_object_name="cosa"
    form_class=misionForm 
    success_url=reverse_lazy("misiones:listar_mision") 