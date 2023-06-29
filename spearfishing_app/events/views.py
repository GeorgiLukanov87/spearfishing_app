from django.shortcuts import render

from spearfishing_app.events.models import Event


def events_list(request):
    print(request.user.is_staff)

    events = Event.objects.all()

    context = {
        'events': events,
        'perms': request.user.is_staff,
    }

    return render(request, 'events/events-list.html', context)


def gift_page(request):
    return render(request, 'common/gift-page.html')
