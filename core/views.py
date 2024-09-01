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
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from core.filters import ContatoFilter, FormapagamentoFilter, ContaFilter
from rest_framework.decorators import action


class BaseUserViewSet(ModelViewSet):
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ContatoViewSet(BaseUserViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    permission_classes = [IsAuthenticated, ContatoPermission]
    search_fields = [
        "nome",
        "telefone",
        "celular",
        "endereco",
        "bairro",
        "cidade",
        "complemento",
        "cpf_cnpj",
    ]
    filter_order_by = ["nome"]
    filterset_class = ContatoFilter

    def list(self, request, *args, **kwargs):

        if "all" in request.query_params:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        return super().list(request, *args, **kwargs)


class FormapagamentoViewSet(BaseUserViewSet):
    queryset = Formapagamento.objects.all()
    serializer_class = FormapagamentoSerializer
    permission_classes = [IsAuthenticated, FormapagamentoPermission]
    search_fields = ["codigo", "descricao"]
    filter_order_by = ["codigo", "descricao"]
    filterset_class = FormapagamentoFilter

    def list(self, request, *args, **kwargs):

        if "all" in request.query_params:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        return super().list(request, *args, **kwargs)


class ContaViewSet(BaseUserViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
    permission_classes = [IsAuthenticated, ContaPermission]
    search_fields = ["descricao", "numero_conta", "numero_agencia", "numero_banco"]
    filter_order_by = ["descricao", "numero_conta", "numero_agencia", "numero_banco"]
    filterset_class = ContaFilter

    def list(self, request, *args, **kwargs):

        if "all" in request.query_params:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        return super().list(request, *args, **kwargs)
