from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect


class StaffPermissionsMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            return redirect('404 error')
        return super().dispatch(request, *args, **kwargs)