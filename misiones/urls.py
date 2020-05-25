from django.urls import path
from misiones.views import ListarMision,InsertarMision,EditarMision, BorrarMision

urlpatterns = [
    path('misiones', ListarMision.as_view(), name='listar_mision'),
    path('misiones/new', InsertarMision.as_view(), name='insertar_mision'),
    path('misiones/edit<int:pk>', EditarMision.as_view(), name='editar_mision'),
    path('misiones/delete<int:pk>', BorrarMision.as_view(), name='borrar_mision'),
]