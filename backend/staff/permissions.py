from rest_framework import permissions


class IsSuperUserOrManager(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.role == 'management':
            return True
        return False


class IsManagerOrSalesman(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
        if request.user.role == 'management':
            return True
        if request.user.role == 'sales':
            return True
        return False


class IsManagerOrSalesContact(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
        if request.user.role == 'management':
            return True
        return obj.sales_contact == request.user


class IsManagerOrSupportMan(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
        if request.user.role == 'management':
            return True
        if request.user.role == 'support':
            return True
        return False


class IsManagerOrSupportContact(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
        if request.user.role == 'management':
            return True
        return obj.support_contact == request.user
