from core.views import BaseUserViewSet
from financeiro.models import TituloReceber, TituloPagar
from financeiro.serializers import ReceberSerializer, PagarSerializer
from financeiro.permissions import ReceberPermission
from financeiro.filters import ReceberFilter, PagarFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.http import JsonResponse
from rest_framework import status
from django.shortcuts import get_object_or_404


class ReceberViewSet(BaseUserViewSet):
    queryset = TituloReceber.objects.all()
    serializer_class = ReceberSerializer
    permission_classes = [IsAuthenticated, ReceberPermission]
    search_fields = ["documento", "contato__nome"]
    filter_order_by = ["documento", "contato__nome"]
    filterset_class = ReceberFilter

    @action(detail=True, methods=["post"], url_path="baixar")
    def baixar(self, request, pk=None):
        receber = get_object_or_404(TituloReceber, pk=pk)
        data_pagamento = request.data.get("data_pagamento")

        if not data_pagamento:
            return JsonResponse(
                {"data_pagamento": ["Este campo é obrigatório."]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        receber.data_pagamento = data_pagamento
        receber.status = "P"
        receber.save()

        return JsonResponse({}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"], url_path="estornar")
    def estornar(self, request, pk=None):
        receber = get_object_or_404(TituloReceber, pk=pk)
        receber.data_pagamento = None
        receber.status = "A"
        receber.save()
        return JsonResponse({}, status=status.HTTP_200_OK)


class PagarViewSet(BaseUserViewSet):
    queryset = TituloPagar.objects.all()
    serializer_class = PagarSerializer
    permission_classes = [IsAuthenticated, ReceberPermission]
    search_fields = ["documento", "contato__nome"]
    filter_order_by = ["documento", "contato__nome"]
    filterset_class = PagarFilter

    @action(detail=True, methods=["post"], url_path="baixar")
    def baixar(self, request, pk=None):
        receber = get_object_or_404(TituloPagar, pk=pk)
        data_pagamento = request.data.get("data_pagamento")

        if not data_pagamento:
            return JsonResponse(
                {"data_pagamento": ["Este campo é obrigatório."]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        receber.data_pagamento = data_pagamento
        receber.status = "P"
        receber.save()

        return JsonResponse({}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"], url_path="estornar")
    def estornar(self, request, pk=None):
        receber = get_object_or_404(TituloPagar, pk=pk)
        receber.data_pagamento = None
        receber.status = "A"
        receber.save()
        return JsonResponse({}, status=status.HTTP_200_OK)
