from rest_framework import permissions



class AdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        #admin_permission = bool(request.user and request.user.is_stuff)
        #if request.method is get will readonly, if it's admin will also write
        #return request.method == 'GET' or admin_permission
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)


class ReviewUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user == obj.review_user
