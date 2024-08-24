from rest_framework import serializers
from core.models import Contato, Formapagamento, Conta


class BaseSerializer(serializers.ModelSerializer):

    def save(self, **kwargs):
        kwargs["user"] = self.context["request"].user
        return super().save(**kwargs)


class ContatoSerializer(BaseSerializer):
    class Meta:
        model = Contato
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
        }


class FormapagamentoSerializer(BaseSerializer):
    class Meta:
        model = Formapagamento
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
        }


class ContaSerializer(BaseSerializer):
    class Meta:
        model = Conta
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
        }
