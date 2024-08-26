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
    search = django_filters.CharFilter(method="filter_by_search")

    class Meta:
        model = Conta
        fields = {}

    def filter_by_search(self, queryset, name, value):
        return queryset.filter(
            Q(descricao__icontains=value)
            | Q(numero_conta__icontains=value)
            | Q(numero_agencia__icontains=value)
        )
