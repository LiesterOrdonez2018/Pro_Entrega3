from django.urls import path, include
from coderApp.views import guardar_cliente, guardar_programadores


urlpatterns = [
    
    path('', guardar_cliente),
    path('programadores/', guardar_programadores),
]
