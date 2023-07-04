from django.urls import path

from spearfishing_app.stories.views import about, StoryListCBV, StoryEditCBV, StoryDeleteCBV, details_story, \
    StoryCreateCBV

urlpatterns = (
    path('about/', about, name='about'),
    path('', StoryListCBV.as_view(), name='all-stories'),

    path('create/', StoryCreateCBV.as_view(), name='create-story'),

    path('edit/<int:pk>/', StoryEditCBV.as_view(), name='edit-story'),
    path('delete/<int:pk>/', StoryDeleteCBV.as_view(), name='delete-story'),
    path('details/<int:pk>/', details_story, name='details-story'),
)

"""
http://127.0.0.1:8000/stories/create/
http://127.0.0.1:8000/stories/edit/1/
http://127.0.0.1:8000/stories/delete/1/
http://127.0.0.1:8000/stories/details/1/
"""
