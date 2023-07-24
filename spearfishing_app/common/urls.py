from django.urls import path

from spearfishing_app.common.views import index, like_functionality, add_comment, share, AllUsersCBV, delete_comment, \
    BandCalculator, ApneaTrainer

# common/urls.py
urlpatterns = (

    path('', index, name='index'),

    path('like/<int:photo_id>/', like_functionality, name='like'),
    path('add_comment/<int:photo_id>/', add_comment, name='add-comment'),
    path('delete_comment/<int:photo_id>/<int:comment_pk>/', delete_comment, name='delete-comment'),
    path('share/<int:photo_id>/', share, name='share'),

    path('users-list/', AllUsersCBV.as_view(), name='users-list'),
    path('calculator/', BandCalculator.as_view(), name='calculator'),
    path('apnea-trainer/', ApneaTrainer.as_view(), name='apnea-trainer'),

)
