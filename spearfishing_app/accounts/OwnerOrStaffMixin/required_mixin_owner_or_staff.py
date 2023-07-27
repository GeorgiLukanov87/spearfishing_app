from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.urls import reverse_lazy


class OwnerOrStaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.is_staff or user == self.get_object()

    # def handle_no_permission(self):
    #     if self.raise_exception:
    #         raise PermissionDenied("You don't have permission to access this page.")
    #     return redirect(reverse_lazy('index'))
    def handle_no_permission(self):
        return render(self.request, 'accounts/permission_denied.html', status=403)
