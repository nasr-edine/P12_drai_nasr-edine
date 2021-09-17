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
        # print(request.user.role)
        # # Read-only permissions are allowed for any request
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        # # Write permissions are only allowed to the author of a post
        # return obj.is_superuser == request.user.is_superuser
