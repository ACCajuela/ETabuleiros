# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from django.core.validators import RegexValidator, EmailValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser, UserManager  # Adicione UserManager aqui

class Produto(models.Model):
    prod_id = models.AutoField(primary_key=True)
    nome_prod = models.CharField(max_length=100, null=True, blank=True)
    qtd = models.IntegerField(null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cat = models.ForeignKey('Categoria', on_delete=models.CASCADE, db_column='cat_id')
    editora = models.ForeignKey('Editora', on_delete=models.SET_NULL, null=True, blank=True, db_column='editora_id')
    tempo_de_jogo = models.IntegerField(null=True, blank=True)
    numero_jogadores = models.CharField(max_length=20, null=True, blank=True)
    itens_inclusos = models.CharField(max_length=200, null=True, blank=True)
    descri = models.CharField(max_length=100, null=True, blank=True)
    recomendado = models.BooleanField(
        default=False,
        verbose_name="Recomendado",
        help_text="Marcar como produto recomendado"
    )
    
    CLAS_IND_CHOICES = [
        ('L', 'L'),
        ('10', '10'),
        ('12', '12'),
        ('14', '14'),
        ('16', '16'),
        ('18', '18'),
    ]
    clas_ind = models.CharField(
        max_length=2,
        choices=CLAS_IND_CHOICES,
        null=True,
        blank=True
    )

    autor = models.CharField(max_length=200, null=True, blank=True)
    categoria = models.TextField(null=True, blank=True)
    data_criacao = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'produtos'       

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)

class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)

class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)

class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class Usuario(AbstractUser):
    TIPO_CHOICES = [
        ('cliente', 'Cliente'),
        ('funcionario', 'Funcionário'),
        ('admin', 'Administrador'),
    ]
    
    
    
    # Removendo o username pois usaremos email
    username = None
    
    #campo de login
    email = models.EmailField(unique=True)
    
    # Campos adicionais
    user_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=True, blank=True)
    
    cpf_validator = RegexValidator(
        regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
        message='CPF deve estar no formato XXX.XXX.XXX-XX'
    )
    cpf = models.CharField(
        max_length=14,
        unique=True,
        null=True,
        blank=True,
        validators=[cpf_validator]
    )
    
    dataNasc = models.DateTimeField(null=True, blank=True, db_column='dataNasc')
    
    telefone_validator = RegexValidator(
        regex=r'^\(\d{2}\) \d{4,5}-\d{4}$',
        message='Telefone deve estar no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX'
    )
    telefone = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        validators=[telefone_validator]
    )
    
    endereco = models.TextField(null=True, blank=True)
    
    tipo = models.CharField(
        max_length=11,
        choices=TIPO_CHOICES,
        default='cliente'
    )

    # Configurações para autenticação por email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cpf', 'nome','username']

    objects = UserManager()

    class Meta:
        db_table = 'Usuario'  # Usando o mesmo nome da tabela original
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
    
    def __str__(self):
        return self.nome or self.email
    
    def save(self, *args, **kwargs):
        if not self.nome and (self.first_name or self.last_name):
            self.nome = f"{self.first_name} {self.last_name}".strip()
        super().save(*args, **kwargs)
        
class AvaliacaoProduto(models.Model):
    avaliacao_id = models.AutoField(primary_key=True)
    ava_prod = models.ForeignKey(
        'Produto',  # or your actual product model name
        on_delete=models.CASCADE,
        db_column='ava_prod_id',
        db_index=True,
        related_name='avaliacoes'
    )
    ava_user = models.ForeignKey(
        'Usuario',  # or your actual user model name
        on_delete=models.CASCADE,
        db_column='ava_user_id',
        db_index=True,
        related_name='avaliacoes_produtos'
    )
    nota = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    comentario = models.TextField(null=True, blank=True)
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'avaliacoes_produtos'
        verbose_name = 'Avaliação de Produto'
        verbose_name_plural = 'Avaliações de Produtos'
        constraints = [
            models.CheckConstraint(
                check=models.Q(nota__gte=1) & models.Q(nota__lte=5),
                name='avaliacoes_produtos_chk_1'
            )
        ]

    def __str__(self):
        return f"Avaliação {self.avaliacao_id} - Produto {self.ava_prod_id}"
    
