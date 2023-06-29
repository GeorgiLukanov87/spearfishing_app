from django.urls import path

from spearfishing_app.events.views import events_list, gift_page

urlpatterns = (
    path('', events_list, name='events-list'),
    path('winner-gift/', gift_page, name='gift-page'),
)
