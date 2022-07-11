from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user == None:
            return False

        if obj.user is None:
            raise Exception("Object has no user")

        return obj.user == request.user
