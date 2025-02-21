from rest_framework.permissions import IsAdminUser
from rest_framework import permissions


class AdminOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        admin_permission=bool(request.use and request.user.is_saff)
        return request.method == "GET" or admin_permission