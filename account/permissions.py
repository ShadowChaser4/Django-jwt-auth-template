from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool( request.user and
            request.user.is_authenticated and 
            request.user.role == 'Admin'
        )
    
class IsSafeMethods(BasePermission):
    def has_permission(self, request, view):
        return bool( request.user and 
            request.user.is_authenticated and 
            request.method in SAFE_METHODS
        )