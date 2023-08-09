from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from spearfishing_app.events.forms import EventCreateForm, EventEditForm, EventDeleteForm
from spearfishing_app.events.models import Event


# events/views.py
def events_list(request):
    events = Event.objects.all()
    context = {
        'events': events,
        'perms': request.user.is_staff,
    }

    return render(request, 'events/events-list.html', context)


class CreateEventCBV(LoginRequiredMixin, generic.CreateView):
    template_name = 'events/create-event.html'
    form_class = EventCreateForm
    success_url = reverse_lazy('events-list')


def is_staff_user(user):
    return user.is_staff


@login_required
@user_passes_test(is_staff_user, login_url=reverse_lazy('events-list'))
def edit_event(request, pk):
    event = Event.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EventEditForm(instance=event)
    else:
        form = EventEditForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events-list')

    context = {'form': form, 'event': event, }

    return render(request, 'events/edit-event.html', context, )


@login_required
@user_passes_test(is_staff_user, login_url=reverse_lazy('events-list'))
def delete_event(request, pk):
    event = Event.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EventDeleteForm(instance=event)
    else:
        form = EventDeleteForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events-list')

    context = {'form': form, 'event': event, }

    return render(request, 'events/delete-event.html', context)


def gift_page(request):
    return render(request, 'common/gift-page.html')
