from rest_framework import serializers
from core.models import Contato, Formapagamento, Conta


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = "__all__"


class FormapagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formapagamento
        fields = "__all__"


class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = "__all__"
