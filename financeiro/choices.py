from django.db import models


class SituacaoChoice(models.TextChoices):
    ABERTO = "A", "Aberto"
    PAGO = "P", "Pago"
