
from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS
class FormPermission(permissions.BasePermission):
    # my_safe_method = ['POST']
    def has_permission(self, request, view):
        return request.user.is_authenticated
        
    def has_object_permission(self, request, view, obj):
        if obj.requireLoggedIn:
            if not request.user.is_authenticated:
                return False  
        if obj.status == 'private':
            if request.data.get('key') != obj.key:
                return False
        return True
    

        

        

