from django.shortcuts import render

from spearfishing_app.events.models import Event


def events_list(request):
    events = Event.objects.all()
    context = {'events': events, }
    return render(request, 'events/events-list.html', context)
