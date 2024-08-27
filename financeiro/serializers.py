from rest_framework.serializers import ModelSerializer
from rest_framework import serializers 
from financeiro.models import Receber


class ReceberSerializer(ModelSerializer):
    class Meta:
        model = Receber
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
        }