from rest_framework import status
from rest_framework.response import Response
from django.db.models import RestrictedError


class HandleRestrictedErrorMixin:
    def destroy(self, request, *args, **kwargs):
        try:

            return super().destroy(request, *args, **kwargs)
        except RestrictedError:
            return Response(
                {
                    "detail": "Não é possível deletar este registro porque ele está vinculado a outro registro."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
