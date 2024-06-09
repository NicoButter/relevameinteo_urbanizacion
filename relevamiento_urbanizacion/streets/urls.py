from django.urls import path
from .views import add_street

urlpatterns = [
    path('add/', add_street, name='add_street')
]