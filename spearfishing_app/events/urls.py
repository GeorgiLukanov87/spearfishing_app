from django.urls import path

from spearfishing_app.events.views import events_list

urlpatterns = (
    path('', events_list, name='events-list'),
)
