from django.urls import path

from spearfishing_app.stories.views import about, all_stories, edite_story, delete_story, details_story, StoryCreateCBV

urlpatterns = (
    path('about/', about, name='about'),
    path('', all_stories, name='all-stories'),

    path('create/', StoryCreateCBV.as_view(), name='create-story'),

    path('edit/<int:pk>/', edite_story, name='edit-story'),
    path('delete/<int:pk>/', delete_story, name='delete-story'),
    path('details/<int:pk>/', details_story, name='details-story'),
)

"""
http://127.0.0.1:8000/stories/create/
http://127.0.0.1:8000/stories/edit/1/
http://127.0.0.1:8000/stories/delete/1/
http://127.0.0.1:8000/stories/details/1/
"""
