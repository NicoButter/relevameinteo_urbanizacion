from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Localidad


from .forms import StreetForm

@login_required
def add_street(request):
    localidad = None
    if request.user.groups.exists():
        grupo = request.user.groups.first()
        localidad, _ = Localidad.objects.get_or_create(nombre=grupo.name)

    if request.method == 'POST':
        form = StreetForm(request.POST)
        if form.is_valid():
            
            street = form.save(commit=False)
            
            # Obtener el grupo del usuario actual
            user_group = request.user.groups.first()
            if user_group:
                street.distrito = user_group.name
            
            street.save()
            messages.success(request, 'Calle cargada con éxito.')
            return redirect('core')
    else:
        form = StreetForm()
    return render(request, 'streets/add_street.html', {'form': form})
