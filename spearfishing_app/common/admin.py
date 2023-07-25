from django.contrib import admin

from spearfishing_app.common.models import Comment, Video
from embed_video.admin import AdminVideoMixin


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_time_of_publication', 'to_photo', 'user', 'text',)
    ordering = ('id',)


@admin.register(Video)
class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass
