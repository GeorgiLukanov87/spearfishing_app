from django.contrib import admin

from spearfishing_app.events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'location',)
