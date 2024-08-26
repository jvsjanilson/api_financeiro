from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.models import Contato, Formapagamento, Conta
from django.core.validators import MaxLengthValidator


class ContatoSerializer(ModelSerializer):
    class Meta:
        model = Contato
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
        }


class FormapagamentoSerializer(ModelSerializer):
    class Meta:
        model = Formapagamento
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
        }


class ContaSerializer(ModelSerializer):
    numero_banco = serializers.CharField(validators=[MaxLengthValidator(3)])

    class Meta:
        model = Conta
        fields = (
            "id",
            "numero_conta",
            "numero_banco",
            "numero_agencia",
            "descricao",
            "saldo",
        )
        extra_kwargs = {
            "user": {"read_only": True},
        }
