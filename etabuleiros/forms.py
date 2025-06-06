# meuapp/forms.py
from django import forms
from .models import Produto  # Importe seu modelo

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'  # Inclui todos os campos do modelo
        
        # Opcional: personalizar widgets (aparência dos campos)
        widgets = {
            'descri': forms.Textarea(attrs={'rows': 3}),  # Textarea para descrição
            'data_criacao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        
        # Opcional: rótulos personalizados
        labels = {
            'nome_prod': 'Nome do Produto',
            'qtd': 'Quantidade em Estoque',
        }