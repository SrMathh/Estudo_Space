from django.db import models

class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.TextField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(max_length=100, null=False, blank=False)
    def __str__(self):
        return f"Fotografia [nome = {self.nome}]"
