from django.urls import include, path
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name = 'index'),
    path('imagem/<int:foto_id>', imagem, name = 'imagem')
]