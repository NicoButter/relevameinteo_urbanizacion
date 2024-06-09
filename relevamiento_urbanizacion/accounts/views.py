from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
# from .forms import RegisterForm

# def register_view(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')  # Asegúrate de tener una vista 'home' configurada
#     else:
#         form = RegisterForm()
#     return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core')
        else:
            # mensaje de error
            messages.error(request, 'Usuario no registrado. Si es un error por favor, comuníquese con el servicio de atención al cliente.')
            return redirect('login')

    return redirect('login')
