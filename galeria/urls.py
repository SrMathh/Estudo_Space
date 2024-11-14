from django.urls import include, path
from galeria.views import index, imagem, buscar

urlpatterns = [
    path('', index, name = 'index'),
    path('imagem/<int:foto_id>', imagem, name = 'imagem'),
    path('buscar', buscar, name='buscar'),
]