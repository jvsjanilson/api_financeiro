import django_filters
from financeiro.models import Receber

class ReceberFilter(django_filters.FilterSet):
    documento = django_filters.CharFilter(lookup_expr="icontains", field_name="documento")  
    contato__nome = django_filters.CharFilter(lookup_expr="icontains", field_name="contato__nome")
    data_emissao = django_filters.DateFromToRangeFilter(field_name="data_emissao")
    data_vencimento = django_filters.DateFromToRangeFilter(field_name="data_vencimento")
    data_pagamento = django_filters.DateFromToRangeFilter(field_name="data_pagamento")
    valor = django_filters.NumericRangeFilter(field_name="valor")
    status = django_filters.CharFilter(lookup_expr="iexact", field_name="status")
    class Meta:
        model = Receber
        fields = {}
        