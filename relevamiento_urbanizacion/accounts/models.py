from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    dni = models.CharField(max_length=10, unique=True)
    groups = models.ManyToManyField(Group, related_name='users', verbose_name='User groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='users', verbose_name='User permissions', blank=True)
    localidad = models.ForeignKey('Localidad', on_delete=models.CASCADE, related_name='users')

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'


class PhoneNumber(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='phone_numbers')
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.phone_number


class Localidad(models.Model):
    nombre = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre