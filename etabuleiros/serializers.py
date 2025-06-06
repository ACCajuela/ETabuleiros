from rest_framework import serializers
from etabuleiros.models import Produto, ImagemProduto, Usuario, Editora, Categoria
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from datetime import date

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

User = get_user_model()

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
        extra_kwargs = {
            'prod_id': {'read_only': True},
            'data_criacao': {'read_only': True}
        }

class PerfilSerializer(serializers.ModelSerializer):
    idade = serializers.SerializerMethodField()
    
    class Meta:
        model = Usuario
        fields = [
            'nome',
            'idade',
            'cpf',
            'endereco',
            'telefone',
            'email'
        ]
    
    def get_idade(self, obj):
        if obj.dataNasc:
            today = date.today()
            return today.year - obj.dataNasc.year - ((today.month, today.day) < (obj.dataNasc.month, obj.dataNasc.day))
        return None

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )

        if not user:
            raise serializers.ValidationError("Credenciais inválidas")

        attrs['user'] = user
        return attrs