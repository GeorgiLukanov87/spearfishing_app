from django.shortcuts import render, redirect

from spearfishing_app.equipment.forms import EquipmentAddForm


def add_equipment(request):
    if request.method == 'GET':
        form = EquipmentAddForm()
    else:
        form = EquipmentAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form, }

    return render(request, 'equipment/add-equipment.html', context)
