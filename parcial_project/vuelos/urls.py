from django.urls import path
from .views import InicioView, RegistrarVueloView, ListarVuelosView, EstadisticasVuelosView

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('registrar/', RegistrarVueloView.as_view(), name='registrar_vuelo'),
    path('listar/', ListarVuelosView.as_view(), name='listar_vuelos'),
    path('estadisticas/', EstadisticasVuelosView.as_view(), name='estadisticas_vuelos'),
]