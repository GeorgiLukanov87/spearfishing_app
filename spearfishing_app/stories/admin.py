from django.contrib import admin

from spearfishing_app.stories.models import Story


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'creator',)
    ordering = ('id',)
