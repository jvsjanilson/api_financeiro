from django.shortcuts import render
from core.views import BaseUserViewSet
from financeiro.models import Receber
from financeiro.serializers import ReceberSerializer
from financeiro.permissions import ReceberPermission
from financeiro.filters import ReceberFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class ReceberViewSet(BaseUserViewSet):
    queryset = Receber.objects.all()
    serializer_class = ReceberSerializer
    permission_classes = [IsAuthenticated, ReceberPermission]
    search_fields = ["documento", "contato__nome"]
    filter_order_by = ["documento", "contato__nome"]
    filterset_class = ReceberFilter

    @action(detail=True, methods=["post"], url_path="baixar-receber")
    def baixar_receber(self, request, pk=None):
        receber = get_object_or_404(Receber, pk=pk)
        data_pagamento = request.data.get("data_pagamento")

        if not data_pagamento:
            return Response(
                {"detail": "Este campo é obrigatório."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        receber.data_pagamento = data_pagamento
        receber.status = "P"
        receber.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"], url_path="estornar-receber")
    def estornar_receber(self, request, pk=None):
        receber = get_object_or_404(Receber, pk=pk)
        receber.data_pagamento = None
        receber.status = "A"
        receber.save()
        return Response(status=status.HTTP_200_OK)
