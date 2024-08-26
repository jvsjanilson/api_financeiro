from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from core.models import Contato, Formapagamento, Conta
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
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


class BaseUserViewSet(ModelViewSet):

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ContatoViewSet(BaseUserViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    permission_classes = [IsAuthenticated, ContatoPermission]
    filter_class = ContatoFilter


class FormapagamentoViewSet(BaseUserViewSet):
    queryset = Formapagamento.objects.all()
    serializer_class = FormapagamentoSerializer
    permission_classes = [IsAuthenticated, FormapagamentoPermission]
    filter_class = FormapagamentoFilter


class ContaViewSet(BaseUserViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
    permission_classes = [IsAuthenticated, ContaPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["descricao", "numero_conta", "numero_agencia", "numero_banco"]
    filter_order_by = ["descricao", "numero_conta", "numero_agencia", "numero_banco"]
    filterset_class = ContaFilter
  
