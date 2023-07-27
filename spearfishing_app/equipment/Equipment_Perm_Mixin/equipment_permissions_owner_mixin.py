from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render


class EquipmentOwnerOrStaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        user = self.request.user
        return user.is_staff or user.id == obj.owner_id

    def handle_no_permission(self):
        return render(self.request, 'accounts/permission_denied.html', status=403)
