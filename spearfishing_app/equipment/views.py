from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from spearfishing_app.equipment.equipment_mixins.equipment_required_mixin import \
    EquipmentOwnerOrStaffRequiredMixin
from spearfishing_app.equipment.forms import EquipmentAddForm
from spearfishing_app.equipment.models import Equipment


# equipment/views.py
@login_required
def add_equipment(request):
    if request.method == 'GET':
        form = EquipmentAddForm()
    else:
        form = EquipmentAddForm(request.POST)
        if form.is_valid():
            equipment = form.save(commit=False)
            equipment.owner = request.user
            equipment.save()
            return redirect('index')

    context = {'form': form, }

    return render(
        request,
        'equipment/add-equipment.html',
        context
    )


class EquipmentEditView(LoginRequiredMixin, EquipmentOwnerOrStaffRequiredMixin, generic.UpdateView):
    template_name = 'equipment/edit-equipment.html'
    model = Equipment
    fields = (
        'gun_model', 'gun_material', 'gun_length', 'gun_image',
        'bands', 'bands_brand', 'bands_image',
        'fins_model', 'fins_material', 'fins_image',
        'additional_info'
    )

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={
            'pk': self.request.user.pk,
        })
