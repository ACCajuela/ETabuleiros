from rest_framework import serializers
from etabuleiros.models import Produto, ImagemProduto
from .models import Usuario
from django.contrib.auth import authenticate

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
    class Meta:
        model = Usuario
        fields = ['user_id', 'email', 'nome', 'cpf', 'dataNasc', 'telefone', 'endereco', 'tipo']
        read_only_fields = ['user_id', 'tipo']

class RegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['email', 'password', 'nome', 'cpf', 'dataNasc', 'telefone', 'endereco']

    def create(self, validated_data):
        return Usuario.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Email ou senha inválidos.")