from rest_framework.permissions import BasePermission


class IsUserOwner(BasePermission):
    """Доступ к объекту для владельца"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class IsUserUser(BasePermission):
    """Доступ на редактирование своего профиля"""

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.id
