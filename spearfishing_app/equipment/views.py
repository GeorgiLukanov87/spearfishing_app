from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from spearfishing_app.equipment.forms import EquipmentAddForm


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

    return render(request, 'equipment/add-equipment.html', context)
