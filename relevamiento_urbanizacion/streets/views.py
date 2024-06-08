from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StreetForm

@login_required
def add_street(request):
    if request.method == 'POST':
        form = StreetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core')  # Redirige al core después de guardar
    else:
        form = StreetForm()
    return render(request, 'streets/add_street.html', {'form': form})
