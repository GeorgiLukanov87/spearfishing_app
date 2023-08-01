from django.contrib import admin

from spearfishing_app.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'user', 'location', 'date_of_publication',)
