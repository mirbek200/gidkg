from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

from apps.users.models import MyUser


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class IsManager(IsAuthenticated):
    def has_permission(self, request, view):
        is_authenticated = super().has_permission(request, view)
        user = MyUser.objects.get(user=request.user)
        if not is_authenticated:
            return False

        return user.is_manager
