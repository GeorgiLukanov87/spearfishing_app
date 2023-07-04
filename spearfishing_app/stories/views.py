from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from spearfishing_app.stories.forms import StoryBaseForm, StoryEditForm
from spearfishing_app.stories.models import Story

UserModel = get_user_model()


# stories/views.py

class StoryCreateCBV(generic.CreateView):
    template_name = 'stories/create-story.html'
    form_class = StoryBaseForm
    success_url = reverse_lazy('index')


def all_stories(request):
    return render(request, 'stories/story-list.html')


class StoryEditCBV(generic.UpdateView):
    template_name = 'stories/edit-story.html'
    model = Story
    form_class = StoryEditForm
    pk_url_kwarg = 'pk'
    context_object_name = 'story'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user_profile'] = UserModel
    #     return context

    def get_success_url(self):
        return reverse_lazy('details-story', kwargs={
            'pk': self.object.pk,
        })


class StoryDeleteCBV(generic.DeleteView):
    template_name = 'stories/delete-story.html'
    model = Story
    success_url = reverse_lazy('index')


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
