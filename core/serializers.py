from rest_framework.serializers import ModelSerializer
from core.models import Contato, Formapagamento, Conta


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
    class Meta:
        model = Conta
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
        }
