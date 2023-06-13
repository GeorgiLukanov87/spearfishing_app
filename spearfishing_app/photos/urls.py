from django.urls import path, include

from spearfishing_app.photos.views import add_photo, show_photo_details, edit_photo, delete_photo

# photos/urls

urlpatterns = (
    path('', include(
        [
            path('add/', add_photo, name='add-photo'),
            path('<int:pk>/', show_photo_details, name='photo-details'),
            path('edit/<int:pk>/', edit_photo, name='edit-photo'),
            path('delete/<int:pk>/', delete_photo, name='delete-photo'),
        ]
    )),

)
