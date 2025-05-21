from django.db import models
from django.utils import timezone
from etabuleiros.models import Produto, Usuario

class Carrinho(models.Model):
    usuario = models.ForeignKey('etabuleiros.Usuario', on_delete=models.CASCADE)
    produto = models.ForeignKey('etabuleiros.Produto', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(default=timezone.now) 
