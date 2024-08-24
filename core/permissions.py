from rest_framework.permissions import BasePermission


class ContatoPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True

        if view.action == "create":
            return request.user.has_perm("core.add_contato")
        elif view.action == ["list", "retrieve"]:
            return request.user.has_perm("core.view_contato")
        elif view.action in ["update", "partial_update"]:
            return request.user.has_perm("core.change_contato")
        elif view.action == "destroy":
            return request.user.has_perm("core.delete_contato")
        else:
            return False


class FormapagamentoPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True

        if view.action == "create":
            return request.user.has_perm("core.add_formapagamento")
        elif view.action in ["list", "retrieve"]:
            return request.user.has_perm("core.view_formapagamento")
        elif view.action in ["update", "partial_update"]:
            return request.user.has_perm("core.change_formapagamento")
        elif view.action == "destroy":
            return request.user.has_perm("core.delete_formapagamento")
        else:
            return False


class ContaPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True

        if view.action == "create":
            return request.user.has_perm("core.add_conta")
        elif view.action in ["list", "retrieve"]:
            return request.user.has_perm("core.view_conta")
        elif view.action in ["update", "partial_update"]:
            return request.user.has_perm("core.change_conta")
        elif view.action == "destroy":
            return request.user.has_perm("core.delete_conta")
        else:
            return False
