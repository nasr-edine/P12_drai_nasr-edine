from rest_framework import permissions

# class IsManager(permissions.BasePermission):


class IsSuperUserOrManager(permissions.BasePermission):
    def has_permission(self, request, view):
        print("IsSuperUserOrManager called")
        if request.user.is_superuser == True:
            print('it\'s ok for you because you are superuser')
            return True
        elif request.user.role == 'management':
            print('it\'s also ok for manager')
            return True
        else:
            print(f'it\'s not ok for you because you are {request.user.role}')
            return False


class IsManagerOrSalesman(permissions.BasePermission):
    def has_permission(self, request, view):
        print("IsManagerorSalesman called")
        if request.user.is_superuser == True:
            print('it\'s ok for you because you are superuser')
            return True
        elif request.user.role == 'management' or request.user.role == 'sales':
            print('it\'s also ok for manager and salesman')
            return True
        else:
            print(f'it\'s not ok for you because you are {request.user.role}')
            return False


class IsManagerOrSalesContact(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Instance must have an attribute named `owner`.
        if request.user.role == 'management' or request.user.is_superuser == True:
            return True
        return obj.sales_contact == request.user


class IsManagerOrSupportContact(permissions.BasePermission):
    def has_permission(self, request, view):
        print("IsManagerorSalesman called")
        if request.user.is_superuser == True:
            print('it\'s ok for you because you are superuser')
            return True
        elif request.user.role == 'management' or request.user.role == 'support':
            print('it\'s also ok for manager and support')
            return True
        else:
            print(f'it\'s not ok for you because you are {request.user.role}')
            return False
