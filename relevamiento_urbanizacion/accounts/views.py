from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core')  # Redirige a la página principal después de iniciar sesión
        else:
            messages.error(request, 'Credenciales incorrectas. Por favor, intenta nuevamente.')
            return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/login.html')
