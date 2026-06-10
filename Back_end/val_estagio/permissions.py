from rest_framework.permissions import BasePermission

class IsAluno(BasePermission):
    """Permite acesso apenas a usuários com perfil de Aluno."""

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            hasattr(request.user, 'aluno')
        )


class IsSecretaria(BasePermission):
    """Permite acesso apenas a usuários com perfil de Secretaria."""

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            hasattr(request.user, 'secretaria')
        )


class IsCoordenador(BasePermission):
    """Permite acesso apenas a usuários com perfil de Coordenador."""

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            hasattr(request.user, 'coordenador')
        )

class IsSecretariaOuCoordenador(BasePermission):
    def has_permission(self, request, view):
        return IsSecretaria().has_permission(request, view) or \
               IsCoordenador().has_permission(request, view)

class IsSecretariaOuAluno(BasePermission):
    def has_permission(self, request, view):
        return IsSecretaria().has_permission(request, view) or \
               IsAluno().has_permission(request, view)

class IsSecretariaOuCoordenadorOuAluno(BasePermission):
    def has_permission(self, request, view):
        return IsSecretaria().has_permission(request, view) or \
               IsCoordenador().has_permission(request, view) or \
               IsAluno().has_permission(request, view)

class IsCoordenadorOuAluno(BasePermission):
    def has_permission(self, request, view):
        return IsCoordenador().has_permission(request, view) or \
               IsAluno().has_permission(request, view)