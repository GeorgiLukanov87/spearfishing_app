from django.urls import path

from spearfishing_app.stories.views import about

urlpatterns = (
    path('about/', about, name='about'),
)
