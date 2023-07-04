from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from spearfishing_app.stories.forms import StoryBaseForm


# stories/views.py

class StoryCreateCBV(generic.CreateView):
    template_name = 'stories/create-story.html'
    form_class = StoryBaseForm
    success_url = reverse_lazy('index')


def all_stories(request):
    return render(request, 'stories/story-list.html')


def edite_story(request, pk):
    return render(request, 'stories/edit-story.html')


def delete_story(request, pk):
    return render(request, 'stories/delete-story.html')


def details_story(request, pk):
    return render(request, 'stories/details-story.html')


def about(request):
    return render(request, 'common/about.html')


"""
http://127.0.0.1:8000/stories/create/
http://127.0.0.1:8000/stories/edit/1/
http://127.0.0.1:8000/stories/delete/1/
http://127.0.0.1:8000/stories/details/1/
"""
