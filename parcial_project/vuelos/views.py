from django.shortcuts import render, redirect
from django.views import View
from .forms import FlightForm
from .models import flight
from django.db.models import Avg, Count

# Create your views here.
class InicioView(View):
    def get(self, request):
        return render(request, 'inicio.html')

class RegistrarVueloView(View):
    def get(self, request):
        form = FlightForm()
        return render(request, 'registrar_vuelo.html', {'form': form})

    def post(self, request):
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
        return render(request, 'registrar_vuelo.html', {'form': form})

class ListarVuelosView(View):
    def get(self, request):
        vuelos = flight.objects.all().order_by('precio')
        return render(request, 'listar_vuelos.html', {'vuelos': vuelos})

class EstadisticasVuelosView(View):
    def get(self, request):
        nacionales = flight.objects.filter(tipo='Nacional').count()
        internacionales = flight.objects.filter(tipo='Internacional').count()
        promedio_nacionales = flight.objects.filter(tipo='Nacional').aggregate(Avg('precio'))['precio__avg'] or 0

        return render(request, 'estadisticas_vuelos.html', {
            'nacionales': nacionales,
            'internacionales': internacionales,
            'promedio_nacionales': promedio_nacionales,
        })