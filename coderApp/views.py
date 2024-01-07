from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente

# Create your views here..

def guardar_cliente(request):
    
    cliente = Cliente()
    cliente.save()
    return HttpResponse("Cliente satisfecho!") # View no renderizada

def guardar_programadores(request):
     return render(request,"plantilla.html")# View renderizada(Mejor)