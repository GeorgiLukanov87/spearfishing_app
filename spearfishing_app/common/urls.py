from django.urls import path

from spearfishing_app.common.views import index, like_functionality, add_comment, share, AllUsersCBV

urlpatterns = (

    path('', index, name='index'),
    path('like/<int:photo_id>/', like_functionality, name='like'),
    path('add_comment/<int:photo_id>/', add_comment, name='add-comment'),
    path('share/<int:photo_id>/', share, name='share'),
    path('users-list/', AllUsersCBV.as_view(), name='users-list'),

)
