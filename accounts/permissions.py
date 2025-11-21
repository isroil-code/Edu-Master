from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin

class IsStudentMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.role == 'STUDENT':
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
    

class IsTeacherMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.role == 'TEACHER':
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
    
class IsAdminMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.role == 'ADMIN':
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
    
class BoughtCourse(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.role == 'ADMIN':
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)