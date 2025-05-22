from rest_framework import serializers
from etabuleiros.models import Produto, ImagemProduto

class ProdutoRecomendadoSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(source='nome_prod')
    imagem_url = serializers.SerializerMethodField()

    class Meta:
        model = Produto
        fields = ['nome', 'imagem_url']

    def get_imagem_url(self, obj):
        imagem = ImagemProduto.objects.filter(prod_id=obj.prod_id).order_by('ordem').first()
        if imagem and imagem.imagem:
            return imagem.imagem.url
        return None