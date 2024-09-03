from django.db import models


class SituacaoChoice(models.TextChoices):
    ABERTO = "A", "Aberto"
    PAGO = "P", "Pago"


class TipoTituloChoice(models.TextChoices):
    CR = "CR", "Conta Receber"
    CP = "CP", "Conta Pagar"
