from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from financeiro.models import Titulo


class ReceberSerializer(ModelSerializer):
    conta_numero = serializers.CharField(source="conta.numero_conta", read_only=True)
    contato_nome = serializers.CharField(source="contato.nome", read_only=True)
    formapagamento_descricao = serializers.CharField(
        source="formapagamento.descricao", read_only=True
    )

    class Meta:
        model = Titulo
        # fields = "__all__"
        exclude = ["created_at", "updated_at"]
        extra_kwargs = {
            "user": {"read_only": True},
        }


class BaixaReceberSerializer(serializers.Serializer):
    data_pagamento = serializers.DateField(required=True)
