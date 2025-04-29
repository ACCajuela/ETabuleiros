from django.db import models
from django.utils import timezone

class Carrinho(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(default=timezone.now) 
