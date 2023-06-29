from django.contrib import admin

from spearfishing_app.equipment.models import Equipment


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    pass
