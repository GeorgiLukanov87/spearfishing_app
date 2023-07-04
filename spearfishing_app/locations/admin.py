from django.contrib import admin

from spearfishing_app.locations.models import Search


@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = ('address', 'date',)
