from django.shortcuts import render
from core.views import BaseUserViewSet
from financeiro.models import Receber
from financeiro.serializers import ReceberSerializer
from financeiro.permissions import ReceberPermission
from financeiro.filters import ReceberFilter
from rest_framework.permissions import IsAuthenticated


class ReceberViewSet(BaseUserViewSet):
    queryset = Receber.objects.all()
    serializer_class = ReceberSerializer
    permission_classes = [IsAuthenticated, ReceberPermission]
    search_fields = ["documento", "contato__nome"]
    filter_order_by = ["documento", "contato__nome"]
    filterset_class = ReceberFilter