from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StreetForm

@login_required
def add_street(request):
    if request.method == 'POST':
        form = StreetForm(request.POST)
        if form.is_valid():
            street = form.save(commit=False)
            street.longitud_en_metros = street.altura_final / 100
            street.save()
            return redirect('core')
    else:
        form = StreetForm()
    return render(request, 'streets/add_street.html', {'form': form})
