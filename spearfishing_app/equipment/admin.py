from django.contrib import admin

from spearfishing_app.equipment.models import Equipment


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'owner', 'gun_model', 'fins_model', 'fins_model',)
    ordering = ('pk',)
