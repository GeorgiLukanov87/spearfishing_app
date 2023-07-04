from django.urls import path

from spearfishing_app.locations.views import locations, weather

urlpatterns = (
    path('', locations, name='locations'),
    path('weather/', weather, name='weather'),
)
