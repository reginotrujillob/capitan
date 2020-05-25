from django.shortcuts import render
from personas.models import persona
from django.views import generic
from django.views.generic import ListView
from personas.forms import personaForm
from django.urls import reverse_lazy

# Create your views here.
class ListarPersonas(generic.ListView):
    model=persona
    queryset=persona.objects.all()
    template_name="persona/listar_persona.html"
    context_object_name="cosa"
class InsertarPersona(generic.CreateView):
    model=persona #Modelo de la vista
    template_name="persona/insertar_persona.html" #Donde esta la plantilla
    context_object_name="cosa"
    form_class=personaForm #Formulario creado en django
    success_url=reverse_lazy("personas:listar_personas") #Rediccionar luego de insertar
class EditarPersona(generic.UpdateView):
    model=persona #Modelo de la vista
    template_name="persona/insertar_persona.html" #Donde esta la plantilla
    context_object_name="cosa"
    form_class=personaForm #Formulario creado en django
    success_url=reverse_lazy("personas:listar_personas") #Rediccionar luego de insertar
class BorrarPersona(generic.DeleteView):
    model=persona 
    template_name="persona/borrar_persona.html" 
    context_object_name="cosa"
    form_class=personaForm 
    success_url=reverse_lazy("personas:listar_personas") 
class ListarEnemigos(generic.ListView):
 
    queryset = persona.objects.filter(relacion='enemigo')
    template_name="persona/listar_persona.html"
    context_object_name="cosa"    
class ListarSalvadas(generic.ListView):

    context_object_name="cosa"
    queryset = persona.objects.filter(relacion='salvar')
    template_name="persona/listar_persona.html"
class ListarPatrocinadores(generic.ListView):
 
    queryset = persona.objects.filter(relacion='patrocinador')
    template_name="persona/listar_persona.html"
    context_object_name="cosa"
class ListarAliados(generic.ListView):
    context_object_name="cosa"    
    queryset=persona.objects.filter(relacion='aliado')
    template_name="persona/listar_persona.html"
class ListarCompañeros(generic.ListView):
    context_object_name="cosa"    
    queryset=persona.objects.filter(relacion='compañero')
    template_name="persona/listar_persona.html"