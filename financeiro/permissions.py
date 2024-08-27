from rest_framework.permissions import BasePermission

class ReceberPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True

        if view.action == "create":
            return request.user.has_perm("financeiro.add_receber")
        elif view.action in ["list", "retrieve"]:
            return request.user.has_perm("financeiro.view_receber")
        elif view.action in ["update", "partial_update"]:
            return request.user.has_perm("financeiro.change_receber")
        elif view.action == "destroy":
            return request.user.has_perm("financeiro.delete_receber")
        else:
            return False