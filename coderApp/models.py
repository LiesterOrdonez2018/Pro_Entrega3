from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    email=models.EmailField()
    
class Programadores(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    curso=models.CharField(max_length=20)
    email=models.EmailField()
    
class Profesores(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    celular=models.IntegerField()
    