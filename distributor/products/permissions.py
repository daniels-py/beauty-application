from rest_framework.permissions import BasePermission

class IsAdminUserRole(BasePermission):
    """
    Permiso para permitir acceso solo a usuarios con rol 'admin'.
    """
    def has_permission(self, request, view):
        # Verifica que el usuario esté autenticado y tenga el rol 'admin'
        return request.user.is_authenticated and request.user.role == 'admin'
