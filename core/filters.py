import django_filters
from django.db.models import Q
from core.models import Contato, Formapagamento, Conta


class ContatoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr="icontains", field_name="nome")
    telefone = django_filters.CharFilter(lookup_expr="icontains", field_name="telefone")
    celular = django_filters.CharFilter(lookup_expr="icontains", field_name="celular")
    endereco = django_filters.CharFilter(lookup_expr="icontains", field_name="endereco")
    
    class Meta:
        model = Contato
        fields ={}


class FormapagamentoFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr="iexact", field_name="codigo")
    descricao = django_filters.CharFilter(lookup_expr="icontains", field_name="descricao")
    class Meta:
        model = Formapagamento
        fields = {}


class ContaFilter(django_filters.FilterSet):
    descricao = django_filters.CharFilter(lookup_expr="icontains", field_name="descricao")
    numero_banco = django_filters.CharFilter(lookup_expr="iexact", field_name="numero_banco")
    numero_agencia = django_filters.CharFilter(lookup_expr="iexact", field_name="numero_agencia")
    numero_conta = django_filters.CharFilter(lookup_expr="iexact", field_name="numero_conta")

    class Meta:
        model = Conta
        fields = {}

    
