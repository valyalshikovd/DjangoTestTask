from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Admining').exists()


class IsAuthorizeUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='AuthorizeUser').exists()
