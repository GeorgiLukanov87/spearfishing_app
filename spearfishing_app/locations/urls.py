from django.urls import path

from spearfishing_app.locations.views import locations

urlpatterns = (
    path('', locations, name='locations'),
)