class CarrinhoCompras(models.Model):
    carrinho_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        'Usuario',  # Replace with your actual user model path if different
        on_delete=models.CASCADE,
        db_column='user_id',
        db_index=True,
        related_name='carrinhos'
    )
    produto = models.ForeignKey(
        'Produto',  # Replace with your actual product model path if different
        on_delete=models.CASCADE,
        db_column='prod_id',
        db_index=True,
        related_name='carrinhos'
    )
    quantidade = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1)]
    )
    data_adicao = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'carrinho_compras'
        verbose_name = 'Carrinho de Compras'
        verbose_name_plural = 'Carrinhos de Compras'
        constraints = [
            models.CheckConstraint(
                check=models.Q(quantidade__gt=0),
                name='car_compras_chk_1'
            )
        ]
        # Optional: Prevent duplicate product entries for same user
        unique_together = ('user', 'produto',)

    def __str__(self):
        return f"Carrinho {self.carrinho_id} - User {self.user_id}"
    
class Categoria(models.Model):
    cat_id = models.AutoField(primary_key=True)
    nome_categoria = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        error_messages={
            'unique': 'Esta categoria já existe.'
        }
    )

    class Meta:
        db_table = 'categorias'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        # Equivalent to UNIQUE KEY in SQL
        constraints = [
            models.UniqueConstraint(
                fields=['nome_categoria'],
                name='nome_categoria_unico'
            )
        ]

    def __str__(self):
        return self.nome_categoria
    
