from django.db import models
from core.models import Base, Contato, Conta, Formapagamento
from financeiro.choices import SituacaoChoice, TipoTituloChoice


class Titulo(Base):
    tipo_titulo = models.CharField(
        max_length=2, choices=TipoTituloChoice.choices, default=TipoTituloChoice.CR
    )
    documento = models.CharField(max_length=20)
    contato = models.ForeignKey(Contato, on_delete=models.RESTRICT)
    conta = models.ForeignKey(Conta, on_delete=models.RESTRICT)
    formapagamento = models.ForeignKey(Formapagamento, on_delete=models.RESTRICT)
    data_emissao = models.DateField()
    data_vencimento = models.DateField()
    data_pagamento = models.DateField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=1, choices=SituacaoChoice.choices, default=SituacaoChoice.ABERTO
    )
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.documento
