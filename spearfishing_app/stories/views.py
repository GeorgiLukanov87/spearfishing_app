from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from spearfishing_app.common.helpers.dirty_words_validator import validate_dirty_words
from spearfishing_app.stories.forms import StoryBaseForm, StoryEditForm, StoryCreateForm
from spearfishing_app.stories.models import Story

UserModel = get_user_model()


# stories/views.py

class StoryCreateCBV(generic.CreateView):
    template_name = 'stories/create-story.html'
    form_class = StoryCreateForm
    success_url = reverse_lazy('all-stories')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.description = validate_dirty_words(self.object.description)
        self.object.save()
        return super().form_valid(form)


class StoryListCBV(generic.ListView):
    template_name = 'stories/story-list.html'
    model = Story


class StoryEditCBV(generic.UpdateView):
    template_name = 'stories/edit-story.html'
    model = Story
    form_class = StoryEditForm
    pk_url_kwarg = 'pk'
    context_object_name = 'story'

    def get_success_url(self):
        return reverse_lazy('details-story', kwargs={
            'pk': self.object.pk,
        })

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.description = validate_dirty_words(self.object.description)
        self.object.save()
        return super().form_valid(form)


class StoryDeleteCBV(generic.DeleteView):
    template_name = 'stories/delete-story.html'
    model = Story
    success_url = reverse_lazy('all-stories')


class StoryDetailsCBV(generic.DetailView):
    model = Story
    template_name = 'stories/details-story.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object.creator
        return context


def about(request):
    return render(request, 'common/about.html')


"""
http://127.0.0.1:8000/stories/create/
http://127.0.0.1:8000/stories/edit/1/
http://127.0.0.1:8000/stories/delete/1/
http://127.0.0.1:8000/stories/details/1/
"""
