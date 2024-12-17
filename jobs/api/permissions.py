from rest_framework import permissions


class IsCompanyJobInstance(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif obj.company.user == request.user:
            return True

        return False


class IsCompanyOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.job.company.user == request.user:
            return True

        return False
