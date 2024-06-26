from django.shortcuts import render
from streets.models import Street

def lista_calles(request):
    streets = Street.objects.all()  # Ajusta esto según tu modelo y necesidades de filtro
    return render(request, 'ver_calles/lista_calles.html', {'streets': streets})
