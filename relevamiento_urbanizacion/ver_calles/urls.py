from django.urls import path
from . import views

urlpatterns = [
    path('lista_calles/', views.lista_calles, name='lista_calles')
]
