from django.urls import path

from spearfishing_app.common.views import index

urlpatterns = (

    path('', index, name='index'),

)
