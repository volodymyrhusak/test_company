from rest_framework.permissions import BasePermission ,SAFE_METHODS
from accounts.models import UserProfile


class IsAllowedToWrite(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        userProfile = UserProfile.objects.get(user=request.user)
        isManager = False
        if userProfile.position == 'manager':
            isManager = True
        return request.user.is_staff or isManager