class CupomDesconto(models.Model):
    cupom_id = models.AutoField(primary_key=True)
    codigo = models.CharField(
        _('Código do Cupom'),
        max_length=50,
        unique=True,
        db_index=True,
        error_messages={
            'unique': _('Este código de cupom já existe.')
        }
    )
    desconto = models.DecimalField(
        _('Percentual de Desconto'),
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0.01),
            MaxValueValidator(100)
        ]
    )
    data_expiracao = models.DateField(
        _('Data de Expiração'),
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'cupons_desconto'
        verbose_name = _('Cupom de Desconto')
        verbose_name_plural = _('Cupons de Desconto')
        constraints = [
            models.CheckConstraint(
                check=models.Q(desconto__gt=0) & models.Q(desconto__lte=100),
                name='cupons_desconto_chk_1'
            )
        ]

    def __str__(self):
        return f"{self.codigo} - {self.desconto}%"

    @property
    def esta_valido(self):
        """Verifica se o cupom ainda está válido"""
        if self.data_expiracao:
            from django.utils import timezone
            return timezone.now().date() <= self.data_expiracao
        return True
    
class Devolucao(models.Model):
    class StatusDevolucao(models.TextChoices):
        PENDENTE = 'pendente', _('Pendente')
        APROVADA = 'aprovada', _('Aprovada')
        RECUSADA = 'recusada', _('Recusada')

    devolucao_id = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(
        'Pedido',  # Replace with your actual order model path
        on_delete=models.PROTECT,
        db_column='ped_id',
        related_name='devolucoes'
    )
    produto = models.ForeignKey(
        'Produto',  # Replace with your actual product model path
        on_delete=models.PROTECT,
        db_column='prod_id',
        related_name='devolucoes'
    )
    motivo = models.TextField(
        _('Motivo da Devolução'),
        blank=True,
        null=True
    )
    status_devolucao = models.CharField(
        _('Status da Devolução'),
        max_length=8,
        choices=StatusDevolucao.choices,
        default=StatusDevolucao.PENDENTE,
        db_index=True
    )
    data_solicitacao = models.DateTimeField(
        _('Data de Solicitação'),
        auto_now_add=True
    )

    class Meta:
        db_table = 'devolucoes'
        verbose_name = _('Devolução')
        verbose_name_plural = _('Devoluções')
        indexes = [
            models.Index(fields=['pedido'], name='devolucao_ped_id_idx'),
            models.Index(fields=['produto'], name='devolucao_prod_id_idx'),
        ]

    def __str__(self):
        return f"Devolução #{self.devolucao_id} - {self.get_status_devolucao_display()}"

    @property
    def pode_ser_processada(self):
        """Verifica se a devolução está no status pendente"""
        return self.status_devolucao == self.StatusDevolucao.PENDENTE

class Duvida(models.Model):
    duvida_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(
        'Usuario',  # Replace with your user model path (e.g. 'etabuleiros.Usuario')
        on_delete=models.SET_NULL,
        db_column='duvida_user_id',
        related_name='duvidas_enviadas',
        null=True,
        blank=True
    )
    respondido_por = models.ForeignKey(
        'Usuario',  # Same user model as above
        on_delete=models.SET_NULL,
        db_column='duvida_resposta_id',
        related_name='duvidas_respondidas',
        null=True,
        blank=True
    )
    produto = models.ForeignKey(
        'Produto',  # Replace with your product model path
        on_delete=models.CASCADE,
        db_column='duvida_prod_id',
        related_name='duvidas',
        null=True,
        blank=True
    )
    pergunta = models.TextField(
        _('Pergunta'),
        db_column='duvida'  # Keeps original column name
    )
    resposta = models.TextField(
        _('Resposta'),
        blank=True,
        null=True
    )
    data_criacao = models.DateTimeField(
        _('Data de Criação'),
        auto_now_add=True
    )
    data_resposta = models.DateTimeField(
        _('Data de Resposta'),
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'duvidas'
        verbose_name = _('Dúvida')
        verbose_name_plural = _('Dúvidas')
        indexes = [
            models.Index(fields=['usuario'], name='duvida_user_id_idx'),
            models.Index(fields=['respondido_por'], name='duvida_resposta_id_idx'),
            models.Index(fields=['produto'], name='FK_duvidas_produtos_idx'),
        ]

    def __str__(self):
        return f"Dúvida #{self.duvida_id} sobre {self.produto}"

    @property
    def foi_respondida(self):
        """Check if the question has been answered"""
        return bool(self.resposta) and bool(self.respondido_por)

    def save(self, *args, **kwargs):
        """Update answer date when response is added"""
        if self.resposta and not self.data_resposta:
            from django.utils import timezone
            self.data_resposta = timezone.now()
        super().save(*args, **kwargs)
               
class Editora(models.Model):
    editora_id = models.AutoField(
        primary_key=True,
        verbose_name=_('ID da Editora')
    )
    nome_editora = models.CharField(
        _('Nome da Editora'),
        max_length=100,
        unique=True,
        db_index=True,
        validators=[MinLengthValidator(2)],
        error_messages={
            'unique': _('Já existe uma editora com este nome.'),
            'min_length': _('O nome deve conter pelo menos 2 caracteres.')
        }
    )

    class Meta:
        db_table = 'editoras'
        verbose_name = _('Editora')
        verbose_name_plural = _('Editoras')
        ordering = ['nome_editora']
        constraints = [
            models.UniqueConstraint(
                fields=['nome_editora'],
                name='nome_editora_unico',
                condition=models.Q(nome_editora__isnull=False)
            )
        ]

    def __str__(self):
        return self.nome_editora

    def clean(self):
        """Additional validation at model level"""
        super().clean()
        if self.nome_editora:
            self.nome_editora = self.nome_editora.strip()
                
class Fornecedor(models.Model):
    fornecedor_id = models.AutoField(
        primary_key=True,
        verbose_name=_('ID do Fornecedor')
    )
    nome_fornecedor = models.CharField(
        _('Nome do Fornecedor'),
        max_length=255,
        validators=[MinLengthValidator(3)],
        help_text=_('Nome completo do fornecedor')
    )
    endereco = models.CharField(
        _('Endereço'),
        max_length=200,
        blank=True,
        null=True
    )
    telefone = models.CharField(
        _('Telefone'),
        max_length=20,
        blank=True,
        null=True,
        validators=[MinLengthValidator(8)]
    )
    email = models.EmailField(
        _('E-mail'),
        max_length=255,
        unique=True,
        blank=True,
        null=True,
        validators=[EmailValidator()],
        error_messages={
            'unique': _('Este e-mail já está cadastrado.')
        }
    )

    class Meta:
        db_table = 'fornecedores'
        verbose_name = _('Fornecedor')
        verbose_name_plural = _('Fornecedores')
        ordering = ['nome_fornecedor']
        constraints = [
            models.UniqueConstraint(
                fields=['email'],
                name='email_unico',
                condition=models.Q(email__isnull=False)
            )
        ]

    def __str__(self):
        return self.nome_fornecedor

    def clean(self):
        """Custom validation for phone number and email"""
        super().clean()
        
        if self.telefone:
            # Remove all non-digit characters
            self.telefone = re.sub(r'[^\d]', '', self.telefone)
            if len(self.telefone) < 8:
                raise ValidationError({
                    'telefone': _('O telefone deve conter pelo menos 8 dígitos.')
                })

    def save(self, *args, **kwargs):
        self.full_clean()  # Runs validations before saving
        super().save(*args, **kwargs)

    @property
    def contato(self):
        """Formatted contact information"""
        parts = []
        if self.telefone:
            parts.append(f"Tel: {self.telefone}")
        if self.email:
            parts.append(f"Email: {self.email}")
        return " | ".join(parts) if parts else _("Sem informações de contato")
    
class Frete(models.Model):
    frete_id = models.AutoField(
        primary_key=True,
        verbose_name=_('ID do Frete')
    )
    cep_destino = models.CharField(
        _('CEP de Destino'),
        max_length=9,
        validators=[MinLengthValidator(8)],
        help_text=_('Formato: 00000-000 ou 00000000')
    )
    peso = models.DecimalField(
        _('Peso (kg)'),
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    valor_frete = models.DecimalField(
        _('Valor do Frete'),
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    class Meta:
        db_table = 'fretes'
        verbose_name = _('Frete')
        verbose_name_plural = _('Fretes')
        ordering = ['-frete_id']

    def __str__(self):
        return f"Frete #{self.frete_id} - {self.cep_destino}"

    def clean(self):
        """Validate and format CEP"""
        super().clean()
        if self.cep_destino:
            # Remove all non-digit characters
            cep = re.sub(r'[^\d]', '', self.cep_destino)
            if len(cep) != 8:
                raise ValidationError(
                    {'cep_destino': _('CEP deve conter 8 dígitos.')}
                )
            # Format as 00000-000
            self.cep_destino = f"{cep[:5]}-{cep[5:]}"

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    @property
    def custo_por_kg(self):
        """Calculate cost per kilogram"""
        if self.peso > 0:
            return self.valor_frete / self.peso
        return 0
    
class FuncionarioPermissao(models.Model):
    func_perm_id = models.AutoField(
        primary_key=True,
        verbose_name=_('ID da Permissão de Funcionário')
    )
    funcionario = models.ForeignKey(
        'Usuario',  # Replace with your user model path (e.g. 'etabuleiros.Usuario')
        on_delete=models.CASCADE,
        db_column='func_id',
        related_name='permissoes_funcionario',
        verbose_name=_('Funcionário')
    )
    permissao = models.ForeignKey(
        'PermissaoFuncionario',  # Replace with your permission model path
        on_delete=models.CASCADE,
        db_column='permissao_id',
        related_name='funcionarios_com_permissao',
        verbose_name=_('Permissão')
    )

    class Meta:
        db_table = 'funcionarios_permissoes'
        verbose_name = _('Permissão de Funcionário')
        verbose_name_plural = _('Permissões de Funcionários')
        constraints = [
            models.UniqueConstraint(
                fields=['funcionario', 'permissao'],
                name='unique_funcionario_permissao'
            )
        ]
        indexes = [
            models.Index(fields=['funcionario'], name='func_permissoes_usuarios_idx'),
            models.Index(fields=['permissao'], name='permissao_id_idx'),
        ]

    def __str__(self):
        return f"{self.funcionario} - {self.permissao}"
    
class HistoricoNavegacao(models.Model):
    id_hist = models.AutoField(
        primary_key=True,
        verbose_name=_('ID do Histórico')
    )
    usuario = models.ForeignKey(
        'Usuario',  # Replace with your user model path (e.g. 'etabuleiros.Usuario')
        on_delete=models.CASCADE,
        db_column='user_id',
        related_name='historico_navegacao',
        verbose_name=_('Usuário')
    )
    produto = models.ForeignKey(
        'Produto',  # Replace with your product model path
        on_delete=models.CASCADE,
        db_column='prod_id',
        related_name='visualizacoes',
        verbose_name=_('Produto')
    )
    data_visualizacao = models.DateTimeField(
        _('Data de Visualização'),
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        db_table = 'historico_navegacao'
        verbose_name = _('Histórico de Navegação')
        verbose_name_plural = _('Histórico de Navegações')
        ordering = ['-data_visualizacao']
        indexes = [
            models.Index(fields=['usuario'], name='user_id_idx'),
            models.Index(fields=['produto'], name='prod_id_idx'),
        ]

    def __str__(self):
        return f"Visualização #{self.id_hist} - {self.usuario} em {self.produto}"

    @classmethod
    def registrar_visualizacao(cls, usuario, produto):
        """Creates a new navigation history record"""
        return cls.objects.create(usuario=usuario, produto=produto)

    @classmethod
    def visualizacoes_recentes(cls, usuario, limit=5):
        """Returns recent viewed products for a user"""
        return cls.objects.filter(usuario=usuario).select_related('produto') \
                         .order_by('-data_visualizacao')[:limit]

class HistoricoPagamento(models.Model):
    pagamento_id = models.AutoField(primary_key=True)
    ped = models.ForeignKey('Pedido', on_delete=models.CASCADE, db_column='ped_id')
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    METODO_PAGAMENTO_CHOICES = [
        ('credito', 'Crédito'),
        ('debito', 'Débito'),
        ('pix', 'Pix'),
    ]
    metodo_pagamento = models.CharField(
        max_length=7,
        choices=METODO_PAGAMENTO_CHOICES,
        null=True,
        blank=True
    )
    data_pagamento = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'historico_pagamentos'
        
class HistoricoPreco(models.Model):
    historico_preco_id = models.AutoField(primary_key=True)
    prod = models.ForeignKey('Produto', on_delete=models.CASCADE, db_column='prod_id')
    preco_antigo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    preco_novo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    data_alteracao = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'historico_precos'
        
class ImagemProduto(models.Model):
    imagem_id = models.AutoField(primary_key=True)
    prod = models.ForeignKey('Produto', on_delete=models.CASCADE, db_column='prod_id')
    caminho_imagem = models.CharField(max_length=255)
    ordem = models.IntegerField(default=1)

    class Meta:
        db_table = 'imagens_produtos'
        
class ListaDesejos(models.Model):
    id_des = models.AutoField(primary_key=True)
    id_des_user = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='id_des_user')
    data_alteracao_LD = models.DateTimeField(auto_now_add=True, null=True)
    id_des_prod = models.ForeignKey('Produto', on_delete=models.SET_NULL, null=True, db_column='id_des_prod', blank=True)

    class Meta:
        db_table = 'lista_desejos'
        
class Log(models.Model):
    log_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True, db_column='usuario_id', blank=True)
    acao = models.CharField(max_length=255)
    descricao = models.TextField(null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True, null=True)

    TIPO_USUARIO_CHOICES = [
        ('usuario', 'Usuário'),
        ('funcionario', 'Funcionário'),
        ('administrador', 'Administrador'),
    ]
    tipo_usuario = models.CharField(max_length=13, choices=TIPO_USUARIO_CHOICES)

    class Meta:
        db_table = 'logs'
        constraints = [
            models.CheckConstraint(
                check=models.Q(tipo_usuario='administrador'),
                name='logs_chk_1'
            )
        ]
        
class LogAcesso(models.Model):
    log_acesso_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True, db_column='usuario_id', blank=True)
    data_acesso = models.DateTimeField(auto_now_add=True, null=True)

    STATUS_ACESSO_CHOICES = [
        ('sucesso', 'Sucesso'),
        ('falha', 'Falha'),
    ]
    status_acesso = models.CharField(
        max_length=7,
        choices=STATUS_ACESSO_CHOICES,
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'logs_acesso'
        
class Notificacao(models.Model):
    notificacao_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='usuario_id')
    mensagem = models.TextField(null=True, blank=True)
    data_envio = models.DateTimeField(auto_now_add=True, null=True)
    lida = models.BooleanField(default=False)

    class Meta:
        db_table = 'notificacoes'
        
class Pedido(models.Model):
    ped_id = models.AutoField(primary_key=True)
    id_user_ped = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='id_user_ped')

    STATUS_PED_CHOICES = [
        ('em analise', 'Em Análise'),
        ('aprovado', 'Aprovado'),
        ('separado', 'Separado'),
        ('enviado', 'Enviado'),
        ('entregue', 'Entregue'),
    ]
    status_ped = models.CharField(
        max_length=10,
        choices=STATUS_PED_CHOICES,
        default='em analise'
    )

    FORMA_PAGAMENTO_CHOICES = [
        ('credito', 'Crédito'),
        ('debito', 'Débito'),
        ('pix', 'Pix'),
    ]
    forma_pagamento = models.CharField(
        max_length=7,
        choices=FORMA_PAGAMENTO_CHOICES
    )

    data_pedido = models.DateTimeField(auto_now_add=True, null=True)
    cod_rast = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'pedidos'   
        
class PedidoProduto(models.Model):
    ped_prod_id = models.AutoField(primary_key=True)
    ped = models.ForeignKey('Pedido', on_delete=models.CASCADE, db_column='ped_id')
    prod = models.ForeignKey('Produto', on_delete=models.CASCADE, db_column='prod_id')
    quantidade = models.IntegerField(validators=[MinValueValidator(1)])
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'pedido_produto'        

class PermissaoFuncionario(models.Model):
    perm_id = models.AutoField(primary_key=True)
    func = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='func_id')
    pode_editar_usuario = models.BooleanField(default=True)
    pode_editar_pedido = models.BooleanField(default=True)
    pode_ver_pagamento = models.BooleanField(default=False)

    class Meta:
        db_table = 'permissoes_funcionarios'

