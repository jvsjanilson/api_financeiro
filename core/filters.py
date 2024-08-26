import django_filters
from django.db.models import Q
from core.models import Contato, Formapagamento, Conta


class ContatoFilter(django_filters.FilterSet):
    class Meta:
        model = Contato
        fields = "__all__"


class FormapagamentoFilter(django_filters.FilterSet):
    class Meta:
        model = Formapagamento
        fields = "__all__"


class ContaFilter(django_filters.FilterSet):
    descricao = django_filters.CharFilter(lookup_expr="icontains", field_name="descricao")
    numero_banco = django_filters.CharFilter(lookup_expr="iexact", field_name="numero_banco")
    numero_agencia = django_filters.CharFilter(lookup_expr="iexact", field_name="numero_agencia")
    numero_conta = django_filters.CharFilter(lookup_expr="iexact", field_name="numero_conta")

    class Meta:
        model = Conta
        fields = {}

    
