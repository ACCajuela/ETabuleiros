from rest_framework import serializers
from etabuleiros.models import Produto, ImagemProduto

class ProdutoRecomendadoSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(source='nome_prod')  # Mapeia nome_prod para nome
    imagem_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Produto
        fields = ['nome', 'imagem_url']  # Campos que serão retornados
    
    def get_imagem_url(self, obj):
        # Obtém a primeira imagem ordenada pelo campo 'ordem'
        primeira_imagem = ImagemProduto.objects.filter(prod_id=obj.prod_id).order_by('ordem').first()
        return primeira_imagem.caminho_imagem if primeira_imagem else None