class ProdutoHistoricoNavegacao(models.Model):
    prod_hist_id = models.AutoField(primary_key=True)
    prod = models.ForeignKey('Produto', on_delete=models.CASCADE, db_column='prod_id')
    hist = models.ForeignKey('HistoricoNavegacao', on_delete=models.CASCADE, db_column='hist_id')

    class Meta:
        db_table = 'produtos_historico_navegacao'
        
class ProdutoListaDesejos(models.Model):
    prod_lista_id = models.AutoField(primary_key=True)
    prod = models.ForeignKey('Produto', on_delete=models.CASCADE, db_column='prod_id')
    lista = models.ForeignKey('ListaDesejos', on_delete=models.CASCADE, db_column='lista_id')

    class Meta:
        db_table = 'produtos_lista_desejos'
             
class Promocao(models.Model):
    promocao_id = models.AutoField(primary_key=True)
    nome_promocao = models.CharField(max_length=255, null=True, blank=True)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'promocoes'

    def clean(self):
        if self.desconto and (self.desconto <= 0 or self.desconto > 100):
            raise ValidationError('O desconto deve ser entre 0 e 100.')
        
class ReclamacaoSuporte(models.Model):
    RECLAMACAO_STATUS_CHOICES = [
        ('aberta', 'Aberta'),
        ('em andamento', 'Em andamento'),
        ('resolvida', 'Resolvida'),
    ]
    
    reclamacao_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='user_id')
    assunto = models.CharField(max_length=255, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=RECLAMACAO_STATUS_CHOICES, default='aberta')
    data_abertura = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user_respondeu = models.ForeignKey('Usuario', null=True, blank=True, related_name='respostas', on_delete=models.SET_NULL, db_column='user_respondeu_id')
    resposta = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'reclamacoes_suporte'

    def __str__(self):
        return f'Reclamação {self.reclamacao_id} - {self.status}'
