from django.urls import path, include
from .views import login_view

urlpatterns = [
    path('', include('django.contrib.auth.urls'))
    # path('login/', login_view, name='login'),
]