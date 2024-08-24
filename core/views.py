from rest_framework.viewsets import ModelViewSet
from core.models import Contato, Formapagamento, Conta
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from core.serializers import (
    ContatoSerializer,
    FormapagamentoSerializer,
    ContaSerializer,
)
from core.permissions import (
    ContatoPermission,
    FormapagamentoPermission,
    ContaPermission,
)

from core.filters import ContatoFilter, FormapagamentoFilter, ContaFilter


class ContatoViewSet(ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    permission_classes = [IsAuthenticated, IsAdminUser, ContatoPermission]
    filter_class = ContatoFilter


class FormapagamentoViewSet(ModelViewSet):
    queryset = Formapagamento.objects.all()
    serializer_class = FormapagamentoSerializer
    permission_classes = [IsAuthenticated, IsAdminUser, FormapagamentoPermission]
    filter_class = FormapagamentoFilter


class ContaViewSet(ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
    permission_classes = [IsAuthenticated, IsAdminUser, ContaPermission]
    filter_class = ContaFilter
