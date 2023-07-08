from django.contrib import admin

from spearfishing_app.common.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_time_of_publication', 'to_photo', 'user', 'text',)
