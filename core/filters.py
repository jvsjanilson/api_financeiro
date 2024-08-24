import django_filters
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
    class Meta:
        model = Conta
        fields = "__all__"
