from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='Admining').exists()


class IsAuthorizeUser(permissions.BasePermission):
    def has_permission(self, request, view):
        print("method was called")
        return request.user.is_authenticated and request.user.groups.filter(name='AuthorizeUser').exists()
