from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Custom permission to allow access only to admin users
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_staff
    