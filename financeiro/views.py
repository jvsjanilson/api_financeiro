from decimal import Decimal
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
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.utils.timezone import make_aware
from datetime import datetime
from rest_framework.views import APIView


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


# Crie uma view para listar o fluxo de caixa
class FluxoCaixaViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data_inicial = request.GET.get("data_inicial")
        data_final = request.GET.get("data_final")

        if not data_inicial or not data_final:
            return JsonResponse(
                {"error": "As datas de início e fim são obrigatórias."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        data_inicial = make_aware(datetime.strptime(data_inicial, "%Y-%m-%d"))
        data_final = make_aware(datetime.strptime(data_final, "%Y-%m-%d"))

        receber_entradas = (
            TituloReceber.objects.filter(
                data_pagamento__range=(data_inicial, data_final), status="P"
            )
            .values("data_pagamento")
            .annotate(entradas=Coalesce(Sum("valor"), Decimal("0.00")))
        )

        pagar_saidas = (
            TituloPagar.objects.filter(
                data_pagamento__range=(data_inicial, data_final), status="P"
            )
            .values("data_pagamento")
            .annotate(saidas=Coalesce(Sum("valor"), Decimal("0.00")))
        )

        # fluxo_caixa = []
        # for entrada in receber_entradas:
        #     data = entrada["data_pagamento"]
        #     valor_entrada = entrada["entradas"]
        #     valor_saida = 0.00
        #     saldo = valor_entrada

        #     for saida in pagar_saidas:
        #         if saida["data_pagamento"] == data:
        #             valor_saida = saida["saidas"]
        #             saldo = valor_entrada - valor_saida
        #             pagar_saidas = pagar_saidas.exclude(data_pagamento=data)
        #             break

        #     fluxo_caixa.append(
        #         {
        #             "data": data,
        #             "valor_entrada": valor_entrada,
        #             "valor_saida": valor_saida,
        #             "saldo": saldo,
        #         }
        #     )

        return JsonResponse(
            {"entradas": list(receber_entradas)}, status=status.HTTP_200_OK
        )

    # def get(self, request):
    #     data_inicial = request.GET.get("data_inicial")
    #     data_final = request.GET.get("data_final")

    #     if not data_inicial or not data_final:
    #         return JsonResponse(
    #             {"error": "As datas de início e fim são obrigatórias."},
    #             status=status.HTTP_400_BAD_REQUEST,
    #         )

    #     data_inicial = make_aware(datetime.strptime(data_inicial, "%Y-%m-%d"))
    #     data_final = make_aware(datetime.strptime(data_final, "%Y-%m-%d"))

    #     receber_entradas = TituloReceber.objects.filter(
    #         data_pagamento__range=(data_inicial, data_final), status="P"
    #     ).aggregate(entradas=Coalesce(Sum("valor"), Decimal("0.00")))

    #     pagar_saidas = TituloPagar.objects.filter(
    #         data_pagamento__range=(data_inicial, data_final), status="P"
    #     ).aggregate(saidas=Coalesce(Sum("valor"), Decimal("0.00")))

    #     saldo = receber_entradas["entradas"] - pagar_saidas["saidas"]

    #     return JsonResponse(
    #         {
    #             "valor_entrada": receber_entradas["entradas"],
    #             "valor_saida": pagar_saidas["saidas"],
    #             "saldo": saldo,
    #         },
    #         status=status.HTTP_200_OK,
    #     )
