from django.urls import path

from spearfishing_app.events.views import events_list, gift_page, CreateEventCBV, edit_event, delete_event

urlpatterns = (
    path('', events_list, name='events-list'),
    path('winner-gift/', gift_page, name='gift-page'),
    path('create/', CreateEventCBV.as_view(), name='create-event'),
    path('update/<int:pk>/', edit_event, name='edit-event'),
    path('delete/<int:pk>/', delete_event, name='delete-event'),
)
