from rest_framework import serializers
from etabuleiros.models import Produto, ImagemProduto, Usuario
from django.contrib.auth.hashers import make_password

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

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    dataNasc = serializers.DateTimeField(format='%Y-%m-%d', input_formats=['%Y-%m-%d'])

    class Meta:
        model = Usuario
        fields = [
            'email', 'nome', 'password', 'password2', 
            'cpf', 'dataNasc', 'telefone', 'endereco'
        ]
        extra_kwargs = {
            'nome': {'required': True},
            'cpf': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "As senhas não coincidem."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        validated_data['password'] = make_password(validated_data['password'])
        return Usuario.objects.create(**validated_data)