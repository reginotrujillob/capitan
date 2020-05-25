from django.urls import path
from personas.views import  ListarCompañeros, ListarPersonas,InsertarPersona,EditarPersona, BorrarPersona,ListarAliados,ListarSalvadas,ListarEnemigos,ListarPatrocinadores

urlpatterns = [
    path('personas', ListarPersonas.as_view(), name='listar_personas'),
    path('personas/new', InsertarPersona.as_view(), name='insertar_persona'),
    path('personas/edit<int:pk>', EditarPersona.as_view(), name='editar_persona'),
    path('personas/delete<int:pk>', BorrarPersona.as_view(), name='borrar_persona'),
    path('personas>', ListarAliados.as_view(), name='listar_aliados'),
    path('personas>>', ListarEnemigos.as_view(), name='listar_enemigo'),
    path('personas>>>', ListarSalvadas.as_view(), name='listar_salvadas'),
    path('personas>>>>', ListarPatrocinadores.as_view(), name='listar_patrocinadores'),
    path('personas>>>>>', ListarCompañeros.as_view(), name='listar_compañeros'),



]