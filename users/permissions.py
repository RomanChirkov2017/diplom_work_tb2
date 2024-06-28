from rest_framework import permissions


class IsModer(permissions.BasePermission):
    """Проверяет, входит ли пользователь в группу модератороов."""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moders").exists()
