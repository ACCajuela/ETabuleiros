from rest_framework import serializers
from etabuleiros.models import Produto

class ProdutoRecomendadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco', 'descricao_curta', 'imagem_url']  # Ajuste com os campos que você quer retornar
        
    # Exemplo de campo customizado
    descricao_curta = serializers.SerializerMethodField()
    
    def get_descricao_curta(self, obj):
        return obj.descricao[:100] + '...' if len(obj.descricao) > 100 else obj.descricao