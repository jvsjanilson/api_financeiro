from django.db import models
from core.choices import EstadoChoice
from django.core.validators import MinLengthValidator


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Contato(Base):
    nome = models.CharField(max_length=60, validators=[MinLengthValidator(2)])
    cpf_cnpj = models.CharField("CPF/CNPJ", max_length=14)
    endereco = models.CharField(max_length=60, null=True, blank=True)
    numero = models.CharField(max_length=20, null=True, blank=True)
    cep = models.CharField(max_length=9, null=True, blank=True)
    complemento = models.CharField(max_length=120, null=True, blank=True)
    bairro = models.CharField(max_length=60, null=True, blank=True)
    cidade = models.CharField(max_length=60, null=True, blank=True)
    estado = models.CharField(
        max_length=2, choices=EstadoChoice.choices, default=EstadoChoice.RN
    )
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    celular = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.nome


class Formapagamento(Base):
    codigo = models.CharField(max_length=3)
    descricao = models.CharField("Descrição", max_length=60)

    def __str__(self):
        return self.descricao


class Conta(Base):
    numero_conta = models.CharField(max_length=10)
    numero_banco = models.CharField(max_length=3)
    numero_agencia = models.CharField(max_length=7)
    descricao = models.CharField("Descrição", max_length=60)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.descricao
